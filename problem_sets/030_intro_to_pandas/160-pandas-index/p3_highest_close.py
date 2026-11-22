"""
PROBLEM 3
Practises: an index of two columns, and one result per value of one of them.

Task: fill in the functions index_by_ticker_and_date and highest_close.

To check your work, type:
    python p3_highest_close.py

It should print what highest_close returned for September 2025:
    ticker
    AAPL    256.87
    AMZN    238.24
    F        12.09
    GME      27.28
    JPM     316.06
    KO       69.06
    MSFT    517.95
    NVDA    186.58
    TSLA    444.72
    XOM     117.22
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def index_by_ticker_and_date(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return the same table with an index of two levels: the ticker, then the date.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date and close.

    Returns:
        The same rows, with ticker and date moved from the columns into the index.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "KO", "F"],
                                  "date": ["2025-09-02", "2025-09-03", "2025-09-02"],
                                  "close": [66.0, 68.0, 11.0]})
        index_by_ticker_and_date(prices_df)
    returns
                           close
        ticker date
        KO     2025-09-02   66.0
               2025-09-03   68.0
        F      2025-09-02   11.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def highest_close(prices_df: pd.DataFrame) -> pd.Series:
    """Return each stock's highest closing price.

    Args:
        prices_df: one row per stock per day, with an index of two levels,
            ticker then date, and the column close.

    Returns:
        A Series whose index is the ticker and whose values are the highest close.

    Example:
        prices_df = index_by_ticker_and_date(pd.DataFrame({"ticker": ["KO", "KO", "F"],
                                                           "date": ["2025-09-02", "2025-09-03", "2025-09-02"],
                                                           "close": [66.0, 68.0, 11.0]}))
        highest_close(prices_df)
    returns
        ticker
        F     11.0
        KO    68.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print(highest_close(index_by_ticker_and_date(prices_df)).to_string())
