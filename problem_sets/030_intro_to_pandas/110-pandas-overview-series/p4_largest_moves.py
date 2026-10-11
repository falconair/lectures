"""
PROBLEM 4
Practises: combining Series operations: a calculation, the largest entries, and looking entries up by label.

Task: fill in the function largest_moves.

To check your work, type:
    python p4_largest_moves.py 3

It should print what largest_moves returned: the 3 largest moves of 2025-09-10:
    ticker
    GME    -0.0333
    AMZN   -0.0303
    AAPL   -0.0233
"""

import sys

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def largest_moves(returns: pd.Series, count: int) -> pd.Series:
    """Return the `count` returns that are largest in size, largest first.

    A fall of 3% is a larger move than a rise of 1%. Each return keeps its sign.

    Args:
        returns: one return per stock, with the ticker as the index.
        count: how many entries to return.

    Returns:
        A Series with `count` entries of returns.

    Example:
        returns = pd.Series([0.0129, -0.0333, 0.0004, -0.0303], index=["JPM", "GME", "KO", "AMZN"])
        largest_moves(returns, 2)
    returns
        GME    -0.0333
        AMZN   -0.0303
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    day_df = prices_df.loc[prices_df.date == "2025-09-10"].set_index("ticker")
    returns = (day_df.close / day_df.open - 1).round(4)  # each stock's move from the open to the close
    print(largest_moves(returns, int(sys.argv[1])).to_string())

# NOTES
#   Not in the lecture: some_series.abs() returns a Series with every minus sign removed.
