"""
PROBLEM 3
Practises: going through a file one chunk of rows at a time, so that the whole
file is never in memory, and adding up the results of the chunks.

Task: fill in the functions total_shares and shares_by_ticker.

To check your work, type:
    python p3_shares_in_chunks.py 300

It should print what total_shares and shares_by_ticker returned when they read
trades.csv 300 rows at a time:
    total_shares: 72860

    shares_by_ticker:
    ticker
    AAPL     4488
    AMZN     1667
    MSFT     1400
    NVDA    37818
    TSLA    27487
"""

import sys
from pathlib import Path

import pandas as pd

# trades.csv sits in the same folder as this file, wherever you run it from.
# It holds the first 1,000 trades in AAPL, AMZN, MSFT, NVDA and TSLA after
# 11:00 New York time (15:00 UTC) on 2025-09-10. The column size is the
# number of shares traded.
TRADES = Path(__file__).parent / "trades.csv"


def total_shares(path: str, chunk_size: int) -> int:
    """Return the number of shares traded in a trades file, reading it a chunk at a time.

    Args:
        path: a CSV file of trades, with the column size.
        chunk_size: how many rows to read at a time.

    Returns:
        The sum of the column size over the whole file.

    Example:
        With a file small_trades.csv that holds
            ticker,price,size,exchange
            TSLA,355.42,30,12
            AAPL,228.019,85,4
            TSLA,355.4,25,12
            NVDA,178.895,10,12
            NVDA,178.89,100,12
        total_shares("small_trades.csv", 2)
    returns
        250
    It reads three chunks: the first two rows, the next two, and the last row.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def shares_by_ticker(path: str, chunk_size: int) -> pd.Series:
    """Return the number of shares traded in each stock, reading the file a chunk at a time.

    Args:
        path: a CSV file of trades, with the columns ticker and size.
        chunk_size: how many rows to read at a time.

    Returns:
        The sum of size for each ticker over the whole file, with the ticker as
        the index, in alphabetical order.

    Example:
        With small_trades.csv as in the example of total_shares,
        shares_by_ticker("small_trades.csv", 2)
    returns
        ticker
        AAPL     85
        NVDA    110
        TSLA     55
    TSLA's 55 shares are in the first chunk (30) and the second (25); NVDA's
    110 are in the second (10) and the third (100).
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    chunk_size = int(sys.argv[1])
    print("total_shares:", total_shares(str(TRADES), chunk_size))
    print()
    print("shares_by_ticker:")
    print(shares_by_ticker(str(TRADES), chunk_size).to_string())

# NOTES
#   pd.concat(list_of_series) puts the Series one after another, so a ticker
#   appears once for each chunk it is in; .groupby(level=0).sum() then adds up
#   the rows that have the same index label.
