"""
PROBLEM 1: make the program print the last close of the ticker given on the command line

YOUR TASK
    Rewrite the lines below the line marked YOUR WORK. Do not change anything above it.
    Your work is checked by running the commands at the end of this comment.
    These are graded:
      - the ticker is read from the command line
      - it prints one line: the ticker, a space, and that ticker's last closing price
      - no ticker on the command line: it prints one line that tells the user how to
        run the program, and the exit status is 1
      - a ticker that is not in prices.csv: it prints one line that says there is no
        such ticker, and the exit status is 1
      - it never ends with a Python error (a "Traceback")
    Write your code directly below the line, not inside a function, as the lecture's
    programs do. No "if __name__ == ..." is needed.

THE PROGRAM
    It looks up the most recent closing price of one stock in prices.csv.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p1_last_close.py         prints nothing
    2. python p1_last_close.py MSFT    prints nothing

WHEN YOU ARE DONE, these commands behave like this
    python p1_last_close.py AAPL
        AAPL 254.63
    python p1_last_close.py MSFT
        MSFT 517.95
    python p1_last_close.py
        (one line that says how to run the program)
        exit status 1
    python p1_last_close.py ZZZ
        (one line that says there is no such ticker)
        exit status 1

    Exit status: a number a program returns when it ends (0 = it worked). To see it, the
    very next command must be:  echo $?
"""

import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def last_close(ticker):
    """Return the most recent closing price of ticker, or None if it is not in the file."""
    price = None
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line: row["close"]
            if row["ticker"] == ticker:
                price = float(row["close"])  # the file is in date order, so the last one wins
    return price


# ---- YOUR WORK: everything below this line ---------------------------------
ticker = "AAPL"
price = last_close(ticker)
f"{ticker} {price}"
