"""
PROBLEM 1: make the program print its answer and take the ticker from the command line

THE PROGRAM
    It looks up the most recent closing price of one stock in prices.csv.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. It prints nothing. Try it:  python p1_last_close.py
    2. The ticker is written into the code, so it can only ever look up AAPL.
       Try it:  python p1_last_close.py MSFT   (still nothing, and MSFT is ignored)

WHEN YOU ARE DONE, these commands behave like this
    python p1_last_close.py AAPL    prints:  AAPL 254.63
    python p1_last_close.py MSFT    prints:  MSFT 517.95
    python p1_last_close.py         prints one line telling the user how to run it,
                                    and exits with status 1

    (An exit status is the number a program hands back when it ends: 0 means it
    worked. To see the status of the program you just ran, type:  echo $?  )

YOUR TASK
    Rewrite the lines at the bottom, below the line marked YOUR WORK.
    Do not change anything above that line.
    Use sys.argv, as in the lecture's program4.py and program5.py.
    Write plain top-level code, as the lecture does. No "if __name__ == ..." is needed.
"""

import csv
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
