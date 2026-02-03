from app.adapters.Exceptions import IdAlreadySet


class Board:
    def __init__(self, name, id = None):
        self._id = id
        self.name = name

    def _set_id(self, id):
        if not self._id:
            raise IdAlreadySet(f'Board id "{self.name}" is already set.')
        self._id = id

    def get_id(self):
        return self._id