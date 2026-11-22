"""
PROBLEM 2
Practises: turning an index into an ordinary column, and naming the columns.

Task: fill in the function returns_table.

To check your work, type:
    python p2_returns_table.py

It should print what returns_table returned for September 2025:
      ticker  return
    0   TSLA  0.3503
    1    GME  0.1653
    2   AAPL  0.1084
    3   NVDA  0.0925
    4    JPM  0.0525
    5   MSFT  0.0254
    6      F  0.0205
    7    XOM -0.0169
    8   AMZN -0.0256
    9     KO -0.0397
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def returns_table(returns: pd.Series) -> pd.DataFrame:
    """Return the stocks' returns as a plain table, largest return first.

    Args:
        returns: each stock's return, with the ticker as the index.

    Returns:
        A table with two columns, ticker and return, and one row per stock,
        sorted from the largest return to the smallest. Its index is the
        row's position: 0, 1, 2 and so on.

    Example:
        returns = pd.Series([0.25, -0.5, 0.5], index=["KO", "F", "XOM"])
        returns_table(returns)
    returns
          ticker  return
        0    XOM    0.50
        1     KO    0.25
        2      F   -0.50
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    first_close = prices_df[prices_df.date == "2025-09-02"].set_index("ticker").close
    last_close = prices_df[prices_df.date == "2025-09-30"].set_index("ticker").close
    # the return over the month: 0.10 means the stock went up 10%
    # (without names, like the example's Series)
    returns = (last_close / first_close - 1).rename(None).rename_axis(None)
    print(returns_table(returns).round(4).to_string())
