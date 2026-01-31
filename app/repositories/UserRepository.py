from abc import ABC, abstractmethod

from app.core.entities.User import User

class UserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def remove(self, user: User) -> None:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass