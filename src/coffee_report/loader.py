import csv
from datetime import date, datetime
from pathlib import Path

from coffee_report.models import StudentRecord


class DataLoaderError(Exception):
    pass


class FileReadError(DataLoaderError):
    pass


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def load_csv_file(filepath: Path) -> list[StudentRecord]:
    records: list[StudentRecord] = []
    try:
        with open(filepath) as file:
            content = file.read()
            if not content.strip():
                raise FileReadError(f"Пустой файл: {filepath}")
            file.seek(0)
            reader: csv.DictReader[str] = csv.DictReader(file)
            for row_num, row in enumerate(reader, start=2):
                record = StudentRecord(
                    student=row["student"],
                    date=parse_date(row["date"]),
                    coffee_spent=int(row["coffee_spent"]),
                    sleep_hours=float(row["sleep_hours"]),
                    study_hours=int(row["study_hours"]),
                    mood=row["mood"],
                    exam=row["exam"],
                )
                records.append(record)
    except FileNotFoundError:
        raise FileReadError(f"Файл не найден: {filepath}")
    except PermissionError:
        raise FileReadError(f"Нет прав на чтение файла: {filepath}")
    except UnicodeDecodeError:
        raise FileReadError(f"Неверная кодировка файла (ожидается UTF-8): {filepath}")
    except KeyError as e:
        raise FileReadError(f"В файле {filepath} отсутствует колонка: {e}")
    except ValueError as e:
        raise FileReadError(f"Ошибка в данных файла {filepath}: {e}")

    return records


def load_all_files(filepaths: list[Path]) -> list[StudentRecord]:
    all_records = []
    for filepath in filepaths:
        records = load_csv_file(filepath)
        all_records.extend(records)
    return all_records
