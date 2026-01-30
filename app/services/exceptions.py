class UserIdNotFound(Exception):
    def __init__(self, user_id):
        super().__init__(f'User id "{user_id}" not found.')
    pass

class BoardIdNotFound(Exception):
    def __init__(self, board_id):
        super().__init__(f'Board id "{board_id}" not found.')
    pass

class TaskIdNotFound(Exception):
    def __init__(self, task_id):
        super().__init__(f'Task id "{task_id}" not found.')
    pass

class TagNameNotFound(Exception):
    def __init__(self, tag_id):
        super().__init__(f'Tag id "{tag_id}" not found.')
    pass

class InvalidTaskDeadline(Exception):
    def __init__(self, task_id):
        super().__init__(f'Task id "{task_id}" is invalid.')
    pass

class PermissionDenied(Exception):
    def __init__(self):
        super().__init__(f'Permission denied.')
    pass

class TaskAlreadyAssigned(Exception):
    def __init__(self, task_id, assignee_id):
        super().__init__(f'Task id "{task_id}" is already assigned to {assignee_id}.')
    pass

class TaskAlreadyOnBoard(Exception):
    def __init__(self, task_id, board_id):
        super().__init__(f'Task id "{task_id}" is already on board {board_id}.')
    pass