from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class StudentRecord:
    student: str
    date: date
    coffee_spent: int
    sleep_hours: float
    study_hours: int
    mood: str
    exam: str
