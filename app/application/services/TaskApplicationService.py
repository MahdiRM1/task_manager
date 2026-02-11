from datetime import datetime

from app.core.entities.Tag import Tag
from app.core.entities.Task import Task
from app.domain.Exceptions import *


class TaskApplicationService:
    def __init__(self, uow, notification_services):
        self._uow = uow
        self.notification_services = notification_services

    def add_task(self, creator_id, assignee_id, name, description,  board_id, deadline):
        with self._uow:
            creator = self._uow.users.get_by_id(creator_id)
            assignee = self._uow.users.get_by_id(assignee_id)
            board = self._uow.boards.get_by_id(board_id)
            now = datetime.now()
            task = Task(creator_id, assignee_id, name, description, board_id, now, deadline)
            self._uow.tasks.add(task)
        msg = (f'Task {task.name} with ID {task.get_id()} was added.\n'
               f'creator: {creator.name}\n'
               f'assignee: {assignee.name}'
               f'board: {board.name}\n')
        self._notify_both(task, msg)

    def remove_task(self, actor_id, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            if actor_id != task.creator_id:
                raise PermissionDenied()
            self._uow.tasks.remove(task)
        msg = f'Task {task.name} with ID {task.id} was removed.\n'
        self._notify_both(task, msg)

    def task_done(self, actor_id, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            task.done(actor_id)
            self._uow.tasks.update(task)
        msg = f'Task {task.name} with ID {task.id} is Done.'
        self._notify_both(task, msg)

    def assign_task(self, actor_id, assignee_id, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            assignee = self._uow.users.get_by_id(assignee_id)
            old_assignee = task.assignee
            task.assign_to(actor_id, assignee)
            self._uow.tasks.update(task)
        msg = f'Task {task.name} with ID {task.id} was assigned to User ID {assignee.id}.'
        self._notify_both(task, msg)
        if old_assignee and old_assignee.id != task.creator.id:
            self.notification_services.send_notification(old_assignee.id, msg)

    def move_task(self, actor_id, board_id, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            board = self._uow.boards.get_by_id(board_id)
            task.move_to(actor_id, board)
            self._uow.tasks.update(task)
        msg = f'task {task.name} with ID {task.id} was moved to Board {board.name}.'
        self._notify_both(task, msg)

    def add_tag_to_task(self, actor_id, tag_name, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            tag = self._uow.tags.get_by_name(tag_name)
            if not tag:
                tag = Tag(tag_name)
                self._uow.tags.add(tag)
            task.add_tag(actor_id, tag)
            self._uow.tasks.update(task)

    def remove_tag_task(self, actor_id, tag_name, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            tag = self._uow.tags.get_by_name(tag_name)
            task.remove_tag(actor_id, tag)
            self._uow.tasks.update(task)

    def rename_task(self, actor_id, name, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            old_name = task.name
            task.rename(actor_id, name)
            self._uow.tasks.update(task)
        msg = f'Task {old_name} was renamed to {name}.'
        self._notify_both(task, msg)

    def update_description(self, actor_id, description, task_id):
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            task.update_description(actor_id, description)
            self._uow.tasks.update(task)
        msg = f'Description of task {task.name} was updated.'
        self._notify_both(task, msg)

    def _notify_both(self, task:Task, msg:str):
        self.notification_services.send_notification(task.creator_id, msg)
        if task.creator_id != task.assignee_id:
            self.notification_services.send_notification(task.assignee_id, msg)