from abc import ABC, abstractmethod

from app.core.entities.Notification import Notification


class NotificationRepository(ABC):

    @abstractmethod
    def add(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def remove(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def update(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def get_by_id(self, notification_id : int) -> Notification | None:
        pass