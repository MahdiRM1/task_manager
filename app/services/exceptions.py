class UserIdNotFound(Exception):
    def __init__(self, user_id):
        super().__init__(f'User id "{user_id}" not found.')

class BoardIdNotFound(Exception):
    def __init__(self, board_id):
        super().__init__(f'Board id "{board_id}" not found.')

class TaskIdNotFound(Exception):
    def __init__(self, task_id):
        super().__init__(f'Task id "{task_id}" not found.')

class NotificationIdNotFound(Exception):
    def __init__(self, notification_id):
        super().__init__(f'Notification id "{notification_id}" not found.')

class ReportIdNotFound(Exception):
    def __init__(self, report_id):
        super().__init__(f'Report id "{report_id}" not found.')

class TagNameNotFound(Exception):
    def __init__(self, tag_id):
        super().__init__(f'Tag id "{tag_id}" not found.')

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