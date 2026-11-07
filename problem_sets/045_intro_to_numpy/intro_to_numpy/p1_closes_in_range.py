"""
PROBLEM 1
Practises: a mask with two conditions, joined with & or | and each in parentheses.

Task: fill in the functions closes_between and closes_outside.

To check your work, type:
    python p1_closes_in_range.py AAPL 235 240

It should print what each function returned:
    closes_between:
    [238.47 239.78 239.69 237.88 236.7  238.15 238.99 237.88]
    closes_outside:
    [229.72 234.35 226.79 230.03 234.07 245.5  256.08 254.43 252.31 256.87
     255.46 254.43 254.63]
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def closes_between(closes: np.ndarray, low: float, high: float) -> np.ndarray:
    """Return the closing prices from low to high, including low and high.

    Write it without a loop: one of the tests fails if your functions have a for
    loop, a while loop or a list comprehension.

    Args:
        closes: one stock's closing prices, one per day.
        low: the lowest price to keep.
        high: the highest price to keep.

    Returns:
        The closing prices in that range, in their original order.

    Example:
        closes = np.array([9.5, 10.0, 12.0, 14.0, 14.5])
        closes_between(closes, 10.0, 14.0)
    returns
        array([10., 12., 14.])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def closes_outside(closes: np.ndarray, low: float, high: float) -> np.ndarray:
    """Return the closing prices below low or above high.

    Write it without a loop: one of the tests fails if your functions have a for
    loop, a while loop or a list comprehension.

    Args:
        closes: one stock's closing prices, one per day.
        low: closing prices below this are kept.
        high: closing prices above this are kept.

    Returns:
        The closing prices outside that range, in their original order.

    Example:
        closes = np.array([9.5, 10.0, 12.0, 14.0, 14.5])
        closes_outside(closes, 10.0, 14.0)
    returns
        array([ 9.5, 14.5])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    ticker = sys.argv[1]
    low = float(sys.argv[2])
    high = float(sys.argv[3])
    prices_df = pd.read_csv(PRICES)
    closes = prices_df.loc[prices_df.ticker == ticker, "close"].to_numpy()
    print("closes_between:")
    print(closes_between(closes, low, high))
    print("closes_outside:")
    print(closes_outside(closes, low, high))
