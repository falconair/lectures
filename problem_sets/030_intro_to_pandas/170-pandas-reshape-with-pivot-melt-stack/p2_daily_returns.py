"""
PROBLEM 2
Practises: pivoting first, so that a calculation runs down each stock's own column.

Task: fill in the function daily_returns.

To check your work, type:
    python p2_daily_returns.py AAPL F NVDA

It should print the first 5 rows of what daily_returns returned, for those three tickers, rounded:
    ticker        AAPL       F    NVDA
    date
    2025-09-02     NaN     NaN     NaN
    2025-09-03  0.0381 -0.0085 -0.0009
    2025-09-04  0.0055  0.0052  0.0061
    2025-09-05 -0.0004  0.0051 -0.0270
    2025-09-08 -0.0076 -0.0043  0.0077
"""

import argparse
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def daily_returns(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return each stock's daily return, as a table with one row per date and one column per ticker.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date and close.

    Returns:
        A table whose index is the date and whose columns are the tickers.
        Each value is that day's close / the day before's close - 1, for that
        stock. The first date has no day before, so its values are NaN.

    Example. F goes from 10 to 20 to 10, KO from 100 to 150 to 75:
        prices_df = pd.DataFrame({"ticker": ["F", "F", "F", "KO", "KO", "KO"],
                                  "date": ["2025-09-02", "2025-09-03", "2025-09-04"] * 2,
                                  "close": [10.0, 20.0, 10.0, 100.0, 150.0, 75.0]})
        daily_returns(prices_df)
    returns
        ticker        F   KO
        date
        2025-09-02  NaN  NaN
        2025-09-03  1.0  0.5
        2025-09-04 -0.5 -0.5
    If KO's first value is 9.0 and not NaN, it was worked out from F's last close.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tickers", nargs="+")
    args = parser.parse_args()

    prices_df = pd.read_csv(PRICES)
    print(daily_returns(prices_df)[args.tickers].head().round(4).to_string())

# NOTES
#   close / close.shift(1) - 1 is each day's return, as in the data representation
#   lecture. On a table, .shift(1) moves every column down one row.
