import csv
from datetime import date, datetime
from pathlib import Path

from coffee_report.models import StudentRecord


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def load_csv_file(filepath: Path) -> list[StudentRecord]:
    records: list[StudentRecord] = []
    with open(filepath) as file:
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
    return records


def load_all_files(filepaths: list[Path]) -> list[StudentRecord]:
    all_records = []
    for filepath in filepaths:
        records = load_csv_file(filepath)
        all_records.extend(records)
    return all_records
