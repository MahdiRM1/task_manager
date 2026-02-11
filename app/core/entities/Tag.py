from app.core.Exceptions import IdAlreadySet


class Tag:
    def __init__(self, tag_name, id=None):
        self.name = tag_name
        self._id = None

    def _set_id(self, id):
        if not self._id:
            raise IdAlreadySet(f'Tag id "{self.name}" is already set.')
        self._id = id

    def get_id(self):
        return self._id

    def __str__(self):
        return f'#{self.name}'
