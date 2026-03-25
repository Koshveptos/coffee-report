from typing import Any

from tabulate import tabulate  # type: ignore[import-untyped]


def print_table(columns: list[str], rows: list[list[Any]]) -> None:
    print(tabulate(rows, headers=columns, tablefmt="grid"))
