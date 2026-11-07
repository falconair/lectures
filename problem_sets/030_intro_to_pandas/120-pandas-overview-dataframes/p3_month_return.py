"""
PROBLEM 3
Practises: getting rows by their position with .iloc, when the index labels are not 0, 1, 2, ...

Task: fill in the function month_return.

To check your work, type:
    python p3_month_return.py TSLA

It should print what month_return returned for TSLA in September 2025:
    0.3503
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def month_return(stock_df: pd.DataFrame) -> float:
    """Return the stock's return from the close of its first row to the close of its last row.

    The return is the last close divided by the first close, minus 1.

    Args:
        stock_df: one row per day for one stock, oldest first, with the column close.

    Returns:
        The return, as a number: 0.5 means the stock rose 50%.

    Example. These rows were rows 20 to 22 of a bigger table, so their labels start at 20:
        stock_df = pd.DataFrame({"close": [40.0, 50.0, 60.0]}, index=[20, 21, 22])
        month_return(stock_df)
    returns
        0.5
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    # stock_df keeps the labels its rows had in prices_df
    stock_df = prices_df.loc[prices_df.ticker == sys.argv[1]]
    print(round(month_return(stock_df), 4))
