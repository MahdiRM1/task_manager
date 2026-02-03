from sqlalchemy.orm import Session

from app.adapters.Exceptions import IdNotFound
from app.adapters.mappers.NotificationMapper import NotificationMapper
from app.adapters.models.NotificationModel import NotificationModel
from app.core.entities.Notification import Notification
from app.domain.repositories.NotificationRepository import NotificationRepository


class SqlNotificationRepository(NotificationRepository):
    def __init__(self, session: Session):
        self.session = session


    def add(self, notification: Notification) -> None:
        model = NotificationMapper.to_model(notification)
        self.session.add(model)
        self.session.flush()
        self.session.commit()
        notification._set_id(model.id)

    def remove(self, notification: Notification) -> None:
        model = self.session.get(NotificationModel, notification.id)
        if model:
            self.session.delete(model)
            self.session.commit()

    def update(self, notification: Notification) -> None:
        model = self.session.get(NotificationModel, notification.id)
        if model:
            NotificationMapper.update_model(model, notification)
            self.session.commit()

    def get_by_id(self, notification_id : int) ->  Notification:
        model = self.session.get(NotificationModel, notification_id)

        if not model:
            raise IdNotFound(f'Notification id {notification_id} not found.')

        notification = NotificationMapper.to_entity(model)
        return notification
