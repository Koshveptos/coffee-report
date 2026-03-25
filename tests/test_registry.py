from typing import Any

import pytest
from coffee_report.models import StudentRecord
from coffee_report.reports.base import BaseReport
from coffee_report.reports.registry import ReportRegistry


class TestReport(BaseReport):  # type: ignore[misc]
    name = "test-report"
    columns = ["Test"]

    def execute(self, records: list[StudentRecord]) -> list[list[Any]]:
        return []


def test_registry_list_available() -> None:
    available: list[str] = ReportRegistry.list_available()
    assert "median-coffee" in available


def test_registry_get_valid() -> None:
    report: BaseReport = ReportRegistry.get("median-coffee")
    assert report.name == "median-coffee"


def test_registry_get_invalid() -> None:
    with pytest.raises(ValueError, match="не найден"):
        ReportRegistry.get("nonexistent-report")


def test_registry_register_returns_class() -> None:
    result: type[BaseReport] = ReportRegistry.register(TestReport)
    assert result == TestReport
