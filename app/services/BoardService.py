from app.core.entities.Board import Board

class BoardService:
    def __init__(self, board_repo, loader):
        self.board_repo = board_repo
        self.loader = loader

    def create_board(self, name):
        board = Board(name)
        self.board_repo.add(board)

    def remove_board(self, board_id):
        board = self.loader.get_board(board_id)
        self.board_repo.remove(board)