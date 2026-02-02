from datetime import datetime

from app.core.entities.Report import Report
from app.domain.Exceptions import PermissionDenied, InvalidTargetType
from app.domain.Helper import get_by_id


class ReportingService:
    def __init__(self, task_repo, user_repo, report_repo, notification_service):
        self.task_repo = task_repo
        self.user_repo = user_repo
        self.report_repo = report_repo
        self.notification_service = notification_service

    def create_report(self, creator_id, name, description, target_id, target_type):
        creator = get_by_id(self.user_repo, creator_id)

        if target_type == 'Task':
            target = get_by_id(self.task_repo, target_id)
            report = Report(creator, name, description, target, False, datetime.now())
        elif target_type == 'User':
            target = get_by_id(self.user_repo, target_id)
            report = Report(creator, name, description, target, True, datetime.now())
        else:
            raise InvalidTargetType(target_type)

        self.report_repo.add(report)

        msg = f'Report for {target_type} with ID {target_id} was filed by user with ID {creator_id}.'
        self.notification_service.send_notification(creator, msg)

    def remove_report(self, actor_id, report_id):
        actor = get_by_id(self.user_repo, actor_id)
        report = get_by_id(self.report_repo, report_id)

        if actor.id != report.creator.id:
            raise PermissionDenied()
        self.report_repo.remove(report)

        msg = f'report with ID {report.id} was removed.'
        self.notification_service.send_notification(actor, msg)