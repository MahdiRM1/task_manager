class Report:
    def __init__(self, creator, report_name, report_description, target, now_time):
        self.id = None
        self.creator = creator
        self.name = report_name
        self.description = report_description
        self.target_id = target.id
        self.target_type = target.__class__.__name__
        self.created_at = now_time

    def __str__(self):
        return (f"report id: {self.id}\n"
                f"creator: {self.creator.name}\n"
                f"created_at: {self.created_at}\n"
                f"name: {self.name}\n"
                f"description: {self.description}"
                )