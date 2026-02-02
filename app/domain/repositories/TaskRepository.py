from abc import ABC, abstractmethod

from app.core.entities.Task import Task


class TaskRepository(ABC):

    @abstractmethod
    def add(self, task:Task) -> None:
        pass

    @abstractmethod
    def remove(self, task:Task) -> None:
        pass

    @abstractmethod
    def update(self, task:Task) -> None:
        pass

    @abstractmethod
    def get_by_id(self, task_id:int) -> Task:
        pass

    @abstractmethod
    def has_tasks(self, user_id:int) -> bool:
        pass