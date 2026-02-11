from abc import ABC, abstractmethod

from app.domain.repositories.BoardRepository import BoardRepository
from app.domain.repositories.TagRepository import TagRepository
from app.domain.repositories.TaskRepository import TaskRepository
from app.domain.repositories.UserRepository import UserRepository


class TaskUow(ABC):
    tasks: TaskRepository
    users: UserRepository
    tags: TagRepository
    boards: BoardRepository

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass