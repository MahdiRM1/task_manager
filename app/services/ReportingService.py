from datetime import datetime

from app.core.entities.Report import Report
from app.services.exceptions import PermissionDenied, InvalidTargetType


class ReportingService:
    def __init__(self, report_repo, notification_service, loader):
        self.report_repo = report_repo
        self.notification_service = notification_service
        self.loader = loader

    def create_report(self, creator_id, name, description, target_id, target_type):
        creator = self.loader.get_user(creator_id)

        if target_type == 'Task':
            target = self.loader.get_task(target_id)
        elif target_type == 'User':
            target = self.loader.get_user(target_id)
        else:
            raise InvalidTargetType(target_type)

        report = Report(creator, name, description, target, datetime.now())
        self.report_repo.add(report)

        msg = f'Report for {target_type} with ID {target_id} was filed by user with ID {creator_id}.'
        self.notification_service.send(creator, msg)

    def remove_report(self, actor_id, report_id):
        actor = self.loader.get_user(actor_id)
        report = self.loader.get_report(report_id)

        if actor.id != report.creator.id:
            raise PermissionDenied()
        self.report_repo.remove(report)

        msg = f'report with ID {report.id} was removed.'
        self.notification_service.send(actor, msg)