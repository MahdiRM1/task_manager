from app.adapters.repositories.SqlBoardRepository import SqlBoardRepository
from app.adapters.repositories.SqlTagRepository import SqlTagRepository
from app.adapters.repositories.SqlTaskRepository import SqlTaskRepository
from app.adapters.repositories.SqlUserRepository import SqlUserRepository
from app.domain.unitOfWorks.TaskUow import TaskUow


class SqlTaskUow(TaskUow):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.tasks = SqlTaskRepository(self.session)
        self.users = SqlUserRepository(self.session)
        self.tags = SqlTagRepository(self.session)
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