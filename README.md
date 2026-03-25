# Coffee Report

Скрипт для генерации отчётов по данным о подготовке студентов к экзаменам.
Анализирует CSV-файлы с информацией о тратах на кофе, сне и часах учёбы.

## Быстрый старт

```bash
uv sync
uv run coffee-report --files <файлы.csv> --report <название_отчёта>
```

Примеры использования
```
uv run coffee-report --files data/session.csv --report median-coffee
```

Пример работы с корректными данными

для одного файла
![Описание картинки](coffee-report\img\god_example.png)


для нескольких
![Описание картинки](img\example_one.png)

Пример работы для не верных файлов\параметров
![Описание картинки](img\bad_examples.png)



Так же было проведено тестирование, покрытие
![Описание картинки](img\test_cover.png)


Архитектура проекта


```
src/coffee_report/
├── main.py              # Точка входа (CLI entry point)
├── cli.py               # Парсинг аргументов и валидация
├── loader.py            # Чтение и парсинг CSV файлов
├── models.py            # Модели данных (StudentRecord)
├── formatter.py         # Форматирование вывода (tabulate)
└── reports/
    ├── base.py          # Абстрактный базовый класс отчёта
    ├── registry.py      # Реестр доступных отчётов (Strategy pattern)
    └── median_coffee.py # Конкретная реализация отчёта
```

Данная архитектура разработа для удобного добавления новых вариаций отчетов, для этого нужно

Создать класс наследуемый от BaseReport

Реализовать name, columns, execute()

Зарегистрировать через @ReportRegistry.register
