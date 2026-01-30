from datetime import datetime

from app.core.entities.Tag import Tag
from app.core.entities.Task import Task
from app.services.exceptions import *

class TaskServices:
    def __init__(self, task_repo, board_repo, tag_repo, user_repo, notification_services):
        self.task_repo = task_repo
        self.board_repo = board_repo
        self.tag_repo = tag_repo
        self.user_repo = user_repo
        self.notification_services = notification_services

    def add_task(self, creator_id, assignee_id, name, description,  board_id, deadline):
        creator = self._get_user(creator_id)
        assignee = self._get_user(assignee_id)
        board = self._get_board(board_id)

        now = datetime.now()
        if deadline <= now:
            raise InvalidTaskDeadline(deadline)

        task = Task(creator, assignee, name, description, board, now, deadline)
        self.task_repo.add(task)

        msg = (f'Task {task.name} with ID {task.id} was added.\n'
               f'creator: {creator.name}\n'
               f'assignee: {assignee.name}')
        self.notification_services.send(creator, msg)
        if creator_id != assignee_id:
            self.notification_services.send(assignee, msg)

    def remove_task(self, actor_id, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)

        if not task.is_creator(actor):
            raise PermissionDenied()

        self.task_repo.remove_by_id(task_id)

        msg = f'Task {task.name} with ID {task.id} was removed.\n'
        self._notify_both(task, msg)

    def task_done(self, actor_id, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)

        if not task.is_assignee(actor):
            raise PermissionDenied()

        task.done()

        msg = f'Task {task.name} with ID {task.id} is Done.'
        self._notify_both(task, msg)

    def assign_task(self, actor_id, assignee_id, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)
        assignee = self._get_user(assignee_id)

        if not task.is_creator(actor):
            raise PermissionDenied()

        old_assignee = task.assignee
        if old_assignee.id == assignee.id:
            raise TaskAlreadyAssigned(task_id, assignee.id)

        task.assign_to(assignee)

        msg = f'Task {task.name} with ID {task.id} was assigned to User ID {assignee.id}.'
        self._notify_both(task, msg)

    def move_task(self, actor_id, board_id, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)
        board = self._get_board(board_id)

        if task.board.id == board.id:
            raise TaskAlreadyOnBoard(task_id, board.id)

        if not task.is_creator(actor):
            raise PermissionDenied()

        task.move_to(board)

        msg = f'task {task.name} with ID {task.id} was moved to Board {board.name}.'

        self._notify_both(task, msg)

    def tag_task(self, actor_id, tag_name, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        tag = self.tag_repo.get_by_name(tag_name)
        if tag is None:
            tag = Tag(tag_name)
            self.tag_repo.create(tag)

        task.add_tag(tag)

    def remove_tag_task(self, actor_id, tag_name, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        tag = self.tag_repo.get_by_name(tag_name)
        if tag is None:
            raise TagNameNotFound(tag_name)

        task.remove_tag(tag)

    def rename_task(self, actor_id, name, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        old_name = task.name

        task.rename(name)

        msg = f'Task {old_name} was renamed to {name}.'
        self._notify_both(task, msg)

    def update_description(self, actor_id, description, task_id):
        actor = self._get_user(actor_id)
        task = self._get_task(task_id)

        if not task.can_edit(actor):
            raise PermissionDenied()

        task.update_description(description)

        msg = f'Description of task {task.name} was updated.'
        self._notify_both(task, msg)

    def _get_user(self, user_id):
        actor = self.user_repo.get_by_id(user_id)
        if actor is None:
            raise UserIdNotFound(user_id)
        return actor

    def _get_task(self, task_id):
        task = self.task_repo.get_by_id(task_id)
        if task is None:
            raise TaskIdNotFound(task_id)
        return task

    def _get_board(self, board_id):
        board = self.board_repo.get_by_id(board_id)
        if board is None:
            raise BoardIdNotFound(board_id)
        return board

    def _notify_both(self, task, msg):
        self.notification_services.send(task.creator, msg)
        if task.creator.id != task.assignee.id:
            self.notification_services.send(task.assignee, msg)