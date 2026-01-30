class Tag:
    def __init__(self, name):
        self.name = name
        self.id = None

    def __str__(self):
        return f'#{self.name}'
