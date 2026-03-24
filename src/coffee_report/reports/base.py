from abc import abstractmethod
from typing import Any

from coffee_report.models import StudentRecord


class BaseReport:
    """Базовый класс для всех отчетов в случае расширения
    любой отчет построенный на данном базовом классе должен иметь обязательно -
    уникальное имя для CLI, колонки и свою реализацию расчета отчета
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def columns(self) -> list[str]:
        pass

    @abstractmethod
    def execute(self, records: list[StudentRecord]) -> list[list[Any]]:
        pass
