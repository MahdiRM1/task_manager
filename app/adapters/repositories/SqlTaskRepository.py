from sqlalchemy.orm import Session

from app.adapters.Exceptions import IdNotFound
from app.adapters.mappers.TaskMapper import TaskMapper
from app.adapters.models.TaskModel import TaskModel
from app.core.entities.Task import Task
from app.domain.repositories.TaskRepository import TaskRepository


class SqlTaskRepository(TaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, task:Task) -> None:
        model = TaskMapper.to_model(task)
        self.session.add(model)
        self.session.flush()
        task._set_id(model.id)

    def remove(self, task:Task) -> None:
        model = self.session.get(TaskModel, task.get_id())
        if model:
            self.session.delete(model)

    def update(self, task:Task) -> None:
        model = self.session.get(TaskModel, task.get_id())

        if model:
            TaskMapper.update_model(model, task)

    def get_by_id(self, task_id: int) -> Task:
        model = self.session.get(TaskModel, task_id)

        if not model:
            raise IdNotFound(f'Task with id {task_id} not found')

        task = TaskMapper.to_entity(model)
        return task