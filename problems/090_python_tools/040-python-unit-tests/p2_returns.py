"""
PROBLEM 2: compare floating point numbers in tests with pytest.approx, to a sensible tolerance

YOUR TASK
    Change only the lines below the line marked YOUR WORK.
    What is graded:
    - the three tests are still there, each with the prices it has now, and all three pass
    - at least one of your tests fails for each wrong version listed at the end
    - the test for AAPL's month fails for wrong version d
    How it is graded: your tests are run against the correct functions and against each
    wrong version. You cannot run that yourself, but you can make each change to the
    functions by hand, watch a test fail, and change it back.
    Type every expected value as a number. Calculate the one for AAPL's month yourself,
    from the closing prices in prices.csv.

THE PROGRAM
    daily_returns gives a stock's return for each day; total_return gives its return
    over the whole period. Both functions are correct. Below them are three tests.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. A test fails although the functions are correct. Try:
           pytest p2_returns.py
       The last line says "1 failed, 2 passed". Read the report above it.
    2. The two tests that pass still pass when total_return is wrong. On the line marked
       BREAK ME change  closes[0]  to  closes[1]  (the return is then measured from the
       second day) and run pytest again. It still says "1 failed, 2 passed". Change it
       back.
    Each test compares floating point numbers in a different wrong way. One has the form
    of the lecture's  (.1 + .2) - .3 < 0.000000001  and that line has the same weakness.
    Not in the lecture, about pytest.approx:
        pytest.approx(0.25)             accepts a relative difference of 1e-6 (one part in
                                        a million)
        pytest.approx([0.25, 0.5])      compares a list, item by item
        pytest.approx(0.25, abs=0.01)   accepts 0.24 to 0.26

WHEN YOU ARE DONE, these commands behave like this
    pytest p2_returns.py
        3 passed
    The same command with  closes[1]  on the BREAK ME line (then change it back):
        2 failed, 1 passed
    The wrong versions of the functions that your tests are run against:
        a. daily_returns divides by today's close instead of yesterday's
        b. both functions give log returns, log(new / old), instead of new / old - 1
        c. total_return measures from the second day instead of the first
        d. total_return adds up the daily returns instead of compounding them
"""

import csv
from pathlib import Path

import pytest

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def load_closes(ticker):
    """Return the closing prices of ticker in September 2025, oldest first."""
    closes = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line of the file
            if row["ticker"] == ticker:
                closes.append(float(row["close"]))  # the file is in date order
    return closes


def daily_returns(closes):
    """Return one return for each day after the first: that day's close / the day before's close - 1."""
    returns = []
    for i in range(1, len(closes)):
        returns.append(closes[i] / closes[i - 1] - 1)
    return returns


def total_return(closes):
    """Return the return over the whole period: last close / first close - 1."""
    return closes[-1] / closes[0] - 1  # BREAK ME


# ---- YOUR WORK: everything below this line ---------------------------------
def test_daily_returns():
    assert daily_returns([100.0, 110.0, 99.0]) == [0.1, -0.1]


def test_total_return_two_days():
    assert total_return([200.0, 210.0]) - 0.05 < 0.000000001


def test_total_return_aapl_month():
    closes = load_closes("AAPL")
    assert total_return(closes) == pytest.approx(0.1, abs=0.05)
