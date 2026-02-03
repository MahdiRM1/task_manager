from datetime import datetime

from app.core.entities.Report import Report
from app.domain.Exceptions import PermissionDenied, InvalidTargetType


class ReportingService:
    def __init__(self, task_repo, user_repo, report_repo, notification_service):
        self.task_repo = task_repo
        self.user_repo = user_repo
        self.report_repo = report_repo
        self.notification_service = notification_service

    def create_report(self, creator_id, name, description, target_id, target_type):
        creator = self.report_repo.get_by_id(creator_id)

        if target_type == 'Task':
            report = Report(creator_id, name, description, None, target_id, datetime.now())
        elif target_type == 'User':
            report = Report(creator_id, name, description, target_id, None, datetime.now())
        else:
            raise InvalidTargetType(target_type)

        self.report_repo.add(report)

        msg = f'Report for {target_type} with ID {target_id} was filed by user with ID {creator_id}.'
        self.notification_service.send_notification(creator.id, msg)

    def remove_report(self, actor_id, report_id):
        report = self.report_repo.get_by_id(report_id)

        if actor_id != report.creator.id:
            raise PermissionDenied()
        self.report_repo.remove(report)

        msg = f'report with ID {report.id} was removed.'
        self.notification_service.send_notification(actor_id, msg)