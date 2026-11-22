"""
PROBLEM 4
Practises: writing a function for one value, then running it on every value of
a column with .apply.

Task: fill in the functions side_name and side_names.

To check your work, type:
    python p4_side_names.py

It should print how many orders of 2025-09-10 had each side code, beside the
name side_names gave it:
    side  side_name
    1     buy           416
    2     sell          141
    5     sell short     11
"""

from pathlib import Path

import pandas as pd

# executions.csv sits in the same folder as this file, wherever you run it from
EXECUTIONS = Path(__file__).parent / "executions.csv"


def side_name(side: int) -> str:
    """Return the name of one FIX side code (tag 54).

    Args:
        side: 1 for a buy, 2 for a sell, 5 for a short sale.

    Returns:
        "buy", "sell" or "sell short".

    Example:
        side_name(5)
    returns
        'sell short'
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def side_names(sides: pd.Series) -> pd.Series:
    """Return the name of every side code in a column, using side_name.

    Args:
        sides: FIX side codes, each 1, 2 or 5.

    Returns:
        A Series of the same length whose values are the names.

    Example:
        side_names(pd.Series([2, 1, 5]))
    returns
        0          sell
        1           buy
        2    sell short
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    executions_df = pd.read_csv(EXECUTIONS)
    executions_df["side_name"] = side_names(executions_df.side)
    print(executions_df.groupby(["side", "side_name"]).size().to_string())
