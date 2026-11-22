"""
PROBLEM 2
Practises: reading only the columns you need from a CSV file, each with the
type you choose.

Task: fill in the function read_trades.

To check your work, type:
    python p2_read_columns.py

It should print the first rows of what read_trades returned for the four
columns in COLUMN_TYPES, their types, and their memory beside that of all 13
columns (this is the server; on your laptop the memory may be a little
different):
      ticker     price        sip_timestamp  size
    0   NVDA  178.8995  1757516400010258122    23
    1   AAPL  228.0190  1757516400014966091    46
    2   AAPL  227.7301  1757516400017620520    50
    3   TSLA  355.4200  1757516400018255966    30
    4   TSLA  355.4200  1757516400018257240   100

    ticker           category
    price             float64
    sip_timestamp       int64
    size                int64

    memory of these columns: 25569 bytes
    memory of all 13 columns: 190435 bytes
"""

from pathlib import Path

import pandas as pd

# trades.csv sits in the same folder as this file, wherever you run it from.
# It holds the first 1,000 trades in AAPL, AMZN, MSFT, NVDA and TSLA after
# 11:00 New York time (15:00 UTC) on 2025-09-10, with all 13 columns of the
# full file.
TRADES = Path(__file__).parent / "trades.csv"


def read_trades(path: str, column_types: dict[str, str]) -> pd.DataFrame:
    """Read only the given columns of a CSV file, each as the given type.

    Args:
        path: the CSV file to read.
        column_types: the name of each column to read, and its type as pandas
            writes it ("category", "float64", "int64").

    Returns:
        A table with only the given columns, each of the given type. The other
        columns are never put in a table.

    Example:
        With a file small_trades.csv that holds
            ticker,price,size,exchange
            TSLA,355.42,30,12
            AAPL,228.019,85,4
            TSLA,355.4,25,12
            NVDA,178.895,10,12
            NVDA,178.89,100,12
        read_trades("small_trades.csv", {"ticker": "category", "size": "int64"})
    returns
          ticker  size
        0   TSLA    30
        1   AAPL    85
        2   TSLA    25
        3   NVDA    10
        4   NVDA   100
    whose .dtypes are
        ticker    category
        size         int64
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
COLUMN_TYPES = {"ticker": "category", "price": "float64", "sip_timestamp": "int64", "size": "int64"}

if __name__ == "__main__":
    trades_df = read_trades(str(TRADES), COLUMN_TYPES)
    print(trades_df.head(5).to_string())
    print()
    print(trades_df.dtypes.to_string())
    print()
    print("memory of these columns:", trades_df.memory_usage(deep=True).sum(), "bytes")
    print("memory of all 13 columns:", pd.read_csv(TRADES).memory_usage(deep=True).sum(), "bytes")
