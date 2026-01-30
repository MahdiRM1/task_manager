class Notification:
    def __init__(self, receiver, message, time):
        self.id = None
        self.receiver = receiver
        self.message = message
        self.time = time
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True