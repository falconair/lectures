"""
PROBLEM 2
Practises: selecting rows with .query, two conditions joined by and.

Task: fill in the function busy_days.

To check your work, type:
    python p2_busy_days.py AAPL 80000000

It should print what busy_days returned, the days on which more than
80 million AAPL shares traded:
       ticker        date    open    high     low   close     volume
    6    AAPL  2025-09-10  232.19  232.42  225.95  226.79   83440800
    13   AAPL  2025-09-19  241.23  246.30  240.21  245.50  163741300
    14   AAPL  2025-09-22  248.30  256.64  248.12  256.08  105517400
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def busy_days(prices_df: pd.DataFrame, ticker: str, min_volume: int) -> pd.DataFrame:
    """Return the rows of one stock on the days its volume was above min_volume.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date,
            open, high, low, close and volume.
        ticker: the stock to keep, for example "AAPL".
        min_volume: keep a day only if more shares than this traded.

    Returns:
        Those rows, with all their columns.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO"],
                                  "date": ["2025-09-02", "2025-09-02", "2025-09-03"],
                                  "open": [66.0, 11.0, 67.0],
                                  "close": [67.0, 12.0, 68.0],
                                  "volume": [10, 40, 30]})
        busy_days(prices_df, "KO", 20)
    returns
          ticker        date  open  close  volume
        2     KO  2025-09-03  67.0   68.0      30
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print(busy_days(prices_df, sys.argv[1], int(sys.argv[2])).to_string())
