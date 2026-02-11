from abc import ABC, abstractmethod

from app.domain.repositories.BoardRepository import BoardRepository


class BoardUoW(ABC):
    boards: BoardRepository

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass