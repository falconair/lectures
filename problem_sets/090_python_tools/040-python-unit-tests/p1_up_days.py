"""
PROBLEM 1: repair three tests that cannot fail

YOUR TASK
    Change only the lines below the line marked YOUR WORK.
    What is graded:
    - the three tests are still there, each with the prices it has now
      (a test may be renamed)
    - pytest runs all three, and all three pass
    - at least one of your tests fails for each wrong version listed at the end
    How it is graded: your tests are run against the correct up_days and against each
    wrong version. You cannot run that yourself, but you can make each change to up_days
    by hand, watch a test fail, and change it back.

THE PROGRAM
    up_days counts the days on which a stock closed higher than the day before. The
    function is correct. Below it are three tests for it. (In a project the tests are in
    their own file in tests/, as in the lecture. Here they share a file with the
    function, so you give pytest the name of the file.)

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. pytest does not run every test. Try:
           pytest p1_up_days.py
       The last line says "2 passed". The file has three tests. Try:
           pytest -v p1_up_days.py
       -v lists each test that ran: compare the list with the file. (Not in the lecture:
       pytest decides from a function's name whether it is a test.)
    2. The tests still pass when the function is wrong. On the line marked BREAK ME
       change  >  to  <  so that up_days counts the down days, and run pytest again.
       It still says "2 passed". Change it back.
    Each test has a different fault. The prices and the expected 3 and 0 are correct.

WHEN YOU ARE DONE, these commands behave like this
    pytest p1_up_days.py
        3 passed
    The same command with  <  on the BREAK ME line (then change it back):
        3 failed
    The wrong versions of up_days that your tests are run against:
        a. a day that closes at the same price as the day before is counted as up
        b. each day is compared with the first day instead of the day before
        c. the last day is never looked at
"""

import csv
from pathlib import Path

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


def up_days(closes):
    """Return how many days closed higher than the day before."""
    count = 0
    for i in range(1, len(closes)):
        if closes[i] > closes[i - 1]:  # BREAK ME
            count += 1
    return count


# ---- YOUR WORK: everything below this line ---------------------------------
def test_up_days_every_day_higher():
    up_days([10.0, 11.0, 12.0, 13.0]) == 3


def check_up_days_same_close_is_not_up():
    assert up_days([50.0, 50.0, 49.0]) == 0


def test_up_days_first_six_aapl_closes():
    closes = load_closes("AAPL")[:6]
    expected = up_days(closes)
    assert up_days(closes) == expected
