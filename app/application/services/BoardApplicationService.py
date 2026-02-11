from app.core.entities.Board import Board

class BoardApplicationService:
    def __init__(self, board_uow):
        self._uow = board_uow

    def create_board(self, name):
        with self._uow:
            board = Board(name)
            self._uow.boards.add(board)

    def remove_board(self, board_id):
        with self._uow:
            board = self._uow.boards.get(board_id)
            self._uow.boards.remove(board)
