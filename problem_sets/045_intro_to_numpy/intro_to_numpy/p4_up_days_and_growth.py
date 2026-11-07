"""
PROBLEM 4
Practises: choosing the axis of a sum and of a running product.

Task: fill in the functions up_days_per_stock and growth_of_one_dollar.

To check your work, type:
    python p4_up_days_and_growth.py

It should print, for each stock, what up_days_per_stock returned and the last row
of what growth_of_one_dollar returned:
          up_days  dollar_at_end
    AAPL       11         1.1084
    F           9         1.0205
    KO          6         0.9603
    NVDA       12         1.0925
    TSLA       16         1.3503
"""

from pathlib import Path

import numpy as np
import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
TICKERS = ["AAPL", "F", "KO", "NVDA", "TSLA"]


def up_days_per_stock(returns: np.ndarray) -> np.ndarray:
    """Return how many days each stock went up.

    Args:
        returns: a matrix of daily returns, one row per date, one column per ticker.

    Returns:
        One count per stock: the number of its returns above 0. A return of
        exactly 0 is not an up day.

    Example:
        returns = np.array([[0.5, 0.25],
                            [0.0, -0.5],
                            [0.5, -0.5]])
        up_days_per_stock(returns)
    returns
        array([2, 1])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def growth_of_one_dollar(returns: np.ndarray) -> np.ndarray:
    """Return what one dollar put in each stock was worth after each date.

    Each date multiplies a stock's money by 1 + that date's return, so the answer is
    the running product of 1 + returns, down each column.

    Args:
        returns: a matrix of daily returns, one row per date, one column per ticker.

    Returns:
        A matrix of the same shape: the value of one dollar in each stock at the
        end of each date.

    Example:
        returns = np.array([[0.5, 0.25],
                            [0.0, -0.5],
                            [0.5, -0.5]])
        growth_of_one_dollar(returns)
    returns
        array([[1.5   , 1.25  ],
               [1.5   , 0.625 ],
               [2.25  , 0.3125]])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    closes_df = prices_df.pivot(index="date", columns="ticker", values="close")[TICKERS]
    closes = closes_df.to_numpy()
    returns = closes[1:] / closes[:-1] - 1  # the first date has no return
    report = {
        "up_days": up_days_per_stock(returns),
        "dollar_at_end": growth_of_one_dollar(returns)[-1],
    }
    print(pd.DataFrame(report, TICKERS).round(4).to_string())

# NOTES
#   Not in the lecture: .cumprod() is the running product, as .cumsum() is the
#   running sum. Both take an axis, as .sum() does.
