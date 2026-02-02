from sqlalchemy.orm import Session

from app.adapters.Models.ReportModel import ReportModel
from app.core.entities.Report import Report
from app.domain.repositories.ReportRepository import ReportRepository


class SqlReportRepository(ReportRepository):
    def __init__(self, session : Session):
        self.session = session

    def add(self, report: Report) -> None:
        report_model = ReportModel(
            creator_id=report.creator_id,
            name=report.name,
            description=report.description,
            target_user_id=report.target_user_id,
            target_task_id=report.target_task_id,
            created_at=report.created_at
        )
        self.session.add(report_model)
        self.session.flush()
        self.session.commit()
        report.id = report_model.id

    def remove(self, report: Report) -> None:
        report_model = self.session.get(ReportModel, report.id)
        if report_model:
            self.session.delete(report_model)
            self.session.commit()

    def get_by_id(self, report_id: int) -> Report | None:
        report_model = self.session.get(ReportModel, report_id)

        if not report_model:
            return None

        report = Report(
            report_model.creator_id,
            report_model.name,
            report_model.description,
            report_model.target_user_id,
            report_model.target_task_id,
            report_model.created_at
        )
        report.id = report_model.id
        return report