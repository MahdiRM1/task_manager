from app.adapters.models.ReportModel import ReportModel
from app.core.entities.Report import Report


class ReportMapper:
    @staticmethod
    def to_entity(model: ReportModel) -> Report:
        return Report(
            model.creator_id,
            model.name,
            model.description,
            model.target_user_id,
            model.target_task_id,
            model.created_at,
            model.id
        )

    @staticmethod
    def to_model(report: Report) -> ReportModel:
        return ReportModel(
            creator_id=report.creator_id,
            name=report.name,
            description=report.description,
            target_user_id=report.target_user_id,
            target_task_id=report.target_task_id,
            created_at=report.created_at
        )