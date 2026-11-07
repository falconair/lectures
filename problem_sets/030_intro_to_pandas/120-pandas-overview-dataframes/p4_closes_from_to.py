"""
PROBLEM 4
Practises: getting rows and columns by their labels with .loc.

Task: fill in the function closes_from_to.

To check your work, type:
    python p4_closes_from_to.py 2025-09-08 2025-09-12 AAPL MSFT NVDA

It should print what closes_from_to returned:
                  AAPL    MSFT    NVDA
    2025-09-08  237.88  498.20  168.31
    2025-09-09  234.35  498.41  170.76
    2025-09-10  226.79  500.37  177.33
    2025-09-11  230.03  501.01  177.17
    2025-09-12  234.07  509.90  177.82
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def closes_from_to(
    closes_df: pd.DataFrame, first_date: str, last_date: str, tickers: list[str]
) -> pd.DataFrame:
    """Return the closes of tickers from first_date to last_date, both dates included.

    Args:
        closes_df: closing prices, with one row per date (the index, as text,
            oldest first) and one column per ticker.
        first_date: the first date, as text, "YYYY-MM-DD".
        last_date: the last date, as text, "YYYY-MM-DD".
        tickers: the columns to keep, in this order.

    Returns:
        A table with the rows from first_date to last_date and the columns tickers.

    Example:
        closes_df = pd.DataFrame({"F": [11.25, 11.5, 11.75], "KO": [67.5, 68.0, 67.0], "XOM": [114.5, 112.0, 112.5]},
                                 index=["2025-09-02", "2025-09-03", "2025-09-04"])
        closes_from_to(closes_df, "2025-09-03", "2025-09-04", ["XOM", "F"])
    returns
                      XOM      F
        2025-09-03  112.0  11.50
        2025-09-04  112.5  11.75
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    # one row per date, one column per ticker
    closes_df = prices_df.pivot(index="date", columns="ticker", values="close")
    closes_df.index.name = None
    closes_df.columns.name = None
    print(closes_from_to(closes_df, sys.argv[1], sys.argv[2], sys.argv[3:]).to_string())
