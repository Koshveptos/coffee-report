from abc import ABC, abstractmethod
from typing import Any

from coffee_report.models import StudentRecord


class BaseReport(ABC):
    """Базовый класс для всех отчетов в случае расширения
    любой отчет построенный на данном базовом классе должен иметь обязательно -
    уникальное имя для CLI, колонки и свою реализацию расчета отчета
    """

    name: str
    columns: list[str]

    @abstractmethod
    def execute(self, records: list[StudentRecord]) -> list[list[Any]]:
        pass
