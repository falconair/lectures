"""
PROBLEM 2
Practises: arithmetic on a whole table, one column at a time.

Task: fill in the function min_max_scale.

To check your work, type:
    python p2_min_max_scale.py

It should print the lowest and the highest value in each column of what
min_max_scale returned for September 2025:
            lowest  highest
    ticker
    AAPL       0.0      1.0
    AMZN       0.0      1.0
    F          0.0      1.0
    GME        0.0      1.0
    JPM        0.0      1.0
    KO         0.0      1.0
    MSFT       0.0      1.0
    NVDA       0.0      1.0
    TSLA       0.0      1.0
    XOM        0.0      1.0
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def min_max_scale(closes_df: pd.DataFrame) -> pd.DataFrame:
    """Scale each column so that it runs from 0 to 1 (min-max scaling).

    Each value becomes (value - its column's min) / (its column's max - its column's min).
    If a column's lowest value is not 0, the table was scaled as one block of numbers.

    Args:
        closes_df: one row per day and one column per stock, holding closing prices.

    Returns:
        A table with the same rows and columns, holding the scaled values.

    Example:
        closes_df = pd.DataFrame({"KO": [60.0, 70.0, 65.0],
                                  "MSFT": [500.0, 400.0, 600.0]})
        min_max_scale(closes_df)
    returns
            KO  MSFT
        0  0.0   0.5
        1  1.0   0.0
        2  0.5   1.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    # one row per day, one column per stock
    closes_df = prices_df.pivot(index="date", columns="ticker", values="close")
    scaled_df = min_max_scale(closes_df)
    lowest_highest_df = pd.DataFrame(
        {"lowest": scaled_df.min(), "highest": scaled_df.max()}
    )
    print(lowest_highest_df.to_string())
