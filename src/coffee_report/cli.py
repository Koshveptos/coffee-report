import argparse
from pathlib import Path

from coffee_report.reports.registry import ReportRegistry


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", type=Path, required=True)
    parser.add_argument("--report", type=str, required=True)
    return parser.parse_args()


def validate_files(filepaths: list[Path]) -> None:
    for filepath in filepaths:
        if not filepath.exists():
            raise FileNotFoundError(f"Файл не найден {filepath}")


def validate_report(report_name: str) -> None:
    available = ReportRegistry.list_available()
    if report_name not in available:
        raise ValueError(f"Отчет '{report_name}' не найден. Доступные: {', '.join(available)}")
