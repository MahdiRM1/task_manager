class IdNotFound(Exception):
    def __init__(self, entity_type, entity_id):
        super().__init__(f'"{entity_type} id "{entity_id}" not found.')

class NameNotFound(Exception):
    def __init__(self, entity_type, entity_name):
        super().__init__(f'{entity_type} id "{id}" not found.')

class InvalidTaskDeadline(Exception):
    def __init__(self, task_id):
        super().__init__(f'Task id "{task_id}" is invalid.')

class PermissionDenied(Exception):
    def __init__(self):
        super().__init__(f'Permission denied.')

class TaskAlreadyAssigned(Exception):
    def __init__(self, task_id, assignee_id):
        super().__init__(f'Task id "{task_id}" is already assigned to {assignee_id}.')

class TaskAlreadyOnBoard(Exception):
    def __init__(self, task_id, board_id):
        super().__init__(f'Task id "{task_id}" is already on board {board_id}.')

class UserCannotRemove(Exception):
    def __init__(self, user_id):
        super().__init__(f'User "{user_id}" cannot be deleted.')

class InvalidTargetType(Exception):
    def __init__(self, target_type):
        super().__init__(f'Invalid target type "{target_type}".')