class TaskAlreadyDone(Exception):
    def __init__(self):
        super().__init__("task already done")