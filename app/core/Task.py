from datetime import datetime
from enum import Enum, auto

class TaskStatus(Enum):
    TODO = auto()
    DONE = auto()

class Task:
    def __init__(self, task_creator, task_assignee, task_name, task_description):
        self.creator = task_creator
        self.assignee = task_assignee
        self.name = task_name
        self.description = task_description
        self.create_time = datetime.now()
        self.status = TaskStatus.TODO
        self.tags = set()
        self.comments = []

    def assign_to(self, assignee):
        self.assignee = assignee

    def del_tag(self, tag):
        self.tags.discard(tag)

    def add_comment(self, comment):
        self.comments.append(comment)

    def del_comment(self, comment):
        if comment in self.comments:
            self.comments.remove(comment)

    def done(self):
        self.status = TaskStatus.DONE

    def update_name(self, name):
        self.name = name

    def update_description(self, description):
        self.description = description