from pathlib import Path

import pytest
from coffee_report.cli import validate_files, validate_report


def test_validate_files_valid(tmp_path: Path) -> None:
    file1: Path = tmp_path / "file1.csv"
    file1.write_text("test", encoding="utf-8")
    validate_files([file1])


def test_validate_files_multiple_valid(tmp_path: Path) -> None:
    file1: Path = tmp_path / "file1.csv"
    file2: Path = tmp_path / "file2.csv"
    file1.write_text("test", encoding="utf-8")
    file2.write_text("test", encoding="utf-8")
    validate_files([file1, file2])


def test_validate_files_not_found(tmp_path: Path) -> None:
    nonexistent: Path = tmp_path / "nonexistent.csv"
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        validate_files([nonexistent])


def test_validate_files_mixed(tmp_path: Path) -> None:
    file1: Path = tmp_path / "file1.csv"
    file1.write_text("test", encoding="utf-8")
    nonexistent: Path = tmp_path / "nonexistent.csv"
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        validate_files([file1, nonexistent])


def test_validate_report_valid() -> None:
    validate_report("median-coffee")


def test_validate_report_invalid() -> None:
    with pytest.raises(ValueError, match="не найден"):
        validate_report("nonexistent-report")


def test_validate_report_empty_string() -> None:
    with pytest.raises(ValueError, match="не найден"):
        validate_report("")
