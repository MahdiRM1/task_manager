from datetime import datetime

from app.core.entities.Notification import Notification
from app.services.Exceptions import PermissionDenied
from app.services.Helper import get_by_id


class NotificationService:
    def __init__(self, notification_repo):
        self.notification_repo = notification_repo

    def send_notification(self, receiver, msg):
        notification = Notification(receiver, msg, datetime.now())
        self.notification_repo.add(notification)

    def mark_as_read(self, actor_id, notification_id):
        notification = get_by_id(self.notification_repo, notification_id)
        if notification.receiver.id != actor_id:
            raise PermissionDenied()
        notification.mark_as_read()
        self.notification_repo.update(notification)

    def remove_notification(self, actor_id, notification_id):
        notification = get_by_id(self.notification_repo, notification_id)
        if notification.receiver.id != actor_id:
            raise PermissionDenied()
        self.notification_repo.remove(notification)