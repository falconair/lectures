"""
PROBLEM 1
Practises: selecting columns with a list, and rows with a condition.

Task: fill in the function one_day.

To check your work, type:
    python p1_one_day.py 2025-09-10

It should print what one_day returned:
        ticker   close     volume
    6     AAPL  226.79   83440800
    27    AMZN  230.33   60907700
    48       F   11.42   47021300
    69     GME   24.37   46254000
    90     JPM  300.54    7787300
    111     KO   67.82   16041900
    132   MSFT  500.37   21611800
    153   NVDA  177.33  226852000
    174   TSLA  347.79   72121700
    195    XOM  112.50   15837600
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def one_day(prices_df: pd.DataFrame, date: str) -> pd.DataFrame:
    """Return the ticker, closing price and volume of every stock on one day.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date,
            open, high, low, close and volume.
        date: the day to keep, as text, for example "2025-09-10".

    Returns:
        The rows of that day, with only the columns ticker, close and volume.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO"],
                                  "date": ["2025-09-02", "2025-09-02", "2025-09-03"],
                                  "open": [66.0, 11.0, 67.0],
                                  "close": [67.0, 12.0, 68.0],
                                  "volume": [10, 40, 30]})
        one_day(prices_df, "2025-09-02")
    returns
          ticker  close  volume
        0     KO   67.0      10
        1      F   12.0      40
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print(one_day(prices_df, sys.argv[1]).to_string())
