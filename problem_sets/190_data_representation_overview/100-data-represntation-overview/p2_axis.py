"""
PROBLEM 2
Practises: taking an average along the correct axis of a 3-dimensional array.

Task: fill in the functions average_per_stock and basket_return_per_day.

To check your work, type:
    python p2_axis.py

It should print what average_per_stock returned, then what
basket_return_per_day returned:
    [[241.9  242.49]
     [306.95 307.54]
     [ 67.11  67.04]
     [394.12 395.89]
     [113.14 113.09]]
    [ 0.0019 -0.003   0.0031 -0.0091 -0.0082  0.0024 -0.0011  0.0167  0.016
     -0.0064  0.0064  0.009  -0.0096  0.0042  0.0088 -0.0037  0.0035 -0.0036
      0.0084 -0.0035  0.0004]
"""

from pathlib import Path

import numpy as np
import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"

TICKERS = ["AAPL", "JPM", "KO", "TSLA", "XOM"]
OPEN, CLOSE = 0, 1  # positions of the two kinds of price along dimension 1

# Both functions take a "cube": a 3-dimensional array of prices.
#   dimension 0: the stocks
#   dimension 1: the kind of price, OPEN then CLOSE
#   dimension 2: the trading days, oldest first
# So cube[0, CLOSE, 2] is the first stock's close on the third day.
#
# The examples in the docstrings use this small cube of 2 stocks and 2 days:
#   small = np.array([[[10.0, 20.0], [15.0, 30.0]],       stock 0: opens 10, 20; closes 15, 30
#                     [[100.0, 100.0], [150.0, 50.0]]])   stock 1: opens 100, 100; closes 150, 50


def average_per_stock(cube: np.ndarray) -> np.ndarray:
    """Return each stock's average open and average close over all the days.

    Args:
        cube: prices, with shape (stocks, 2, days).

    Returns:
        An array with shape (stocks, 2): one row per stock, with its average
        open and then its average close.

    Example:
        average_per_stock(small)
    returns
        array([[ 15. ,  22.5],
               [100. , 100. ]])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def basket_return_per_day(cube: np.ndarray) -> np.ndarray:
    """Return, for each day, the average of the stocks' returns on that day.

    A stock's return on a day is close / open - 1.

    Args:
        cube: prices, with shape (stocks, 2, days).

    Returns:
        An array with shape (days,): one number per day.

    Example. On the first day both stocks gain 50%. On the second day one
    gains 50% and the other loses 50%:
        basket_return_per_day(small)
    returns
        array([0.5, 0. ])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
def load_cube() -> np.ndarray:
    """Return September 2025's prices for TICKERS as a cube, built as the lecture builds threed_mat."""
    prices_df = pd.read_csv(PRICES)
    prices_df = prices_df.loc[prices_df.ticker.isin(TICKERS)]
    matrix_per_date = []
    for _, group in prices_df.groupby("date"):
        matrix_per_date.append(group.sort_values(by="ticker")[["open", "close"]].to_numpy())
    return np.stack(matrix_per_date, axis=2)


if __name__ == "__main__":
    cube = load_cube()
    print(average_per_stock(cube).round(2))
    print(basket_return_per_day(cube).round(4))
