from app.adapters.Exceptions import IdAlreadySet


class User:
    def __init__(self, name, id=None):
        self.name = name
        self._id = id

    def rename(self, new_name):
        self.name = new_name

    def _set_id(self, id):
        if not self._id:
            raise IdAlreadySet(f'User id "{self.name}" is already set.')
        self._id = id

    def get_id(self):
        return self._id

    def __str__(self):
        return (f'User id: {self._id}\n'
                f'name: {self.name}\n'
                )