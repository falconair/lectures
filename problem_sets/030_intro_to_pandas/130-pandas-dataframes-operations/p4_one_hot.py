"""
PROBLEM 4
Practises: putting numbers into buckets (pd.cut), then one-hot encoding them.

Task: fill in the functions add_price_bucket and one_hot.

To check your work, type:
    python p4_one_hot.py

It should print what one_hot returned for 2025-09-30, after add_price_bucket
put each close in one of 3 buckets, then the columns day_df has after the calls:
             close  (11.454, 180.623]  (180.623, 349.287]  (349.287, 517.95]
    ticker
    AAPL    254.63              False                True              False
    AMZN    219.57              False                True              False
    F        11.96               True               False              False
    GME      27.28               True               False              False
    JPM     315.43              False                True              False
    KO       66.32               True               False              False
    MSFT    517.95              False               False               True
    NVDA    186.58              False                True              False
    TSLA    444.72              False               False               True
    XOM     112.75               True               False              False
    columns of day_df after the calls: close
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def add_price_bucket(day_df: pd.DataFrame, bins: int) -> pd.DataFrame:
    """Return a copy of day_df with a new column price_bucket, made with pd.cut.

    pd.cut splits the range of the close column into `bins` equal parts;
    price_bucket says which part each close is in. day_df itself must not change.

    Args:
        day_df: a table with the column close.
        bins: how many buckets to make.

    Returns:
        A new table: the columns of day_df, then price_bucket.

    Example:
        day_df = pd.DataFrame({"close": [10.0, 20.0, 30.0, 40.0]},
                              index=["F", "GME", "KO", "XOM"])
        add_price_bucket(day_df, 2)
    returns
             close  price_bucket
        F     10.0  (9.97, 25.0]
        GME   20.0  (9.97, 25.0]
        KO    30.0  (25.0, 40.0]
        XOM   40.0  (25.0, 40.0]
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def one_hot(day_df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Return a copy of day_df with column replaced by one True/False column per value.

    day_df itself must not change.

    Args:
        day_df: a table with the column `column`.
        column: the name of the column to one-hot encode.

    Returns:
        A new table: the other columns of day_df, then one column per value.

    Example:
        day_df = pd.DataFrame({"close": [10.0, 40.0, 20.0],
                               "price_level": ["low", "high", "low"]},
                              index=["F", "XOM", "GME"])
        one_hot(day_df, "price_level")
    returns
             close   high    low
        F     10.0  False   True
        XOM   40.0   True  False
        GME   20.0  False   True
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    # one row per stock on 2025-09-30, with the ticker as the index
    day_df = prices_df.loc[prices_df.date == "2025-09-30"].set_index("ticker")
    day_df = day_df[["close"]]
    encoded_df = one_hot(add_price_bucket(day_df, 3), "price_bucket")
    print(encoded_df.to_string())
    print("columns of day_df after the calls:", ", ".join(day_df.columns))

# NOTES
#   pd.concat([a, b], axis=1) puts two tables side by side, matching rows by index.
#   This lecture uses it once; the next lecture teaches it.
