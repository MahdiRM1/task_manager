from abc import ABC, abstractmethod

from app.core.entities.Report import Report


class ReportRepository(ABC):

    @abstractmethod
    def add(self, report: Report) -> None:
        pass

    @abstractmethod
    def remove(self, report: Report) -> None:
        pass

    @abstractmethod
    def get_by_id(self, report_id: int) -> Report | None:
        pass