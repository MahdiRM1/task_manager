from app.core.Exceptions import IdAlreadySet


class Notification:
    def __init__(self, receiver_id, message, creation_time, is_read=False, id=None):
        self._id = id
        self.receiver_id = receiver_id
        self.message = message
        self.created_at = creation_time
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def _set_id(self, id):
        if not self._id:
            raise IdAlreadySet(f'Notification id is already set.')
        self._id = id

    def get_id(self):
        return self._id