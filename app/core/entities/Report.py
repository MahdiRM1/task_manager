class Report:
    def __init__(self, creator, report_name, report_description, target, target_is_user, now_time):
        self.id = None
        self.creator_id = creator.id
        self.name = report_name
        self.description = report_description
        self.target_user_id = target.id if target_is_user else None
        self.target_task_id = None if target.id else target.id
        self.created_at = now_time

    def __str__(self):
        return (f"report id: {self.id}\n"
                f"creator id: {self.creator_id}\n"
                f"created_at: {self.created_at}\n"
                f"name: {self.name}\n"
                f"description: {self.description}"
                )