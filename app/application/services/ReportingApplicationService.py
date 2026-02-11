from datetime import datetime

from app.core.entities.Report import Report
from app.domain.Exceptions import PermissionDenied, InvalidTargetType


class ReportingApplicationService:
    def __init__(self, uow, notification_service):
        self._uow = uow
        self.notification_service = notification_service

    def create_report(self, creator_id, name, description, target_id, target_type):
        with self._uow:
            creator = self._uow.users.get_by_id(creator_id)
            if target_type == 'Task':
                report = Report(creator_id, name, description, None, target_id, datetime.now())
            elif target_type == 'User':
                report = Report(creator_id, name, description, target_id, None, datetime.now())
            else:
                raise InvalidTargetType(target_type)
            self._uow.reports.add(report)

        msg = f'Report for {target_type} with ID {target_id} was filed by user with ID {creator_id}.'
        self.notification_service.send_notification(creator.id, msg)

    def remove_report(self, actor_id, report_id):
        with self._uow:
            report = self._uow.reports.get_by_id(report_id)
            if actor_id != report.creator.id:
                raise PermissionDenied()
            self._uow.reports.remove(report)

        msg = f'report with ID {report.id} was removed.'
        self.notification_service.send_notification(actor_id, msg)