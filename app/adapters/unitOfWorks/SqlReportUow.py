from app.adapters.repositories.SqlReportRepository import SqlReportRepository
from app.adapters.repositories.SqlTaskRepository import SqlTaskRepository
from app.adapters.repositories.SqlUserRepository import SqlUserRepository
from app.domain.unitOfWorks.ReportUow import ReportUow


class SqlReportUow(ReportUow):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.reports = SqlReportRepository(self.session)
        self.tasks = SqlTaskRepository(self.session)
        self.users = SqlUserRepository(self.session)
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