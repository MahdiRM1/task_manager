class InvalidName(Exception):
    def __init__(self):
        super().__init__("name is invalid")

class TaskAlreadyDone(Exception):
    def __init__(self):
        super().__init__("task already done")

class PermissionDenied(Exception):
    def __init__(self):
        super().__init__(f'Permission denied.')

class InvalidTaskDeadline(Exception):
    def __init__(self, task_id):
        super().__init__(f'Task id "{task_id}" is invalid.')


class TaskAlreadyAssigned(Exception):
    def __init__(self, task_id, assignee_id):
        super().__init__(f'Task id "{task_id}" is already assigned to {assignee_id}.')

class TaskAlreadyOnBoard(Exception):
    def __init__(self, task_id, board_id):
        super().__init__(f'Task id "{task_id}" is already on board {board_id}.')

class IdAlreadySet(Exception):
    def __init__(self, id):
        super().__init__(f'Id "{id}" is already set.')
