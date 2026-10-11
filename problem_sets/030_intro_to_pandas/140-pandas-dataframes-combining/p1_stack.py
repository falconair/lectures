"""
PROBLEM 1
Practises: putting one table under another.

Task: fill in the function stack.

To check your work, type:
    python p1_stack.py

It should print what stack returned for two tables of KO's closes:
             date  close
    0  2025-09-02  69.06
    1  2025-09-03  68.99
    2  2025-09-04  68.25
    3  2025-09-05  67.96
"""

from pathlib import Path

import pandas as pd

# the data files sit in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
COMPANIES = Path(__file__).parent / "companies.csv"


def stack(first_df: pd.DataFrame, second_df: pd.DataFrame) -> pd.DataFrame:
    """Return one table: the rows of first_df, then the rows of second_df.

    Args:
        first_df: a table.
        second_df: a table with the same columns.

    Returns:
        A table with those columns and all the rows of both, first_df's first.

    Example:
        first_df = pd.DataFrame({"date": ["2025-09-02"], "close": [69.06]})
        second_df = pd.DataFrame({"date": ["2025-09-03"], "close": [68.99]})
        stack(first_df, second_df)
    returns
                 date  close
        0  2025-09-02  69.06
        0  2025-09-03  68.99
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    ko_df = prices_df.loc[prices_df.ticker == "KO", ["date", "close"]].reset_index(drop=True)
    print(stack(ko_df[:2], ko_df[2:4]).to_string())
