"""
PROBLEM 1
Practises: one number per group, with groupby.

Task: fill in the function average_volume.

To check your work, type:
    python p1_average_volume.py

It should print what average_volume returned for September 2025, in millions of shares:
    ticker
    AAPL     60.3
    AMZN     46.0
    F        59.2
    GME      11.0
    JPM       8.7
    KO       18.6
    MSFT     20.2
    NVDA    185.3
    TSLA     94.0
    XOM      16.8
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def average_volume(prices_df: pd.DataFrame) -> pd.Series:
    """Return each stock's average daily volume.

    Args:
        prices_df: one row per stock per day, with the columns ticker and volume.

    Returns:
        A Series whose index is the ticker and whose values are the average volume.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO"], "volume": [10, 40, 30]})
        average_volume(prices_df)
    returns
        ticker
        F     40.0
        KO    20.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print((average_volume(prices_df) / 1e6).round(1).to_string())
