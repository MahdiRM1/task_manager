from abc import ABC, abstractmethod

from app.domain.repositories.UserRepository import UserRepository

class UserUow(ABC):
    users: UserRepository

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass