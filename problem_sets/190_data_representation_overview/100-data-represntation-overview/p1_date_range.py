"""
PROBLEM 1
Practises: looking rows up by date, using a date index.

Task: fill in the function closes_between.

To check your work, type:
    python p1_date_range.py AAPL 2025-09-08 2025-09-12

It should print what closes_between returned:
    date
    2025-09-08    237.88
    2025-09-09    234.35
    2025-09-10    226.79
    2025-09-11    230.03
    2025-09-12    234.07
"""

import argparse
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def closes_between(prices_df: pd.DataFrame, ticker: str, start: str, end: str) -> pd.Series:
    """Return ticker's closing prices from start to end, both dates included.

    Args:
        prices_df: one row per ticker per day, with the columns ticker, date and close.
            The dates are text, like "2025-09-02".
        ticker: for example "AAPL".
        start: the first date, as text, "YYYY-MM-DD".
        end: the last date, as text, "YYYY-MM-DD".

    Returns:
        A Series of closing prices whose index is the date, oldest first.

    Example. 2025-09-01 was a holiday, so the result starts on the 2nd:
        closes_between(prices_df, "AAPL", "2025-09-01", "2025-09-03")
    returns
        date
        2025-09-02    229.72
        2025-09-03    238.47
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("start", help="first date, YYYY-MM-DD")
    parser.add_argument("end", help="last date, YYYY-MM-DD")
    args = parser.parse_args()

    prices_df = pd.read_csv(PRICES)
    print(closes_between(prices_df, args.ticker, args.start, args.end).to_string())
