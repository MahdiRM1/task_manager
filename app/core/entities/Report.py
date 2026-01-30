class Report:
    def __init__(self, report_name, report_description, now_time):
        self.name = report_name
        self.description = report_description
        self.id = None
        self.created_at = now_time

    def __str__(self):
        return (f"report id: {self.id}\n"
                f"created_at: {self.created_at}"
                f"name: {self.name}\n"
                f"description: {self.description}"
                )