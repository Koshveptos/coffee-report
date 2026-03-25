from coffee_report.reports.base import BaseReport


class ReportRegistry:
    """
    Реестр доступных отчетов
    """

    _reports: dict[str, type[BaseReport]] = {}

    @classmethod
    def register(cls, report_class: type[BaseReport]) -> type[BaseReport]:
        # декоратор для регистрации отчета
        cls._reports[report_class.name] = report_class
        return report_class

    @classmethod
    def get(cls, name: str) -> BaseReport:
        # создает и возвращяет экземпляр  по имени
        if name not in cls._reports:
            available = " ".join(sorted(cls._reports.keys()))
            raise ValueError(f"Отчет '{name}' не найден. Доступные: {available}")
        return cls._reports[name]()

    @classmethod
    def list_available(cls) -> list[str]:
        # список доступных
        return sorted(cls._reports.keys())
