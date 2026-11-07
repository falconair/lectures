"""
PROBLEM 1
Practises: turning long data into a wide table (dates down, tickers across), with pivot.

Task: fill in the function close_matrix.

To check your work, type:
    python p1_close_matrix.py AAPL F NVDA

It should print the first 5 rows of what close_matrix returned, for those three tickers:
    ticker        AAPL      F    NVDA
    date
    2025-09-02  229.72  11.72  170.78
    2025-09-03  238.47  11.62  170.62
    2025-09-04  239.78  11.68  171.66
    2025-09-05  239.69  11.74  167.02
    2025-09-08  237.88  11.69  168.31
"""

import argparse
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def close_matrix(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return the closing prices as a table with one row per date and one column per ticker.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date and close.

    Returns:
        A table whose index is the date and whose columns are the tickers.
        Each value is that stock's close on that date.

    Example:
        prices_df = pd.DataFrame({"ticker": ["F", "F", "KO", "KO"],
                                  "date": ["2025-09-02", "2025-09-03", "2025-09-02", "2025-09-03"],
                                  "close": [11.5, 11.75, 69.0, 69.25]})
        close_matrix(prices_df)
    returns
        ticker          F     KO
        date
        2025-09-02  11.50  69.00
        2025-09-03  11.75  69.25
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tickers", nargs="+")
    args = parser.parse_args()

    prices_df = pd.read_csv(PRICES)
    print(close_matrix(prices_df)[args.tickers].head().to_string())
