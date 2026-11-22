"""
PROBLEM 4
Practises: moving one level of an index to the columns, and back again.

Task: fill in the functions to_wide and to_long.

To check your work, type:
    python p4_wide_and_long.py

It should print what to_wide returned for AAPL and MSFT on three days,
then what to_long returned for that table:
    ticker        AAPL    MSFT
    date
    2025-09-02  229.72  505.12
    2025-09-03  238.47  505.35
    2025-09-04  239.78  507.97
    date        ticker
    2025-09-02  AAPL      229.72
                MSFT      505.12
    2025-09-03  AAPL      238.47
                MSFT      505.35
    2025-09-04  AAPL      239.78
                MSFT      507.97
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def to_wide(closes: pd.Series) -> pd.DataFrame:
    """Return the closes as a table with one row per date and one column per ticker.

    Args:
        closes: closing prices, with an index of two levels: ticker, then date.

    Returns:
        A table whose index is the date, whose columns are the tickers and
        whose values are the closes.

    Example:
        closes = pd.DataFrame({"ticker": ["F", "F", "KO", "KO"],
                               "date": ["2025-09-02", "2025-09-03", "2025-09-02", "2025-09-03"],
                               "close": [11.0, 11.5, 66.0, 68.0]}).set_index(["ticker", "date"]).close
        to_wide(closes)
    returns
        ticker         F    KO
        date
        2025-09-02  11.0  66.0
        2025-09-03  11.5  68.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def to_long(closes_table: pd.DataFrame) -> pd.Series:
    """Return the closes in a table like to_wide's as one Series, one entry per date and ticker.

    Args:
        closes_table: a table whose index is the date and whose columns are the tickers.

    Returns:
        A Series with an index of two levels, date then ticker, whose values are the closes.

    Example:
        closes_table = pd.DataFrame({"F": [11.0, 11.5], "KO": [66.0, 68.0]}, index=["2025-09-02", "2025-09-03"])
        to_long(closes_table)
    returns
        2025-09-02  F     11.0
                    KO    66.0
        2025-09-03  F     11.5
                    KO    68.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    two_stocks_df = prices_df[
        prices_df.ticker.isin(["AAPL", "MSFT"]) & (prices_df.date <= "2025-09-04")
    ]
    closes = two_stocks_df.set_index(["ticker", "date"]).close
    closes_table = to_wide(closes)
    print(closes_table.to_string())
    print(to_long(closes_table).to_string())
