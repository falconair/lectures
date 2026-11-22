"""
PROBLEM 4
Practises: turning a CSV file into a Parquet file, and reading back only some
of the columns, which Parquet can do without reading the others.

Task: fill in the functions csv_to_parquet and read_columns.

To check your work, type:
    python p4_csv_to_parquet.py

It should print the size on disk of trades.csv and of the trades.parquet that
csv_to_parquet wrote, then the first rows of what read_columns returned for the
columns ticker, price and size:
    trades.csv:     0.09 MB
    trades.parquet: 0.04 MB

    read_columns: 1000 rows; the first five:
      ticker     price  size
    0   NVDA  178.8995    23
    1   AAPL  228.0190    46
    2   AAPL  227.7301    50
    3   TSLA  355.4200    30
    4   TSLA  355.4200   100
"""

from pathlib import Path

import pandas as pd

# trades.csv sits in the same folder as this file, wherever you run it from.
# It holds the first 1,000 trades in AAPL, AMZN, MSFT, NVDA and TSLA after
# 11:00 New York time (15:00 UTC) on 2025-09-10, with all 13 columns of the
# full file.
TRADES = Path(__file__).parent / "trades.csv"


def csv_to_parquet(csv_path: str, parquet_path: str) -> None:
    """Write a CSV file as one Parquet file.

    Args:
        csv_path: the CSV file to read.
        parquet_path: the Parquet file to write. If it exists, it is replaced.

    Returns:
        Nothing: the Parquet file holds the same rows and columns as the CSV file.

    Example:
        With a file small_trades.csv that holds
            ticker,price,size,exchange
            TSLA,355.42,30,12
            AAPL,228.019,85,4
            TSLA,355.4,25,12
            NVDA,178.895,10,12
            NVDA,178.89,100,12
        csv_to_parquet("small_trades.csv", "small_trades.parquet")
    writes small_trades.parquet, and pd.read_parquet("small_trades.parquet") then
    returns
          ticker    price  size  exchange
        0   TSLA  355.420    30        12
        1   AAPL  228.019    85         4
        2   TSLA  355.400    25        12
        3   NVDA  178.895    10        12
        4   NVDA  178.890   100        12
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def read_columns(parquet_path: str, columns: list[str]) -> pd.DataFrame:
    """Read only the given columns of a Parquet file.

    Args:
        parquet_path: the Parquet file to read.
        columns: the names of the columns to read.

    Returns:
        The rows of the file with only the given columns. The other columns are
        never read.

    Example:
        With small_trades.parquet as csv_to_parquet wrote it in its example,
        read_columns("small_trades.parquet", ["ticker", "size"])
    returns
          ticker  size
        0   TSLA    30
        1   AAPL    85
        2   TSLA    25
        3   NVDA    10
        4   NVDA   100
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
PARQUET = Path(__file__).parent / "trades.parquet"


def megabytes(path: Path) -> str:
    return f"{path.stat().st_size / (1024 * 1024):.2f} MB"


if __name__ == "__main__":
    PARQUET.unlink(missing_ok=True)  # delete what an earlier run wrote
    csv_to_parquet(str(TRADES), str(PARQUET))
    print("trades.csv:    ", megabytes(TRADES))
    print("trades.parquet:", megabytes(PARQUET))
    print()
    trades_df = read_columns(str(PARQUET), ["ticker", "price", "size"])
    print("read_columns:", len(trades_df), "rows; the first five:")
    print(trades_df.head(5).to_string())
