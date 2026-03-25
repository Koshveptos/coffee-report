import sys

from coffee_report.cli import parse_args, validate_files, validate_report
from coffee_report.formatter import print_table
from coffee_report.loader import load_all_files
from coffee_report.reports.registry import ReportRegistry


def cli() -> None:
    try:
        args = parse_args()
        validate_files(args.files)
        validate_report(args.report)

        records = load_all_files(args.files)

        report = ReportRegistry.get(args.report)
        rows = report.execute(records)
        print_table(report.columns, rows)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    cli()
