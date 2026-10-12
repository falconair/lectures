"""
PROBLEM 1
Practises: making a Series whose index is a label, not a position.

Task: fill in the function closes_by_ticker.

To check your work, type:
    python p1_closes_by_ticker.py

It should print what closes_by_ticker returned for the closes of 2025-09-10:
    AAPL    226.79
    AMZN    230.33
    F        11.42
    GME      24.37
    JPM     300.54
    KO       67.82
    MSFT    500.37
    NVDA    177.33
    TSLA    347.79
    XOM     112.50
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def closes_by_ticker(tickers: list[str], closes: list[float]) -> pd.Series:
    """Return a Series of closing prices whose index is the ticker.

    Args:
        tickers: one ticker per stock.
        closes: the closing price of each of those stocks, in the same order.

    Returns:
        A Series of the closes, with the tickers as its index.

    Example:
        closes_by_ticker(["KO", "F"], [67.82, 11.42])
    returns
        KO    67.82
        F     11.42
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    day_df = prices_df.loc[prices_df.date == "2025-09-10"]
    print(closes_by_ticker(day_df.ticker.tolist(), day_df.close.tolist()).to_string())
