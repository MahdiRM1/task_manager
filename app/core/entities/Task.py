from app.core.value_objects.TaskStatus import TaskStatus
from app.core.exceptions import *

class Task:
    def __init__(self, task_creator_id, task_assignee_id, task_name,  task_description, board_id, now_time,  task_deadline):
        self.id = None
        self.creator_id = task_creator_id
        self.assignee_id = task_assignee_id
        self.name = task_name
        self.description = task_description
        self.board_id = board_id
        self.deadline = task_deadline
        self.created_at = now_time
        self.status = TaskStatus.TODO
        self.tags = set()

    def assign_to(self, assignee):
        self.assignee = assignee

    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

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
        return self.creator.id == actor.id or self.assignee.id == actor.id

    def is_creator(self, actor):
        return self.creator.id == actor.id

    def is_assignee(self, actor):
        return self.assignee.id == actor.id

    def __str__(self):
        return (f'task id: {self.id}\n'
                f'name: {self.name}\n'
                f'create_time: {self.created_at}\n'
                f'status: {self.status}\n'
                f'description: {self.description}\n'
                f'creator: {self.creator}\n'
                f'assignee: {self.assignee}\n'
                f'tags: {self.tags}\n'
                )