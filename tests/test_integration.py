"""Интеграционные тесты полного пайплайна."""

from pathlib import Path
from typing import Any

import pytest
from coffee_report.formatter import print_table
from coffee_report.loader import load_all_files
from coffee_report.reports.registry import ReportRegistry


def test_full_pipeline(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    csv_content: str = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей,2024-06-01,450,4.5,12,норм,Математика
Алексей,2024-06-02,500,4.0,14,устал,Математика
Дарья,2024-06-01,200,7.0,6,отл,Математика
"""
    csv_file: Path = tmp_path / "test.csv"
    csv_file.write_text(csv_content, encoding="utf-8")
    records = load_all_files([csv_file])
    assert len(records) == 3
    report = ReportRegistry.get("median-coffee")
    rows: list[list[Any]] = report.execute(records)

    assert len(rows) == 2
    assert rows[0][0] == "Алексей"
    assert rows[0][1] == 475

    print_table(report.columns, rows)
    captured: pytest.CaptureResult[str] = capsys.readouterr()

    assert "Алексей" in captured.out
    assert "Дарья" in captured.out
