"""
PROBLEM 4
Practises: checking that tidied code still does what the old code did.

Task: repair volume_weighted_closes and the functions it calls, so that it
returns exactly what summ returns and leaves the rows it is given unchanged.
It differs from summ in four ways.

To check your work, type these three commands:
    python p4_review_tidy_up.py 0
    python p4_review_tidy_up.py 60000000
    python p4_review_tidy_up.py 83440800

The last line each of them prints should be:
    SAME
"""

import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


# The old version: hard to read, but what it returns is correct. Do not change it.
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


# The new version: summ rewritten with clear names, small functions and docstrings.
# It was meant to be only cleaner.
# ---- YOUR WORK: the four functions below ------------------------------------
def is_busy_enough(row: dict, min_volume: int) -> bool:
    """Return True when enough shares traded that day for it to count."""
    return row["volume"] > min_volume


def drop_quiet_days(rows: list[dict], min_volume: int) -> list[dict]:
    """Remove the days on which too few shares traded."""
    for row in list(rows):  # list(rows) is a copy to loop over
        if not is_busy_enough(row, min_volume):
            rows.remove(row)
    return rows


def total_by_ticker(rows: list[dict]) -> dict[str, tuple]:
    """Add up days, shares and traded value (shares times close) for each ticker."""
    totals = {}
    for row in rows:
        # .get: this ticker's totals so far, or (0, 0, 0.0) the first time
        days, shares, value = totals.get(row["ticker"], (0, 0, 0.0))
        totals[row["ticker"]] = (days + 1, shares + row["volume"], value + row["volume"] * row["close"])
    return totals


def volume_weighted_closes(rows: list[dict], min_volume: int = 1) -> list[tuple]:
    """Return (ticker, days, total shares, volume-weighted average close) for each ticker.

    Days on which fewer than min_volume shares traded are ignored.

    Args:
        rows: one dict per stock per day, with the keys "ticker", "close" and "volume".
        min_volume: the fewest shares a day must have traded to be counted.

    Returns:
        One tuple per ticker, exactly as summ(rows, min_volume) returns them.
    """
    totals = total_by_ticker(drop_quiet_days(rows, min_volume))
    summary = []
    for ticker in sorted(totals):
        days, shares, value = totals[ticker]
        summary.append((ticker, days, shares, round(value / shares, 2)))
    return summary


# ---- do not change anything below this line --------------------------------
def load_rows() -> list[dict]:
    """Return one dict per stock per day (ticker, date, close, volume), oldest day first."""
    rows = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line of the file
            rows.append(
                {"ticker": row["ticker"], "date": row["date"], "close": float(row["close"]), "volume": int(row["volume"])}
            )
    rows.sort(key=lambda row: row["date"])  # the file is grouped by ticker; put it in date order
    return rows


if __name__ == "__main__":
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
    print("rows given to the new function:", rows_before, "before the call,", len(new_rows), "after")
    print("SAME" if new_answer == old_answer and new_rows == old_rows else "DIFFERENT")
