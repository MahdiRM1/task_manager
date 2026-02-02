class Notification:
    def __init__(self, receiver_id, message, creation_time, is_read=False):
        self.id = None
        self.receiver_id = receiver_id
        self.message = message
        self.created_at = creation_time
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True