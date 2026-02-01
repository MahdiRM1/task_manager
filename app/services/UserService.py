from app.core.entities.User import User
from app.services.Exceptions import UserCannotRemove
from app.services.Helper import get_by_id


class UserService:
    def __init__(self, task_repo, user_repo, notification_services):
        self.task_repo = task_repo
        self.user_repo = user_repo
        self.notification_services = notification_services

    def create_user(self, name):
        user = User(name)
        self.user_repo.add(user)

    def rename_user(self, user_id, new_name):
        user = get_by_id(self.user_repo, user_id)
        old_name = user.name
        user.rename(new_name)
        self.user_repo.update(user)
        msg = f'User {old_name} with id {user.id} has been renamed to {new_name}'
        self.notification_services.send_notification(user, msg)

    def remove_user(self, user_id):
        user = get_by_id(self.user_repo, user_id)
        if not self.task_repo.has_tasks(user.id):
            raise UserCannotRemove(user.id)
        self.user_repo.remove(user)
        msg = f'User {user_id} has been removed'
        self.notification_services.send_notification(user, msg)