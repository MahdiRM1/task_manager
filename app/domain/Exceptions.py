class PermissionDenied(Exception):
    def __init__(self):
        super().__init__(f'Permission denied.')

class UserCannotRemove(Exception):
    def __init__(self, user_id):
        super().__init__(f'User "{user_id}" cannot be deleted.')

class InvalidTargetType(Exception):
    def __init__(self, target_type):
        super().__init__(f'Invalid target type "{target_type}".')