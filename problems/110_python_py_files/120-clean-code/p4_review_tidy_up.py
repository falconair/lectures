"""
PROBLEM 4: make a rewritten function give exactly the answers the old one gave

YOUR TASK
    Fix the code below the line marked YOUR WORK. Change nothing above that line,
    and leave the comparison at the bottom of the file as it is.
    Your work is checked by calling volume_weighted_closes with the rows of
    prices.csv and with short made-up lists of rows that you do not have.
    - volume_weighted_closes(rows, min_volume) returns exactly what
      summ(rows, min_volume) returns, and has no other effect, for any rows
      and any min_volume.
    - The new version does not call summ.
    - It keeps its four small functions and their names.
    - Every docstring says what the code does after your changes.
    ruff is not part of this problem.

THE PROGRAM
    For each stock it prints the number of trading days, the total shares traded
    and the volume-weighted average closing price, counting only the days on which
    at least MIN_VOLUME shares traded. MIN_VOLUME comes from the command line.
    The file holds two versions of the function that does this:
        summ                    the old one. Hard to read, but it has run every
                                night for two years. Its answers are correct.
        volume_weighted_closes  summ rewritten by an AI assistant: clear names,
                                small functions, docstrings. It came with the
                                note "Only cleaner. No change in behaviour."
    The program runs both, prints both answers, and then SAME or DIFFERENT.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    The note is false. Try it:
        python p4_review_tidy_up.py 0
        python p4_review_tidy_up.py 60000000
        python p4_review_tidy_up.py 83440800
    Every one ends with DIFFERENT. Between them they show four ways in which the
    new version behaves differently from the old one; find all four.
    The four differences are not one in each function. Each fix is a few lines
    at most.

WHEN YOU ARE DONE, these commands behave like this
    python p4_review_tidy_up.py 0
    python p4_review_tidy_up.py 60000000
    python p4_review_tidy_up.py 83440800
    The last line each of them prints, and the last line for any other whole
    number you try, is:
        SAME
"""

import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def load_rows():
    """Return one dict per stock per day (ticker, date, close, volume), oldest day first."""
    rows = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line of the file
            rows.append(
                {
                    "ticker": row["ticker"],
                    "date": row["date"],
                    "close": float(row["close"]),
                    "volume": int(row["volume"]),
                }
            )
    rows.sort(
        key=lambda row: row["date"]
    )  # the file is grouped by ticker; put it in date order
    return rows


# The old version. Do not change it: what it returns is, by definition, correct.
def summ(rows, min_volume=1):
    t = {}
    for r in rows:
        if r["volume"] < min_volume:
            continue
        s = r["ticker"]
        if s not in t:
            t[s] = [0, 0, 0.0]
        t[s][0] += 1
        t[s][1] += r["volume"]
        t[s][2] += r["volume"] * r["close"]
    out = []
    for s in t:  # a dict gives back its keys in the order they were first added
        out.append((s, t[s][0], t[s][1], t[s][2] / t[s][1]))
    return out


# ---- YOUR WORK: everything below this line ---------------------------------
def is_busy_enough(row, min_volume):
    """Return True when enough shares traded that day for it to count."""
    return row["volume"] > min_volume


def drop_quiet_days(rows, min_volume):
    """Remove the days on which too few shares traded."""
    for row in list(rows):  # list(rows) is a copy to loop over
        if not is_busy_enough(row, min_volume):
            rows.remove(row)
    return rows


def total_by_ticker(rows):
    """Add up days, shares and traded value (shares times close) for each ticker."""
    totals = {}
    for row in rows:
        # .get: this ticker's totals so far, or (0, 0, 0.0) the first time
        days, shares, value = totals.get(row["ticker"], (0, 0, 0.0))
        totals[row["ticker"]] = (
            days + 1,
            shares + row["volume"],
            value + row["volume"] * row["close"],
        )
    return totals


def volume_weighted_closes(rows, min_volume=1):
    """Return (ticker, days, total shares, volume-weighted average close) for each ticker.

    Days on which fewer than min_volume shares traded are ignored.
    """
    totals = total_by_ticker(drop_quiet_days(rows, min_volume))
    summary = []
    for ticker in sorted(totals):
        days, shares, value = totals[ticker]
        summary.append((ticker, days, shares, round(value / shares, 2)))
    return summary


# ---- THE COMPARISON: leave everything below this line as it is ---------------
if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print(
        "usage: python p4_review_tidy_up.py MIN_VOLUME      (a whole number of shares)"
    )
    sys.exit(1)
min_volume = int(sys.argv[1])

old_rows = load_rows()
old_answer = summ(old_rows, min_volume)

new_rows = load_rows()
rows_before = len(new_rows)
new_answer = volume_weighted_closes(new_rows, min_volume)

for line in old_answer:
    print("old", line)
for line in new_answer:
    print("new", line)
print(
    "rows given to the new function:",
    rows_before,
    "before the call,",
    len(new_rows),
    "after",
)
print("SAME" if new_answer == old_answer and new_rows == old_rows else "DIFFERENT")
