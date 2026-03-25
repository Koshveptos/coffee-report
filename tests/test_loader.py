from datetime import date
from pathlib import Path

import pytest
from coffee_report.loader import FileReadError, load_all_files, load_csv_file, parse_date
from coffee_report.models import StudentRecord


def test_parse_date_valid() -> None:
    result: date = parse_date("2024-06-01")
    assert result == date(2024, 6, 1)


def test_parse_date_end_of_year() -> None:
    result: date = parse_date("2024-12-31")
    assert result == date(2024, 12, 31)


def test_parse_date_invalid_format() -> None:
    with pytest.raises(ValueError):
        parse_date("01-06-2024")


def test_parse_date_empty_string() -> None:
    with pytest.raises(ValueError):
        parse_date("")


def test_load_csv_file_valid(tmp_path: Path) -> None:
    csv_content: str = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей,2024-06-01,450,4.5,12,норм,Математика
Дарья,2024-06-02,200,7.0,6,отл,Математика
"""
    csv_file: Path = tmp_path / "test.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    records: list[StudentRecord] = load_csv_file(csv_file)

    assert len(records) == 2
    assert records[0].student == "Алексей"
    assert records[0].coffee_spent == 450
    assert records[1].student == "Дарья"
    assert records[1].coffee_spent == 200


def test_load_csv_file_not_found() -> None:
    with pytest.raises(FileReadError, match="Файл не найден"):
        load_csv_file(Path("nonexistent.csv"))


def test_load_csv_file_empty(tmp_path: Path) -> None:
    csv_file: Path = tmp_path / "empty.csv"
    csv_file.write_text("", encoding="utf-8")

    with pytest.raises(FileReadError, match="Пустой файл"):
        load_csv_file(csv_file)


def test_load_csv_file_missing_column(tmp_path: Path) -> None:
    csv_content: str = """student,date,coffee_spent
Алексей,2024-06-01,450
"""
    csv_file: Path = tmp_path / "missing.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    with pytest.raises(FileReadError, match="отсутствует колонка"):
        load_csv_file(csv_file)


def test_load_csv_file_invalid_data(tmp_path: Path) -> None:
    csv_content: str = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей,2024-06-01,abc,4.5,12,норм,Математика
"""
    csv_file: Path = tmp_path / "invalid.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    with pytest.raises(FileReadError, match="Ошибка в данных"):
        load_csv_file(csv_file)


def test_load_all_files_single(tmp_path: Path) -> None:
    csv_content: str = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей,2024-06-01,450,4.5,12,норм,Математика
"""
    csv_file: Path = tmp_path / "test.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    records: list[StudentRecord] = load_all_files([csv_file])
    assert len(records) == 1


def test_load_all_files_multiple(tmp_path: Path) -> None:
    csv_content1: str = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей,2024-06-01,450,4.5,12,норм,Математика
"""
    csv_content2: str = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Дарья,2024-06-01,200,7.0,6,отл,Математика
"""
    file1: Path = tmp_path / "test1.csv"
    file2: Path = tmp_path / "test2.csv"
    file1.write_text(csv_content1, encoding="utf-8")
    file2.write_text(csv_content2, encoding="utf-8")

    records: list[StudentRecord] = load_all_files([file1, file2])
    assert len(records) == 2


def test_load_all_files_empty_list() -> None:
    records: list[StudentRecord] = load_all_files([])
    assert records == []
