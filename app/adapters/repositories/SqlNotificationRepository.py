from sqlalchemy.orm import Session

from app.adapters.Models.NotificationModel import NotificationModel
from app.core.entities.Notification import Notification
from app.domain.repositories.NotificationRepository import NotificationRepository


class SqlNotificationRepository(NotificationRepository):
    def __init__(self, session: Session):
        self.session = session


    def add(self, notification: Notification) -> None:
        notification_model = NotificationModel(
            message = notification.message,
            created_at = notification.created_at,
            is_read = notification.is_read
        )
        self.session.add(notification_model)
        self.session.flush()
        self.session.commit()
        notification.id = notification_model.id

    def remove(self, notification: Notification) -> None:
        notification_model = self.session.get(NotificationModel, notification.id)
        if notification_model:
            self.session.delete(notification_model)
            self.session.commit()

    def update(self, notification: Notification) -> None:
        notification_model = self.session.get(NotificationModel, notification.id)
        if notification_model:
            notification_model.message = notification.message
            notification_model.is_read = notification.is_read
            self.session.commit()

    def get_by_id(self, notification_id : int) -> Notification | None:
        notification_model = self.session.get(NotificationModel, notification_id)

        if not notification_model:
            return None

        notification = Notification(
            notification_model.receiver_id,
            notification_model.message,
            notification_model.created_at,
            notification_model.is_read
        )
        notification.id = notification_model.id
        return notification
