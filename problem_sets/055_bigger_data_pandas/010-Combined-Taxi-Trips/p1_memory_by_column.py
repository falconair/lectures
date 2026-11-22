"""
PROBLEM 1
Practises: measuring the memory each column takes, and storing a column that
has few different values as a category.

Task: fill in the functions memory_by_column and to_categories.

To check your work, type:
    python p1_memory_by_column.py ticker conditions

It should print the megabytes each column takes before and after to_categories
made ticker and conditions categories (this is the server; on your laptop the
two text columns may take a little more or less: Python versions store text
differently):
                           before  after
    ticker                  0.051  0.001
    conditions              0.047  0.001
    correction              0.008  0.008
    exchange                0.008  0.008
    id                      0.008  0.008
    participant_timestamp   0.008  0.008
    price                   0.008  0.008
    sequence_number         0.008  0.008
    sip_timestamp           0.008  0.008
    size                    0.008  0.008
    tape                    0.008  0.008
    trf_id                  0.008  0.008
    trf_timestamp           0.008  0.008
    total                   0.181  0.087
"""

import sys
from pathlib import Path

import pandas as pd

# trades.csv sits in the same folder as this file, wherever you run it from.
# It holds the first 1,000 trades in AAPL, AMZN, MSFT, NVDA and TSLA after
# 11:00 New York time (15:00 UTC) on 2025-09-10, with all 13 columns of the
# full file. They took 2.2 seconds: the full file has 121 million trades.
TRADES = Path(__file__).parent / "trades.csv"


def memory_by_column(trades_df: pd.DataFrame) -> pd.Series:
    """Return the megabytes each column takes in memory, largest first.

    Args:
        trades_df: any table.

    Returns:
        The megabytes each column takes, counting the text inside each text
        column, with the column names as the index. The index of the table is
        not counted.

    Example:
        trades_df = pd.DataFrame({"ticker": ["TSLA", "AAPL"] * 50_000,
                                  "price": [355.42, 228.019] * 50_000})
        memory_by_column(trades_df)
    returns, on the server
        ticker    5.054474
        price     0.762939
    price takes 8 bytes for each of its 100,000 numbers. If ticker shows
    0.762939 as well, the text inside it was not counted.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def to_categories(trades_df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Return a copy of the table with the given columns stored as categories.

    Args:
        trades_df: any table. It is left unchanged.
        columns: the names of the columns to store as categories.

    Returns:
        A new table with the same values, in which each of the given columns has
        the type category.

    Example:
        trades_df = pd.DataFrame({"ticker": ["TSLA", "AAPL", "TSLA"],
                                  "price": [355.42, 228.019, 355.40]})
        to_categories(trades_df, ["ticker"])
    returns
          ticker    price
        0   TSLA  355.420
        1   AAPL  228.019
        2   TSLA  355.400
    whose .dtypes are
        ticker    category
        price      float64
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    trades_df = pd.read_csv(TRADES)
    before = memory_by_column(trades_df)
    after = memory_by_column(to_categories(trades_df, sys.argv[1:]))
    table = pd.DataFrame({"before": before, "after": after}).loc[before.index]
    table.loc["total"] = table.sum()
    print(table.to_string(float_format="{:.3f}".format))

# NOTES
#   memory_usage gives bytes. To turn bytes into megabytes, divide by
#   1024 * 1024, as the lecture does.
