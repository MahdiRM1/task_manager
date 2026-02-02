class Report:
    def __init__(self, creator_id, report_name, report_description, target_user_id, target_task_id, now_time):
        self.id = None
        self.creator_id = creator_id
        self.name = report_name
        self.description = report_description
        self.target_user_id = target_user_id
        self.target_task_id = target_task_id
        self.created_at = now_time

    def __str__(self):
        return (f"report id: {self.id}\n"
                f"creator id: {self.creator_id}\n"
                f"created_at: {self.created_at}\n"
                f"name: {self.name}\n"
                f"description: {self.description}"
                )