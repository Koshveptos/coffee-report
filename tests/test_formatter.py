"""Тесты для модуля formatter.py."""

from typing import Any

import pytest
from coffee_report.formatter import print_table


def test_print_table_basic(capsys: pytest.CaptureFixture[str]) -> None:
    columns: list[str] = ["Имя", "Значение"]
    rows: list[list[Any]] = [
        ["Алексей", 500],
        ["Дарья", 200],
    ]

    print_table(columns, rows)
    captured: pytest.CaptureResult[str] = capsys.readouterr()

    assert "Алексей" in captured.out
    assert "Дарья" in captured.out
    assert "500" in captured.out


def test_print_table_empty(capsys: pytest.CaptureFixture[str]) -> None:
    columns: list[str] = ["Имя", "Значение"]
    rows: list[list[Any]] = []

    print_table(columns, rows)
    captured: pytest.CaptureResult[str] = capsys.readouterr()

    assert "Имя" in captured.out
    assert "Значение" in captured.out


def test_print_table_single_row(capsys: pytest.CaptureFixture[str]) -> None:
    columns: list[str] = ["Имя", "Значение"]
    rows: list[list[Any]] = [["Иван", 300]]

    print_table(columns, rows)
    captured: pytest.CaptureResult[str] = capsys.readouterr()

    assert "Иван" in captured.out
    assert "300" in captured.out
