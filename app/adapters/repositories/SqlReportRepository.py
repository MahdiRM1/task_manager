from sqlalchemy.orm import Session

from app.adapters.Exceptions import IdNotFound
from app.adapters.mappers.ReportMapper import ReportMapper
from app.adapters.models.ReportModel import ReportModel
from app.core.entities.Report import Report
from app.domain.repositories.ReportRepository import ReportRepository


class SqlReportRepository(ReportRepository):
    def __init__(self, session : Session):
        self.session = session

    def add(self, report: Report) -> None:
        model = ReportMapper.to_model(report)
        self.session.add(model)
        self.session.flush()
        report._set_id(model.id)

    def remove(self, report: Report) -> None:
        model = self.session.get(ReportModel, report.id)
        if model:
            self.session.delete(model)

    def get_by_id(self, report_id: int) -> Report:
        model = self.session.get(ReportModel, report_id)

        if not model:
            raise IdNotFound(f'Report id {report_id} not found.')

        report = ReportMapper.to_entity(model)
        return report