"""
PROBLEM 3
Practises: broadcasting, where the shapes decide whether a subtraction works.

Task: fill in the functions subtract_column_means and subtract_row_means.

To check your work, type:
    python p3_subtract_means.py

It should print the first three rows of what each function returned:
    subtract_column_means:
                  AAPL       F      KO    NVDA    TSLA
    2025-09-03  0.0328 -0.0096  0.0010 -0.0056 -0.0011
    2025-09-04  0.0002  0.0041 -0.0087  0.0015 -0.0022
    2025-09-05 -0.0057  0.0040 -0.0022 -0.0317  0.0209
    subtract_row_means:
                  AAPL       F      KO    NVDA    TSLA
    2025-09-03  0.0297 -0.0169 -0.0094 -0.0093  0.0060
    2025-09-04  0.0016  0.0013 -0.0146  0.0022  0.0094
    2025-09-05 -0.0023  0.0032 -0.0062 -0.0290  0.0344
"""

from pathlib import Path

import numpy as np
import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
TICKERS = ["AAPL", "F", "KO", "NVDA", "TSLA"]


def subtract_column_means(returns: np.ndarray) -> np.ndarray:
    """Subtract from each column the mean of that column.

    Write it without a loop: one of the tests fails if your functions have a for
    loop, a while loop or a list comprehension.

    Args:
        returns: a matrix of daily returns, one row per date, one column per ticker.

    Returns:
        A matrix of the same shape: how far each return is from that stock's own
        average return. Each column of the result averages to 0.

    Example:
        returns = np.array([[0.5, 0.0],
                            [0.25, 0.5],
                            [-0.25, 0.25],
                            [0.5, -0.25]])
        subtract_column_means(returns)
    returns
        array([[ 0.25 , -0.125],
               [ 0.   ,  0.375],
               [-0.5  ,  0.125],
               [ 0.25 , -0.375]])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def subtract_row_means(returns: np.ndarray) -> np.ndarray:
    """Subtract from each row the mean of that row.

    Write it without a loop: one of the tests fails if your functions have a for
    loop, a while loop or a list comprehension. The row means have to be a matrix
    with one column before you subtract, as in the lecture's
    np.ones((5, 5)) + np.ones((5, 1)).

    Args:
        returns: a matrix of daily returns, one row per date, one column per ticker.

    Returns:
        A matrix of the same shape: how far each return is from the average return
        of all the stocks that day. Each row of the result averages to 0.

    Example:
        returns = np.array([[0.5, 0.0],
                            [0.25, 0.5],
                            [-0.25, 0.25],
                            [0.5, -0.25]])
        subtract_row_means(returns)
    returns
        array([[ 0.25 , -0.25 ],
               [-0.125,  0.125],
               [-0.25 ,  0.25 ],
               [ 0.375, -0.375]])
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    closes_df = prices_df.pivot(index="date", columns="ticker", values="close")[TICKERS]
    closes = closes_df.to_numpy()
    returns = closes[1:] / closes[:-1] - 1  # the first date has no return
    dates = closes_df.index[1:].tolist()
    column_result = subtract_column_means(returns.copy())
    row_result = subtract_row_means(returns.copy())
    print("subtract_column_means:")
    print(pd.DataFrame(column_result, dates, TICKERS).head(3).round(4).to_string())
    print("subtract_row_means:")
    print(pd.DataFrame(row_result, dates, TICKERS).head(3).round(4).to_string())

# NOTES
#   Not in the lecture: .mean() is the average, and it takes an axis, as .sum() does.
