from datetime import datetime

from app.core.entities.Notification import Notification


class NotificationService:
    def __init__(self, notification_repo):
        self.notification_repo = notification_repo

    def send_notification(self, receiver_id, msg):
        notification = Notification(receiver_id, msg, datetime.now())
        self.notification_repo.add(notification)

    def mark_as_read(self, actor_id, notification_id):
        notification = self.notification_repo.get_by_id(notification_id)
        notification.mark_as_read(actor_id)
        self.notification_repo.update(notification)

    def remove_notification(self, notification_id):
        notification = self.notification_repo.get_by_id(notification_id)
        self.notification_repo.remove(notification)