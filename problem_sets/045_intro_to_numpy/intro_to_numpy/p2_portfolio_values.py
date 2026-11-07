"""
PROBLEM 2
Practises: columns of data as a matrix, and the dot product.

Task: fill in the functions ticker_closes and portfolio_values.

To check your work, type:
    python p2_portfolio_values.py KO

It should print the first three values each function returned:
    ticker_closes: [69.06 68.99 68.25]
    portfolio_values: [19895.5  19875.94 20090.07]
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def ticker_closes(closes: np.ndarray, tickers: list[str], ticker: str) -> np.ndarray:
    """Return one stock's column of a matrix of closing prices.

    Args:
        closes: a matrix of closing prices, one row per date, one column per ticker.
        tickers: the tickers of the columns, in order.
        ticker: the stock to return.

    Returns:
        That stock's closing prices, one per date.

    Example:
        closes = np.array([[10.0, 20.0, 30.0],
                           [11.0, 21.0, 31.0]])
        ticker_closes(closes, ["AAPL", "F", "KO"], "F")
    returns
        array([20., 21.])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def portfolio_values(closes: np.ndarray, shares: list[int]) -> np.ndarray:
    """Return what a portfolio was worth on each date, with a dot product.

    The value on one date is, for every stock, its closing price times the number
    of shares held, all added up.

    Args:
        closes: a matrix of closing prices, one row per date, one column per ticker.
        shares: the number of shares held of each stock, in the order of the columns.

    Returns:
        The value of the portfolio, one per date.

    Example:
        closes = np.array([[10.0, 20.0],
                           [11.0, 19.0],
                           [12.0, 22.0]])
        portfolio_values(closes, [2, 1])
    returns
        array([40., 41., 46.])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    ticker = sys.argv[1]
    prices_df = pd.read_csv(PRICES)
    closes_df = prices_df.pivot(index="date", columns="ticker", values="close")
    closes = closes_df.to_numpy()
    tickers = list(closes_df.columns)
    # the number of shares of AAPL, AMZN, F, GME, JPM, KO, MSFT, NVDA, TSLA, XOM
    shares = [10, 20, 100, 50, 5, 40, 2, 10, 1, 30]
    print("ticker_closes:", ticker_closes(closes, tickers, ticker)[:3])
    print("portfolio_values:", portfolio_values(closes, shares)[:3])

# NOTES
#   Not in the lecture: tickers.index("F") gives the position of "F" in the list.
