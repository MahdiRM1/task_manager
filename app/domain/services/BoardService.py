from app.core.entities.Board import Board

class BoardService:
    def __init__(self, board_repo):
        self.board_repo = board_repo

    def create_board(self, name):
        board = Board(name)
        self.board_repo.add(board)

    def remove_board(self, board_id):
        board = self.board_repo.get_by_id(board_id)
        self.board_repo.remove(board)