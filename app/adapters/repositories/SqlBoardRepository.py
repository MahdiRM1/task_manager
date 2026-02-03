from sqlalchemy.orm import Session

from app.adapters.Exceptions import IdNotFound
from app.adapters.models.BoardModel import BoardModel
from app.core.entities.Board import Board
from app.domain.repositories.BoardRepository import BoardRepository

class SqlBoardRepository(BoardRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, board:Board) -> None:
        model = BoardModel(name = board.name)
        self.session.add(model)
        self.session.flush()
        self.session.commit()
        board._set_id(model.id)

    def remove(self, board:Board) -> None:
        model = self.session.get(BoardModel, board.get_id())
        if model:
            self.session.delete(model)
            self.session.commit()

    def get_by_id(self, board_id:int) -> Board:
        model = self.session.get(BoardModel, board_id)

        if not model:
            raise IdNotFound(f'Board id {board_id} not found.')

        board = Board(model.name, model.id)
        return board