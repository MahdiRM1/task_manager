from app.domain.unitOfWorks.boardUow import BoardUoW

from app.adapters.repositories.SqlBoardRepository import SqlBoardRepository


class SqlBoardUow(BoardUoW):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.boards = SqlBoardRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else :
            self.session.commit()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()