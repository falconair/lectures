"""
PROBLEM 3
Practises: aggregates by group, with groupby and aggregate.

Task: fill in the function close_range.

To check your work, type:
    python p3_close_range.py

It should print what close_range returned for September 2025:
               min     max
    ticker
    AAPL    226.79  256.87
    AMZN    218.15  238.24
    F        11.42   12.09
    GME      22.37   27.28
    JPM     292.91  316.06
    KO       65.67   69.06
    MSFT    495.00  517.95
    NVDA    167.02  186.58
    TSLA    329.36  444.72
    XOM     109.23  117.22
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def close_range(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return each stock's lowest and highest closing price.

    Args:
        prices_df: one row per stock per day, with the columns ticker and close.

    Returns:
        A table whose index is the ticker, with two columns: min is the
        lowest close of that stock, max is its highest.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO"],
                                  "date": ["2025-09-02", "2025-09-02", "2025-09-03"],
                                  "open": [66.0, 11.0, 67.0],
                                  "close": [67.0, 12.0, 68.0],
                                  "volume": [10, 40, 30]})
        close_range(prices_df)
    returns
                 min   max
        ticker
        F       12.0  12.0
        KO      67.0  68.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print(close_range(prices_df).to_string())
