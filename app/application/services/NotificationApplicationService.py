from datetime import datetime
from app.core.entities.Notification import Notification

class NotificationService:
    def __init__(self):
        self.notifications = []

    def send_notification(self, receiver_id, msg):
        notification = Notification(receiver_id, msg, datetime.now())
        self.notifications.append(notification)
        print(f"Notification sent to {receiver_id}: {msg}")
        return notification

    def mark_as_read(self, notification):
        notification.mark_as_read()
        if notification in self.notifications:
            self.notifications.remove(notification)
        print(f"Notification for {notification.receiver_id} marked as read and removed.")
