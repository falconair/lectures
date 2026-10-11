"""
PROBLEM 3
Practises: an optional argparse argument that has a type and a default.

Task: fill in the function parse_args.

To check your work, type:
    python p3_top_volume.py 2025-09-10 --top 2

It should print the 2 stocks with the most shares traded on that day:
    NVDA 226852000
    AAPL 83440800
"""

import argparse
import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Read a day and an optional --top from the command line, using argparse.

    The day is required. --top is how many stocks to print: a whole number,
    3 when the user leaves it out.

    Args:
        argv: what the user typed after the program's name, as a list of text.

    Returns:
        What argparse returns: the day is in .day (text) and the number is
        in .top (an int, not text).

    Examples:
        parse_args(["2025-09-10"])
    returns
        Namespace(day='2025-09-10', top=3)
    and
        parse_args(["2025-09-10", "--top", "5"])
    returns
        Namespace(day='2025-09-10', top=5)
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
def top_by_volume(day: str, top: int) -> list[tuple[str, int]]:
    """Return (ticker, volume) for the `top` most traded stocks on day, busiest first."""
    rows = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["date"] == day:
                rows.append((row["ticker"], int(row["volume"])))
    rows.sort(key=lambda pair: -pair[1])  # minus: largest volume first
    return rows[:top]


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])  # [1:] leaves out the program's name
    for ticker, volume in top_by_volume(args.day, args.top):
        print(ticker, volume)

# NOTES
#   Not in the lecture: add_argument(..., default=VALUE) sets the value used when
#   the user leaves an optional argument out.
#   Not in the lecture: parser.parse_args(argv) reads the list argv. With nothing
#   between the brackets, as in the lecture, it reads sys.argv[1:] itself.
