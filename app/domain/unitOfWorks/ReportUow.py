from abc import ABC, abstractmethod

from app.domain.repositories.ReportRepository import ReportRepository
from app.domain.repositories.TaskRepository import TaskRepository
from app.domain.repositories.UserRepository import UserRepository


class ReportUow(ABC):
    reports: ReportRepository
    tasks: TaskRepository
    users: UserRepository

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass