from app.core.entities.User import User
from app.domain.Exceptions import UserCannotRemove


class UserApplicationService:
    def __init__(self, uow, notification_services):
        self._uow = uow
        self.notification_services = notification_services

    def create_user(self, name):
        with self._uow:
            user = User(name)
            self._uow.users.add(user)

    def rename_user(self, user_id, new_name):
        with self._uow:
            user = self._uow.users.get_by_id(user_id)
            old_name = user.name
            user.rename(new_name)
            self._uow.users.update(user)

        msg = f'User {old_name} with id {user.id} has been renamed to {new_name}'
        self.notification_services.send_notification(user.id, msg)

    def remove_user(self, user_id):
        with self._uow:
            user = self._uow.users.get_by_id(user_id)
            if self._uow.users.has_tasks(user.id):
                raise UserCannotRemove(user.id)
            self._uow.users.remove(user)

        msg = f'User {user_id} has been removed'
        self.notification_services.send_notification(user.id, msg)