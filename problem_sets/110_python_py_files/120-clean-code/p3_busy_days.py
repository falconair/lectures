"""
PROBLEM 3
Practises: writing a function that changes nothing it was given.

Task: repair the function busiest_days. Its answer is right, but it reorders
the list it is given, and the code that uses that list afterwards goes wrong.

To check your work, type:
    python p3_busy_days.py AAPL

It should print what busiest_days returned, then AAPL's return over the month:
    AAPL busiest days ['2025-09-19', '2025-09-22', '2025-09-10']
    AAPL month return 10.84%
"""

import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def busiest_days(rows: list[dict], count: int = 3) -> list[str]:
    """Return the dates of the `count` days with the most shares traded, busiest first.

    rows is left exactly as it was given.

    Args:
        rows: one dict per trading day, with the keys "date" and "volume".
        count: how many dates to return.

    Returns:
        A list of dates, as text.

    Example:
        rows = [{"date": "2025-09-02", "volume": 10},
                {"date": "2025-09-03", "volume": 30},
                {"date": "2025-09-04", "volume": 20}]
        busiest_days(rows, 2)
    returns
        ['2025-09-03', '2025-09-04']
    and rows still starts with the row for 2025-09-02.
    """
    # YOUR WORK: repair the lines below
    rows.sort(key=lambda row: -row["volume"])  # key: the value to sort by; minus: largest first
    dates = []
    for row in rows[:count]:
        dates.append(row["date"])
    return dates


# ---- do not change anything below this line --------------------------------
def load_rows(ticker: str) -> list[dict]:
    """Return one dict per trading day for ticker, oldest first: date, close, volume."""
    rows = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line of the file
            if row["ticker"] == ticker:
                rows.append({"date": row["date"], "close": float(row["close"]), "volume": int(row["volume"])})
    return rows


if __name__ == "__main__":
    ticker = sys.argv[1]
    rows = load_rows(ticker)
    print(f"{ticker} busiest days {busiest_days(rows)}")
    month_return = rows[-1]["close"] / rows[0]["close"] - 1  # last day against first day
    print(f"{ticker} month return {month_return:.2%}")
