from sqlalchemy.orm import Session

from app.adapters.Models.TaskModel import TaskModel
from app.core.entities.Task import Task
from app.domain.repositories.TaskRepository import TaskRepository


class SqlTaskRepository(TaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, task:Task) -> None:
        task_model = TaskModel(
            creator_id=task.creator_id,
            assignee_id=task.assignee_id,
            name=task.name,
            description=task.description,
            board_id=task.board_id,
            deadline=task.deadline,
            created_at=task.created_at,
            status=task.status
        )
        self.session.add(task_model)
        self.session.flush()
        self.session.commit()
        task.id = task_model.id

    def remove(self, task:Task) -> None:
        task_model = self.session.get(TaskModel, task.id)
        if task_model:
            self.session.delete(task_model)
            self.session.commit()

    def update(self, task:Task) -> None:
        task_model = self.session.get(TaskModel, task.id)

        if task_model:
            task_model.assignee_id = task.assignee_id
            task_model.name = task.name
            task_model.description = task.description
            task_model.board_id = task.board_id
            task_model.deadline = task.deadline
            task_model.status=task.status
            self.session.commit()

    def get_by_id(self, task_id:int) -> Task | None:
        task_model = self.session.get(TaskModel, task_id)

        if not task_model:
            return None

        tag_ids = []
        for tag in task_model.tags:
            tag_ids.append(tag.id)

        task = Task(
            task_model.creator_id,
            task_model.assignee_id,
            task_model.name,
            task_model.description,
            task_model.board_id,
            task_model.created_at,
            task_model.deadline,
            task_model.status.name,
            tags=tag_ids
        )
        task.id = task_model.id
        return task