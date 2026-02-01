from app.core.value_objects.TaskStatus import TaskStatus
from app.core.exceptions import *

class Task:
    def __init__(self, task_creator, task_assignee, task_name,  task_description, board, now_time,  task_deadline):
        self.id = None
        self.creator_id = task_creator.id
        self.assignee_id = task_assignee.id
        self.name = task_name
        self.description = task_description
        self.board_id = board.id
        self.created_at = now_time
        self.deadline = task_deadline
        self.status = TaskStatus.TODO
        self.tag_ids = set()

    def assign_to(self, assignee):
        self.assignee_id = assignee.id

    def add_tag(self, tag):
        self.tag_ids.add(tag.id)

    def remove_tag(self, tag):
        self.tag_ids.remove(tag.Id)

    def move_to_board(self, new_board_id):
        self.board_id = new_board_id

    def done(self):
        if self.status == TaskStatus.DONE:
            raise TaskAlreadyDone()
        self.status = TaskStatus.DONE

    def rename(self, name):
        self.name = name

    def update_description(self, description):
        self.description = description

    def can_edit(self, actor):
        return self.creator_id == actor.id or self.assignee_id == actor.id

    def is_creator(self, actor):
        return self.creator_id == actor.id

    def is_assignee(self, actor):
        return self.assignee_id == actor.id

    def __str__(self):
        return (f'task id: {self.id}\n'
                f'name: {self.name}\n'
                f'create_time: {self.created_at}\n'
                f'status: {self.status}\n'
                f'description: {self.description}\n'
                f'creator id: {self.creator_id}\n'
                f'assignee id: {self.assignee_id}\n'
                f'tags: {self.tag_ids}\n'
                )