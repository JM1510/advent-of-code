import argparse
import sys

from datetime import datetime, timedelta, timezone
from importlib import import_module


def run(func, filename="filename"):
    try:
        with open(filename) as f:
            content = f.read()
            lines = [line for line in content.split("\n") if line]
            try:
                print(func(lines, content))
            except Exception as e:
                print(f"Error: {e}")
    except FileNotFoundError:
        print("No file provided")


if __name__ == "__main__":
    now = datetime.now(timezone(-timedelta(hours=5)))

    # Add year and day to arguments to allow running solutions from different
    # days
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--year", type=int, help="Year to run", default=now.year
    )
    argument_parser.add_argument(
        "--day", type=int, help="Day to run", default=now.day
    )
    args = argument_parser.parse_args()

    input_path = f"input/{args.year}/day{args.day:02}.txt"
    solution_module = f"solutions.{args.year}.day{args.day:02}"

    try:
        module = import_module(solution_module)
    except ModuleNotFoundError:
        print("The solution hasn't been written yet")
        sys.exit()

    print(f"Day {args.day:02}")
    for part in ("part_one", "part_two"):
        print(f"{part}:")
        run(getattr(module, part), input_path)
