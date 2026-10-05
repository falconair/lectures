"""
PROBLEM 2: replace the typed-in questions with command-line arguments

THE PROGRAM
    It prints how far one stock moved in one day: that day's high minus its low.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. It stops and asks the user to type the ticker and the date.
       Try it:  python p2_day_range.py
       A scheduler that starts this program at 2 a.m. has nobody to answer.
    2. When there is no data for that ticker and day, it prints "range None"
       and carries on as if nothing were wrong.
       Try it: answer TSLA and 2025-09-06 (a Saturday).

WHEN YOU ARE DONE, these commands behave like this
    python p2_day_range.py TSLA 2025-09-10    prints:  TSLA 2025-09-10 range 10.26
    python p2_day_range.py --help             explains both arguments
    python p2_day_range.py TSLA               argparse's own error message, exit status 2
    python p2_day_range.py TSLA 2025-09-06    prints one line saying there is no data,
                                              and exits with status 1

    (An exit status is the number a program hands back when it ends: 0 means it
    worked. To see the status of the program you just ran, type:  echo $?  )

YOUR TASK
    Rewrite the lines at the bottom, below the line marked YOUR WORK.
    Do not change anything above that line.
    Use argparse, as in the lecture's program6.py.
    Write plain top-level code, as the lecture does. No "if __name__ == ..." is needed.
"""

import csv
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def day_range(ticker, day):
    """Return high minus low for ticker on day ("YYYY-MM-DD"), or None if there is no such row."""
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["ticker"] == ticker and row["date"] == day:
                return round(float(row["high"]) - float(row["low"]), 2)  # round to cents
    return None


# ---- YOUR WORK: everything below this line ---------------------------------
ticker = input("Ticker: ")
day = input("Date (YYYY-MM-DD): ")

print(f"{ticker} {day} range {day_range(ticker, day)}")
