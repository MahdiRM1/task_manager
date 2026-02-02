from sqlalchemy.orm import Session

from app.adapters.Models.BoardModel import BoardModel
from app.core.entities.Board import Board
from app.domain.repositories.BoardRepository import BoardRepository

class SqlBoardRepository(BoardRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, board:Board) -> None:
        board_model = BoardModel(
            name = board.name
        )
        self.session.add(board_model)
        self.session.flush()
        self.session.commit()
        board.id = board_model.id

    def remove(self, board:Board) -> None:
        board_model = self.session.query(BoardModel).get(board.id)
        if board_model:
            self.session.delete(board_model)
            self.session.commit()

    def get_by_id(self, board_id:int) -> Board | None:
        board_model = self.session.get(BoardModel, board_id)

        if not board_model:
            return None

        board = Board(board_model.name)
        board.id = board_model.id
        return board