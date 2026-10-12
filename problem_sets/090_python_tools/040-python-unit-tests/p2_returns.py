"""
PROBLEM 2
Practises: comparing floating point numbers in a test.

Task: fill in the three tests of daily_returns and total_return. Both
functions are correct.

To check your work, type:
    pytest p2_returns.py

The last line it prints should say:
    3 passed
"""

import csv
from pathlib import Path

import pytest

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


def daily_returns(closes: list[float]) -> list[float]:
    """Return one return for each day after the first: that day's close / the day before's close - 1."""
    returns = []
    for i in range(1, len(closes)):
        returns.append(closes[i] / closes[i - 1] - 1)
    return returns


def total_return(closes: list[float]) -> float:
    """Return the return over the whole period: last close / first close - 1."""
    return closes[-1] / closes[0] - 1


# ---- YOUR WORK: the three tests below --------------------------------------
def test_daily_returns() -> None:
    """Check that daily_returns([100.0, 110.0, 99.0]) is [0.1, -0.1]."""
    raise NotImplementedError  # YOUR WORK: replace this line


def test_total_return_two_days() -> None:
    """Check that total_return([200.0, 210.0]) is 0.05."""
    raise NotImplementedError  # YOUR WORK: replace this line


def test_total_return_aapl_month() -> None:
    """Check AAPL's return over the month, total_return(load_closes("AAPL")).

    Work the expected return out yourself from the first and last close in
    prices.csv, and write it in the test as a number with 4 decimal places.
    The test must accept only returns that agree with it to 4 decimal places.
    """
    raise NotImplementedError  # YOUR WORK: replace this line

# NOTES
#   How your tests are graded: they are run against the function above, where
#   they must pass, and against wrong versions of it, where at least one of
#   them must fail. A test that cannot fail earns nothing.
#   Not in the lecture: pytest.approx([0.25, 0.5]) compares a list, item by item,
#   and pytest.approx(0.25, abs=0.01) accepts 0.24 to 0.26.
