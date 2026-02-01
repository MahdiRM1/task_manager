from datetime import datetime

from app.core.entities.Tag import Tag
from app.core.entities.Task import Task
from app.services.Helper import *


class TaskService:
    def __init__(self, task_repo, user_repo, board_repo, tag_repo, notification_services):
        self.task_repo = task_repo
        self.user_repo = user_repo
        self.board_repo = board_repo
        self.tag_repo = tag_repo
        self.notification_services = notification_services

    def add_task(self, creator_id, assignee_id, name, description,  board_id, deadline):
        creator = get_by_id(self.user_repo, creator_id)
        assignee = get_by_id(self.user_repo, assignee_id)
        board = get_by_id(self.board_repo, board_id)

        now = datetime.now()
        if deadline <= now:
            raise InvalidTaskDeadline(deadline)

        task = Task(creator, assignee, name, description, board, now, deadline)
        self.task_repo.add(task)

        msg = (f'Task {task.name} with ID {task.id} was added.\n'
               f'creator: {creator.name}\n'
               f'assignee: {assignee.name}')
        self.notification_services.send_notification(creator, msg)
        if creator_id != assignee_id:
            self.notification_services.send_notification(assignee, msg)

    def remove_task(self, actor_id, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)

        if not task.is_creator(actor):
            raise PermissionDenied()

        self.task_repo.remove(task)

        msg = f'Task {task.name} with ID {task.id} was removed.\n'
        self._notify_both(task, msg)

    def task_done(self, actor_id, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)

        if not task.is_assignee(actor):
            raise PermissionDenied()

        task.done()
        self.task_repo.update(task)

        msg = f'Task {task.name} with ID {task.id} is Done.'
        self._notify_both(task, msg)

    def assign_task(self, actor_id, assignee_id, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)
        assignee = get_by_id(self.user_repo, assignee_id)

        if not task.is_creator(actor):
            raise PermissionDenied()

        old_assignee = task.assignee
        if old_assignee.id == assignee.id:
            raise TaskAlreadyAssigned(task_id, assignee.id)

        task.assign_to(assignee)
        self.task_repo.update(task)

        msg = f'Task {task.name} with ID {task.id} was assigned to User ID {assignee.id}.'
        self._notify_both(task, msg)
        if old_assignee.id != task.creator.id:
            self.notification_services.send_notification(old_assignee, msg)

    def move_task(self, actor_id, board_id, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)
        board = get_by_id(self.board_repo, board_id)

        if task.board_id == board.id:
            raise TaskAlreadyOnBoard(task.id, board.id)

        if not task.is_creator(actor):
            raise PermissionDenied()

        task.move_to(board)
        self.task_repo.update(task)

        msg = f'task {task.name} with ID {task.id} was moved to Board {board.name}.'

        self._notify_both(task, msg)

    def add_tag_to_task(self, actor_id, tag_name, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        tag = self.tag_repo.get_by_name(tag_name)
        if tag is None:
            tag = Tag(tag_name)
            self.tag_repo.add(tag)

        task.add_tag(tag)
        self.task_repo.update(task)

    def remove_tag_task(self, actor_id, tag_name, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        tag = get_by_name(self.tag_repo, tag_name)

        task.remove_tag(tag)
        self.task_repo.update(task)

    def rename_task(self, actor_id, name, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        old_name = task.name

        task.rename(name)
        self.task_repo.update(task)

        msg = f'Task {old_name} was renamed to {name}.'
        self._notify_both(task, msg)

    def update_description(self, actor_id, description, task_id):
        actor = get_by_id(self.user_repo, actor_id)
        task = get_by_id(self.task_repo, task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        task.update_description(description)
        self.task_repo.update(task)

        msg = f'Description of task {task.name} was updated.'
        self._notify_both(task, msg)

    def _notify_both(self, task, msg):
        self.notification_services.send_notification(task.creator, msg)
        if task.creator.id != task.assignee.id:
            self.notification_services.send_notification(task.assignee, msg)