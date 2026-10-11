"""
PROBLEM 2
Practises: a different calculation for each column of a group.

Task: fill in the function price_range.

To check your work, type:
    python p2_price_range.py

It should print what price_range returned for September 2025:
               low    high
    ticker
    AAPL    225.95  257.60
    AMZN    216.47  238.85
    F        11.31   12.32
    GME      22.18   27.34
    JPM     291.44  318.01
    KO       65.35   69.46
    MSFT    492.37  519.30
    NVDA    164.07  187.35
    TSLA    325.60  450.98
    XOM     108.35  118.36
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def price_range(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return the lowest and the highest price each stock traded at.

    Args:
        prices_df: one row per stock per day, with the columns ticker, low and high
            (the lowest and highest price of that day).

    Returns:
        A table whose index is the ticker, with two columns: low is the
        lowest of the stock's lows, high is the highest of its highs.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO"], "low": [66.0, 11.0, 65.0], "high": [68.0, 12.0, 67.0]})
        price_range(prices_df)
    returns
                 low  high
        ticker
        F       11.0  12.0
        KO      65.0  68.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print(price_range(prices_df).to_string())
