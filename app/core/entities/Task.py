from app.core.value_objects.TaskStatus import TaskStatus
from app.core.Exceptions import *

class Task:
    def __init__(self, task_creator_id, task_assignee_id, task_name,  task_description, board_id, now_time,  task_deadline, status='TODO', tags=None, id=None):
        self._id = id
        self.creator_id = task_creator_id
        self.assignee_id = task_assignee_id
        self.name = task_name
        self.description = task_description
        self.board_id = board_id
        if task_deadline <= now_time:
            raise InvalidTaskDeadline(task_deadline)
        self.created_at = now_time
        self.deadline = task_deadline
        self.status = TaskStatus.TODO if status == 'TODO' else TaskStatus.DONE
        self.tag_ids = set(tags)

    def assign_to(self, actor_id, assignee):
        if actor_id != self.creator_id:
            raise PermissionDenied()
        if assignee.id == self.assignee_id:
            raise TaskAlreadyAssigned(self._id, assignee.id)
        self.assignee_id = assignee.id

    def move_to_board(self, actor_id, new_board):
        if self.board_id == new_board.id:
            raise TaskAlreadyOnBoard(self._id, self.board_id)
        if self.creator_id == actor_id:
            raise PermissionDenied()

        self.board_id = new_board.id

    def add_tag(self, actor_id, tag):
        if not self._can_edit(actor_id):
            raise PermissionDenied()
        self.tag_ids.add(tag.id)

    def remove_tag(self, actor_id, tag):
        if not self._can_edit(actor_id):
            raise PermissionDenied()
        self.tag_ids.remove(tag.id)

    def done(self, actor_id):
        if actor_id != self.creator_id and actor_id != self.assignee_id:
            raise PermissionDenied()
        if self.status == TaskStatus.DONE:
            raise TaskAlreadyDone()
        self.status = TaskStatus.DONE

    def rename(self, actor_id, name):
        if not self._can_edit(actor_id):
            raise PermissionDenied()
        self.name = name

    def update_description(self, actor_id, description):
        if not self._can_edit(actor_id):
            raise PermissionDenied()
        self.description = description

    def _can_edit(self, actor_id):
        return self.creator_id == actor_id or self.assignee_id == actor_id

    def _set_id(self, id):
        if not self._id:
            raise IdAlreadySet(self._id)
        self._id = id

    def get_id(self):
        return self._id

    def __str__(self):
        return (f'task id: {self._id}\n'
                f'name: {self.name}\n'
                f'create_time: {self.created_at}\n'
                f'status: {self.status}\n'
                f'description: {self.description}\n'
                f'creator id: {self.creator_id}\n'
                f'assignee id: {self.assignee_id}\n'
                f'tags: {self.tag_ids}\n'
                )