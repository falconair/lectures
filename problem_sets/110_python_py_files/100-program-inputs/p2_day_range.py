"""
PROBLEM 2
Practises: reading command-line arguments with argparse.

Task: fill in the function parse_args.

To check your work, type:
    python p2_day_range.py TSLA 2025-09-10

It should print the ticker and the day that parse_args returned, then that day's high minus its low:
    TSLA 2025-09-10 range 10.26
"""

import argparse
import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Read a ticker and a day from the command line, using argparse.

    Both are required. Give each one a help text, so that --help explains it.

    Args:
        argv: what the user typed after the program's name, as a list of text.

    Returns:
        What argparse returns: the ticker is in .ticker and the day is in .day.

    Example:
        parse_args(["TSLA", "2025-09-10"])
    returns
        Namespace(ticker='TSLA', day='2025-09-10')
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
def day_range(ticker: str, day: str) -> float:
    """Return high minus low for ticker on day (nan if there is no such row)."""
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["ticker"] == ticker and row["date"] == day:
                return round(float(row["high"]) - float(row["low"]), 2)  # round to cents
    return float("nan")


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])  # [1:] leaves out the program's name
    print(f"{args.ticker} {args.day} range {day_range(args.ticker, args.day)}")

# NOTES
#   Not in the lecture: parser.parse_args(argv) reads the list argv. With nothing
#   between the brackets, as in the lecture, it reads sys.argv[1:] itself.
