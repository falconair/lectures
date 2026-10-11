"""
PROBLEM 1
Practises: writing tests with assert.

Task: fill in the three tests of up_days. The function up_days is correct.

To check your work, type:
    pytest p1_up_days.py

The last line it prints should say:
    3 passed
"""

import csv
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def load_closes(ticker: str) -> list[float]:
    """Return the closing prices of ticker in September 2025, oldest first."""
    closes = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line of the file
            if row["ticker"] == ticker:
                closes.append(float(row["close"]))  # the file is in date order
    return closes


def up_days(closes: list[float]) -> int:
    """Return how many days closed higher than the day before."""
    count = 0
    for i in range(1, len(closes)):
        if closes[i] > closes[i - 1]:
            count += 1
    return count


# ---- YOUR WORK: the three tests below --------------------------------------
def test_every_day_higher() -> None:
    """Check what up_days returns when every close is higher than the one before.

    Use the closes [10.0, 11.0, 12.0, 13.0].
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def test_same_close_is_not_up() -> None:
    """Check that a day which closes at the same price as the day before is not counted.

    Use the closes [50.0, 50.0, 49.0].
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def test_first_six_aapl_closes() -> None:
    """Check what up_days returns for AAPL's first six closes of the month.

    The closes are load_closes("AAPL")[:6]. Look at them, count the up days
    yourself, and write that count in the test as a number.
    """
    raise NotImplementedError  # YOUR WORK: replace this line

# NOTES
#   How your tests are graded: they are run against the function above, where
#   they must pass, and against wrong versions of it, where at least one of
#   them must fail. A test that cannot fail earns nothing.
