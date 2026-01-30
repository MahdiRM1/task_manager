class User:
    def __init__(self, name):
        self.name = name
        self.id = None

    def rename(self, new_name):
        self.name = new_name

    def __str__(self):
        return (f'User id: {self.id}\n'
                f'name: {self.name}\n'
                )