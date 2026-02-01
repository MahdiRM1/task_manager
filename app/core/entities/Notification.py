class Notification:
    def __init__(self, receiver_id, message, creation_time):
        self.id = None
        self.receiver_id = receiver_id
        self.message = message
        self.created_at = creation_time
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True