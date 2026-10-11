"""
PROBLEM 4
Practises: finding where each group's largest value is, not what it is.

Task: fill in the function busiest_day.

To check your work, type:
    python p4_busiest_day.py

It should print what busiest_day returned for September 2025:
    ticker
    AAPL    2025-09-19
    AMZN    2025-09-19
    F       2025-09-26
    GME     2025-09-10
    JPM     2025-09-19
    KO      2025-09-03
    MSFT    2025-09-19
    NVDA    2025-09-22
    TSLA    2025-09-12
    XOM     2025-09-19
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def busiest_day(prices_df: pd.DataFrame) -> pd.Series:
    """Return, for each stock, the date on which the most shares traded.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date and volume.

    Returns:
        A Series whose index is the ticker and whose values are dates, as text.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO"],
                                  "date": ["2025-09-02", "2025-09-02", "2025-09-03"],
                                  "volume": [10, 40, 30]})
        busiest_day(prices_df)
    returns
        ticker
        F     2025-09-02
        KO    2025-09-03
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    print(busiest_day(prices_df).to_string())

# NOTES
#   The lecture uses .idxmax() on a column: it gives the index label of the
#   largest value. It works on each group of a groupby too.
