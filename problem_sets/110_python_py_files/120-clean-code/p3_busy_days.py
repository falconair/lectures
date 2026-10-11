"""
PROBLEM 3: fix two functions so that the report prints the right answers

YOUR TASK
    Fix the two functions below the line marked YOUR WORK. Change nothing above
    that line, and leave the report at the bottom of the file as it is.
    Your work is checked by running the commands under WHEN YOU ARE DONE, and by
    calling the two functions by name with a few made-up rows.
    - busiest_days and big_moves keep their names and their arguments.
    - The report prints the right month return and the right moves.
    - Each function gives the same answer whenever and however often it is
      called, and changes nothing it was given. One exception, which the
      docstring promises: a list passed as `found` gets the dates added to it.

THE PROGRAM
    For each ticker on the command line it prints three lines: the return over the
    month, the three days with the most shares traded, and the days on which the
    closing price moved more than 3% from the day before.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    Both functions look clean and the program runs without an error, but some of
    what it prints is wrong. There are two separate faults.
    1. Try it:  python p3_busy_days.py AAPL
       It prints a month return of 3.72%. AAPL rose 10.84% that month.
       The line of moves over 3% is wrong too: it lists 14 dates, not in date
       order. The line of busiest days is right.
    2. Try it:  python p3_busy_days.py NVDA GME
       GME's line of moves starts with NVDA's dates. It still does after you
       have fixed the first fault, and it is easier to see then.
       The lecture did not cover this one. When you think you have found it,
       a linter can confirm it:  ruff check --select B p3_busy_days.py
       (B is a set of rules for likely bugs. Do not use --fix here: the task
       is to understand the fault.) No linter reports the first fault.

WHEN YOU ARE DONE, these commands behave like this
    python p3_busy_days.py AAPL
        AAPL month return 10.84%
        AAPL busiest days 2025-09-19 2025-09-22 2025-09-10
        AAPL moves over 3% 2025-09-03 2025-09-10 2025-09-19 2025-09-22
    The next command prints six lines. The last one is shown.
    python p3_busy_days.py NVDA GME
        GME moves over 3% 2025-09-10 2025-09-16 2025-09-25 2025-09-26
    The next command prints the same three lines twice.
    python p3_busy_days.py GME GME
    ruff check --select B p3_busy_days.py
        All checks passed!
"""

import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def load_rows(ticker):
    """Return one dict per trading day for ticker, oldest first: date, close, volume."""
    rows = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line of the file
            if row["ticker"] == ticker:
                rows.append(
                    {
                        "date": row["date"],
                        "close": float(row["close"]),
                        "volume": int(row["volume"]),
                    }
                )
    return rows


# ---- YOUR WORK: everything below this line ---------------------------------
def busiest_days(rows, count=3):
    """Return the dates of the `count` days with the most shares traded, busiest first."""
    rows.sort(
        key=lambda row: -row["volume"]
    )  # key: the value to sort by; minus: largest first
    dates = []
    for row in rows[:count]:
        dates.append(row["date"])
    return dates


def big_moves(rows, threshold=0.03, found=[]):
    """Return the dates on which the close moved more than `threshold` from the day before.

    `rows` must be in date order. Pass a list as `found` to have the dates added to it.
    """
    for i in range(1, len(rows)):
        change = rows[i]["close"] / rows[i - 1]["close"] - 1
        if abs(change) > threshold:  # abs: a fall of 4% is a move too
            found.append(rows[i]["date"])
    return found


# ---- THE REPORT: leave everything below this line as it is ------------------
for ticker in sys.argv[1:]:
    rows = load_rows(ticker)
    if not rows:
        print("no data for", ticker)
        sys.exit(1)
    busiest = busiest_days(rows)
    moves = big_moves(rows)
    month_return = (
        rows[-1]["close"] / rows[0]["close"] - 1
    )  # last day against first day
    print(f"{ticker} month return {month_return:.2%}")
    print(f"{ticker} busiest days {' '.join(busiest)}")
    print(f"{ticker} moves over 3% {' '.join(moves) or 'none'}")
