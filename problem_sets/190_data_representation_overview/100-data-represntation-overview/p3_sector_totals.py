"""
PROBLEM 3
Practises: joining two tables without losing rows.

Task: fill in the function sector_totals.

To check your work, type:
    python p3_sector_totals.py

It should print what sector_totals returned, in billions of dollars:
    sector
    Consumer Cyclical     1029.1
    Consumer Defensive      26.2
    Energy                  39.8
    Financial Services      56.3
    Technology            1207.3
    no sector             1056.0
"""

from pathlib import Path

import pandas as pd

# both files sit in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
SECTORS = Path(__file__).parent / "sectors.csv"

NO_SECTOR = "no sector"


def sector_totals(prices_df: pd.DataFrame, sectors_df: pd.DataFrame) -> pd.Series:
    """Return the dollars traded in each sector.

    Every row of prices_df is counted once. A stock that has no sector is
    counted under NO_SECTOR.

    Args:
        prices_df: one row per stock per day, with the columns ticker and dollars.
        sectors_df: one row per stock, with the columns ticker and sector.

    Returns:
        A Series whose index is the sector and whose values are the sum of dollars.

    Example. BBB's sector is empty and CCC is not in the sectors table:
        prices_df = pd.DataFrame({"ticker": ["AAA", "BBB", "CCC"], "dollars": [1.0, 2.0, 4.0]})
        sectors_df = pd.DataFrame({"ticker": ["AAA", "BBB"], "sector": ["Energy", None]})
        sector_totals(prices_df, sectors_df)
    returns
        sector
        Energy       1.0
        no sector    6.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    prices_df["dollars"] = prices_df["close"] * prices_df["volume"]  # roughly the dollars traded that day
    sectors_df = pd.read_csv(SECTORS, usecols=["ticker", "sector"])

    totals = sector_totals(prices_df, sectors_df)
    print((totals / 1e9).round(1).to_string())

# NOTES
#   Not in the lecture: some_series.fillna("x") returns a copy of a column in which
#   every missing value (NaN) is replaced by "x".
