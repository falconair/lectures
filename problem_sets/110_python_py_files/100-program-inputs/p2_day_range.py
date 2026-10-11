"""
PROBLEM 2: replace the typed-in questions with argparse arguments, and report missing data

YOUR TASK
    Rewrite the lines below the line marked YOUR WORK. Do not change anything above it.
    Your work is checked by running the commands at the end of this comment.
    These are graded:
      - the ticker and the date are two command-line arguments, read with argparse
      - the program never waits for the user to type something
      - when there is data, it prints the same line as it does now, with the range
      - --help shows a help text, written by you, beside each of the two arguments
      - an argument is missing: argparse's own error message, exit status 2
      - there is no data for that ticker and day: it prints one line that says so
        instead of the "range" line, and the exit status is 1
    Write your code directly below the line, not inside a function, as the lecture's
    programs do. No "if __name__ == ..." is needed.

THE PROGRAM
    It prints how far one stock moved in one day: that day's high minus its low.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p2_day_range.py
       It stops and waits for a person to type the ticker and then the date. When the
       program is started automatically at night, nobody is there to type.
    2. Run it again and type TSLA, then 2025-09-06 (a Saturday).
       It prints  TSLA 2025-09-06 range None  and the exit status is 0.

WHEN YOU ARE DONE, these commands behave like this
    python p2_day_range.py TSLA 2025-09-10
        TSLA 2025-09-10 range 10.26
    python p2_day_range.py --help
        (argparse's help text, with your help text beside each argument)
    python p2_day_range.py TSLA
        (argparse's error message)
        exit status 2
    python p2_day_range.py TSLA 2025-09-06
        (one line that says there is no data)
        exit status 1

    Exit status: a number a program returns when it ends (0 = it worked). To see it, the
    very next command must be:  echo $?
"""

import argparse
import csv
import sys
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
