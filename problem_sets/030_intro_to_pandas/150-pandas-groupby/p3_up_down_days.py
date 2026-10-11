"""
PROBLEM 3
Practises: grouping by two columns, then moving one of them to the columns.

Task: fill in the function up_down_days.

To check your work, type:
    python p3_up_down_days.py

It should print what up_down_days returned for September 2025:
    direction  down  up
    ticker
    AAPL         10  11
    AMZN         12   9
    F            12   9
    GME           8  13
    JPM           9  12
    KO           11  10
    MSFT         11  10
    NVDA          7  14
    TSLA          9  12
    XOM           9  12
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def up_down_days(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return how many up days and how many down days each stock had.

    Args:
        prices_df: one row per stock per day, with the columns ticker and
            direction. direction is "up" or "down".

    Returns:
        A table whose index is the ticker, with one column per direction:
        down and up. Each value is a number of days.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO", "F", "KO"],
                                  "direction": ["up", "down", "up", "up", "down"]})
        up_down_days(prices_df)
    returns
        direction  down  up
        ticker
        F             1   1
        KO            1   2
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    # a day is "up" when the stock closed above its opening price
    prices_df["direction"] = (prices_df.close > prices_df.open).map({True: "up", False: "down"})
    print(up_down_days(prices_df).to_string())

# NOTES
#   Not in the lecture: .size() counts the rows of each group, as .count() does,
#   but gives one number per group and not one per column.
