from collections import defaultdict
from statistics import median
from typing import Any

from coffee_report.models import StudentRecord
from coffee_report.reports.base import BaseReport
from coffee_report.reports.registry import ReportRegistry


@ReportRegistry.register
class MedianCoffeeReport(BaseReport):
    name = "median-coffee"
    columns = ["Студент", "Медиана трат "]

    def execute(self, records: list[StudentRecord]) -> list[list[Any]]:
        spending_by_student: dict[str, list[int]] = defaultdict(list)
        for record in records:
            spending_by_student[record.student].append(record.coffee_spent)

        results: list[list[Any]] = []
        for student, spending_list in spending_by_student.items():
            median_spending = median(spending_list)
            results.append([student, median_spending])
        results.sort(key=lambda x: x[1], reverse=True)
        return results
