"""
PROBLEM 3: tell argparse what kind of value each argument must be

THE PROGRAM
    It prints the most heavily traded stocks on one day, busiest first.
    It already uses argparse: a date, and an optional --top for how many to print.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    The arguments are declared, but argparse was never told what they should look
    like, so bad values get through and good ones break. Try each:
        python p3_top_volume.py 2025-09-10            prints all 10 stocks; it should print 3
        python p3_top_volume.py 2025-09-10 --top 5    crashes with a TypeError
        python p3_top_volume.py 9/10/2025             prints nothing and reports success

WHEN YOU ARE DONE, these commands behave like this
    python p3_top_volume.py 2025-09-10             prints exactly these three lines:
                                                       NVDA 226852000
                                                       AAPL 83440800
                                                       TSLA 72121700
    python p3_top_volume.py 2025-09-10 --top 5     prints 5 lines
    python p3_top_volume.py 2025-09-10 --top five  argparse error message, exit status 2
    python p3_top_volume.py 2025-09-10 --top 0     argparse error message, exit status 2
                                                   (--top must be 1 or more)
    python p3_top_volume.py 9/10/2025              argparse error message, exit status 2
                                                   (dates must be written YYYY-MM-DD)

    (An exit status is the number a program hands back when it ends: 0 means it
    worked. To see the status of the program you just ran, type:  echo $?  )

YOUR TASK
    Fix the lines at the bottom, below the line marked YOUR WORK, so that argparse
    does the checking. Do not change anything above that line.
    This goes one step past the lecture. Look up three things in the argparse
    documentation: type=, default=, and argparse.ArgumentTypeError (you raise it
    from a small function of your own to reject a value).
    Write plain top-level code. No "if __name__ == ..." is needed.
"""

import argparse
import csv
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def top_by_volume(day, top):
    """Return the `top` most traded tickers on day as (ticker, volume) pairs, busiest first."""
    rows = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["date"] == day:
                rows.append((row["ticker"], int(row["volume"])))
    rows.sort(key=lambda pair: -pair[1])  # minus: largest volume first
    return rows[:top]


# ---- YOUR WORK: everything below this line ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("date")
parser.add_argument("--top")
args = parser.parse_args()

for ticker, volume in top_by_volume(args.date, args.top):
    print(ticker, volume)
