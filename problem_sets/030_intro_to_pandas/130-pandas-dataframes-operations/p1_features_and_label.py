"""
PROBLEM 1
Practises: removing a column without changing the table you were given.

Task: fill in the function features_and_label.

To check your work, type:
    python p1_features_and_label.py

It should print the first three rows of what features_and_label returned
for 2025-09-10, where the label is each stock's close on the next day,
then the columns day_df has after the call:
    features:
              open    high     low   close    volume
    ticker
    AAPL    232.19  232.42  225.95  226.79  83440800
    AMZN    237.52  237.68  229.10  230.33  60907700
    F        11.49   11.52   11.31   11.42  47021300
    label:
    ticker
    AAPL    230.03
    AMZN    229.95
    F        11.76
    columns of day_df after the call: open, high, low, close, volume, next_close
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def features_and_label(
    day_df: pd.DataFrame, label_column: str
) -> tuple[pd.DataFrame, pd.Series]:
    """Split a table into the columns a model learns from and the column it predicts.

    day_df itself must not change: whoever called the function still needs it whole.

    Args:
        day_df: a table with label_column among its columns.
        label_column: the name of the column the model predicts.

    Returns:
        Two things: a table of every column of day_df except label_column,
        and the label_column column on its own.

    Example:
        day_df = pd.DataFrame({"open": [10.0, 20.0], "close": [10.5, 19.5]},
                              index=["KO", "F"])
        features, label = features_and_label(day_df, "close")
    gives features
            open
        KO  10.0
        F   20.0
    and label
        KO    10.5
        F     19.5
    and day_df still has the columns open and close.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    # next_close: each stock's close on the next trading day, the thing a model would predict
    # (today's high, low and close are only known at the end of today, so they cannot be the label)
    prices_df["next_close"] = prices_df.groupby("ticker")["close"].shift(-1)
    # one row per stock on 2025-09-10, with the ticker as the index
    day_df = prices_df.loc[prices_df.date == "2025-09-10"].set_index("ticker")
    day_df = day_df[["open", "high", "low", "close", "volume", "next_close"]]
    features, label = features_and_label(day_df, "next_close")
    print("features:")
    print(features.head(3).to_string())
    print("label:")
    print(label.head(3).to_string())
    print("columns of day_df after the call:", ", ".join(day_df.columns))
