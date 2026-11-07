"""
PROBLEM 2
Practises: choosing rows with a True/False test and columns with a list of their names.

Task: fill in the function heavy_volume_days.

To check your work, type:
    python p2_heavy_volume_days.py AAPL 70000000

It should print what heavy_volume_days returned: the days on which more than 70 million AAPL shares traded:
              date   close     volume
    6   2025-09-10  226.79   83440800
    13  2025-09-19  245.50  163741300
    14  2025-09-22  256.08  105517400
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def heavy_volume_days(
    prices_df: pd.DataFrame, ticker: str, min_volume: int
) -> pd.DataFrame:
    """Return the days on which more than min_volume shares of ticker traded.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date, close
            and volume, among others.
        ticker: for example "AAPL".
        min_volume: a number of shares.

    Returns:
        The rows of prices_df for ticker whose volume is above min_volume,
        in the order they had in prices_df, with only the columns date, close and volume.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO", "KO"],
                                  "date": ["2025-09-02", "2025-09-02", "2025-09-03", "2025-09-04"],
                                  "open": [67.0, 11.5, 68.0, 67.5],
                                  "close": [67.5, 11.25, 68.0, 67.0],
                                  "volume": [30, 90, 10, 50]})
        heavy_volume_days(prices_df, "KO", 20)
    returns
                 date  close  volume
        0  2025-09-02   67.5      30
        3  2025-09-04   67.0      50
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print(heavy_volume_days(prices_df, sys.argv[1], int(sys.argv[2])).to_string())
