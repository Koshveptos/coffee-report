"""Тесты для отчета MedianCoffeeReport."""

from datetime import date
from typing import Any

import pytest
from coffee_report.models import StudentRecord
from coffee_report.reports.median_coffee import MedianCoffeeReport


@pytest.fixture  # type: ignore
def sample_records() -> list[StudentRecord]:
    return [
        StudentRecord("Алексей", date(2024, 6, 1), 450, 4.5, 12, "норм", "Математика"),
        StudentRecord("Алексей", date(2024, 6, 2), 500, 4.0, 14, "устал", "Математика"),
        StudentRecord("Алексей", date(2024, 6, 3), 550, 3.5, 16, "зомби", "Математика"),
        StudentRecord("Дарья", date(2024, 6, 1), 200, 7.0, 6, "отл", "Математика"),
        StudentRecord("Дарья", date(2024, 6, 2), 250, 6.5, 8, "норм", "Математика"),
    ]


def test_median_coffee_name() -> None:
    report: MedianCoffeeReport = MedianCoffeeReport()
    assert report.name == "median-coffee"


def test_median_coffee_columns() -> None:
    report: MedianCoffeeReport = MedianCoffeeReport()
    assert report.columns == ["Студент", "Медиана трат"]


def test_median_coffee_execute(sample_records: list[StudentRecord]) -> None:
    report: MedianCoffeeReport = MedianCoffeeReport()
    result: list[list[Any]] = report.execute(sample_records)
    assert len(result) == 2
    assert result[0] == ["Алексей", 500]
    assert result[1] == ["Дарья", 225]


def test_median_coffee_sorting(sample_records: list[StudentRecord]) -> None:
    report: MedianCoffeeReport = MedianCoffeeReport()
    result: list[list[Any]] = report.execute(sample_records)
    assert result[0][1] >= result[1][1]


def test_median_coffee_empty() -> None:
    report: MedianCoffeeReport = MedianCoffeeReport()
    result: list[list[Any]] = report.execute([])
    assert result == []


def test_median_coffee_single_student() -> None:
    records: list[StudentRecord] = [
        StudentRecord("Иван", date(2024, 6, 1), 300, 5.0, 10, "норм", "Физика"),
    ]
    report: MedianCoffeeReport = MedianCoffeeReport()
    result: list[list[Any]] = report.execute(records)

    assert len(result) == 1
    assert result[0] == ["Иван", 300]


def test_median_coffee_single_record_per_student() -> None:
    records: list[StudentRecord] = [
        StudentRecord("Алексей", date(2024, 6, 1), 450, 4.5, 12, "норм", "Математика"),
        StudentRecord("Дарья", date(2024, 6, 1), 200, 7.0, 6, "отл", "Математика"),
    ]
    report: MedianCoffeeReport = MedianCoffeeReport()
    result: list[list[Any]] = report.execute(records)

    assert result[0] == ["Алексей", 450]
    assert result[1] == ["Дарья", 200]


def test_median_coffee_even_count_median() -> None:
    records: list[StudentRecord] = [
        StudentRecord("Иван", date(2024, 6, 1), 100, 5.0, 10, "норм", "Физика"),
        StudentRecord("Иван", date(2024, 6, 2), 200, 5.0, 10, "норм", "Физика"),
    ]
    report: MedianCoffeeReport = MedianCoffeeReport()
    result: list[list[Any]] = report.execute(records)

    assert result[0] == ["Иван", 150]
