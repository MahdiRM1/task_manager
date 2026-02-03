from app.adapters.models.TaskModel import TaskModel
from app.core.entities.Task import Task


class TaskMapper:
    @staticmethod
    def to_entity(model: TaskModel) -> Task:
        tag_ids=[tag.id for tag in model.tags]

        return Task(
           model.creator_id,
           model.assignee_id,
           model.name,
           model.description,
           model.board_id,
           model.created_at,
           model.deadline,
           model.status.name,
           tags=tag_ids,
           id=model.id
        )

    @staticmethod
    def update_model(model: TaskModel, task: Task) -> None:
        model.assignee_id = task.assignee_id
        model.name = task.name
        model.description = task.description
        model.board_id = task.board_id
        model.deadline = task.deadline
        model.status = task.status

    @staticmethod
    def to_model(task: Task) -> TaskModel:
        return TaskModel(
            creator_id=task.creator_id,
            assignee_id=task.assignee_id,
            name=task.name,
            description=task.description,
            board_id=task.board_id,
            deadline=task.deadline,
            created_at=task.created_at,
            status=task.status
        )