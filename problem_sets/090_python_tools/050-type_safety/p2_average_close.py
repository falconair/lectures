"""
PROBLEM 2
Practises: annotating lists and dictionaries with the types of what they hold.

Task: add type annotations to average and highest_average. Each docstring
says what the types are. Change nothing else.

To check your work, type these two commands:
    mypy --strict p2_average_close.py
    python p2_average_close.py

They should print:
    Success: no issues found in 1 source file
    MSFT
"""

import csv
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def average(closes):
    """Return the average of closes.

    closes is a list of decimal numbers. The average is a decimal number.
    """
    return sum(closes) / len(closes)


def highest_average(closes_by_ticker):
    """Return the ticker whose closes have the highest average.

    closes_by_ticker is a dictionary. Each key is a ticker (text) and each
    value is that ticker's closes (a list of decimal numbers).
    """
    best_ticker = ""
    best_average = 0.0
    for ticker, closes in closes_by_ticker.items():
        if average(closes) > best_average:
            best_ticker = ticker
            best_average = average(closes)
    return best_ticker


# ---- do not change anything below this line --------------------------------
def load_closes_by_ticker() -> dict[str, list[float]]:
    """Return every ticker's closing prices in September 2025, oldest first."""
    closes_by_ticker: dict[str, list[float]] = {}
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line of the file
            closes_by_ticker.setdefault(row["ticker"], []).append(float(row["close"]))
    return closes_by_ticker


if __name__ == "__main__":
    print(highest_average(load_closes_by_ticker()))

# NOTES
#   Not in the lecture: --strict makes mypy also report a function that has no
#   type annotations. Without it, mypy says nothing about such a function.
