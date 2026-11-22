"""
PROBLEM 4
Practises: window functions, a rolling mean and an exponentially weighted mean.

Task: fill in the functions moving_average and exponential_average.

To check your work, type:
    python p4_moving_averages.py AAPL 5

It should print AAPL's closes beside what moving_average and exponential_average
returned for 5 days, for the first ten trading days of September 2025:
                 close  moving_average  exponential_average
    date
    2025-09-02  229.72             NaN               229.72
    2025-09-03  238.47             NaN               232.64
    2025-09-04  239.78             NaN               235.02
    2025-09-05  239.69             NaN               236.58
    2025-09-08  237.88          237.11               237.01
    2025-09-09  234.35          238.03               236.12
    2025-09-10  226.79          235.70               233.01
    2025-09-11  230.03          233.75               232.02
    2025-09-12  234.07          232.62               232.70
    2025-09-15  236.70          232.39               234.03
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def moving_average(closes: pd.Series, days: int) -> pd.Series:
    """Return each day's moving average: the mean of its close and the days-1 before it.

    Args:
        closes: one stock's closing prices, one per trading day, oldest first.
        days: how many days each mean covers.

    Returns:
        A Series with the same index as closes. The first days-1 values are NaN,
        because there are not yet enough days before them.

    Example:
        moving_average(pd.Series([1.0, 2.0, 3.0, 4.0, 5.0]), 3)
    returns
        0    NaN
        1    NaN
        2    2.0
        3    3.0
        4    4.0
        dtype: float64
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def exponential_average(closes: pd.Series, span: int) -> pd.Series:
    """Return the exponentially weighted mean of the closes, with adjust=False.

    Args:
        closes: one stock's closing prices, one per trading day, oldest first.
        span: the span of the weights, as in the lecture: alpha = 2 / (span + 1).

    Returns:
        A Series with the same index as closes. The first value is the first close.

    Example:
        exponential_average(pd.Series([1.0, 2.0, 3.0, 4.0, 5.0]), 3)
    returns
        0    1.0000
        1    1.5000
        2    2.2500
        3    3.1250
        4    4.0625
        dtype: float64
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    ticker, days = sys.argv[1], int(sys.argv[2])
    prices_df = pd.read_csv(PRICES)
    one_stock_df = prices_df.loc[prices_df["ticker"] == ticker].copy()
    one_stock_df["date"] = pd.to_datetime(one_stock_df["date"])
    closes = one_stock_df.set_index("date")["close"]
    table_df = pd.DataFrame(
        {
            "close": closes,
            "moving_average": moving_average(closes, days),
            "exponential_average": exponential_average(closes, days),
        }
    )
    print(table_df.head(10).round(2).to_string())
