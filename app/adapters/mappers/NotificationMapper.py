from app.adapters.models.NotificationModel import NotificationModel
from app.core.entities.Notification import Notification


class NotificationMapper:
    @staticmethod
    def to_entity(model: NotificationModel) -> Notification:
        return Notification(
            model.receiver_id,
            model.message,
            model.created_at,
            model.is_read,
            model.id
        )

    @staticmethod
    def update_model(model: NotificationModel, notification: Notification) -> None:
        model.message = notification.message
        model.is_read = notification.is_read

    @staticmethod
    def to_model(notification: Notification) -> NotificationModel:
        return NotificationModel(
            message = notification.message,
            created_at = notification.created_at,
            is_read = notification.is_read
        )
