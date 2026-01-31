from abc import ABC, abstractmethod

from app.core.entities.Board import Board


class BoardRepository(ABC):

    @abstractmethod
    def add(self, board:Board) -> None:
        pass

    @abstractmethod
    def remove(self, board:Board) -> None:
        pass

    @abstractmethod
    def get_by_id(self, board_id:int) -> Board:
        pass