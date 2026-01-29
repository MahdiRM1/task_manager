from datetime import datetime

class Comment:
    def __init__(self, author, comment):
        self.author = author
        self.comment = comment
        self.create_time = datetime.now()
        self.id = None

    def __eq__(self, other):
        return self.id == other.id