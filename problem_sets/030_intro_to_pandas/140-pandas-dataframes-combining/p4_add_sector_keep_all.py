"""
PROBLEM 4
Practises: joining a column to an index, and keeping the rows that have no match.

Task: fill in the function add_sector_keep_all.

To check your work, type:
    python p4_add_sector_keep_all.py

It should print what add_sector_keep_all returned for the closes of
2025-09-10. F and GME are not in companies.csv, so their sector is missing (NaN):
      ticker   close              sector
    0   AAPL  226.79          Technology
    1   AMZN  230.33   Consumer Cyclical
    2      F   11.42                 NaN
    3    GME   24.37                 NaN
    4    JPM  300.54  Financial Services
    5     KO   67.82  Consumer Defensive
    6   MSFT  500.37          Technology
    7   NVDA  177.33          Technology
    8   TSLA  347.79   Consumer Cyclical
    9    XOM  112.50              Energy
"""

from pathlib import Path

import pandas as pd

# the data files sit in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
COMPANIES = Path(__file__).parent / "companies.csv"


def add_sector_keep_all(day_df: pd.DataFrame, sector_df: pd.DataFrame) -> pd.DataFrame:
    """Return every row of day_df, with the columns of sector_df added.

    A row of day_df is matched with the row of sector_df whose index is that
    row's ticker. A stock that is not in sector_df is kept, with a missing
    value (NaN) in the added columns.

    Args:
        day_df: one row per stock, with the columns ticker and close.
        sector_df: one row per stock, with the column sector. Its index is the ticker.

    Returns:
        A table with as many rows as day_df and the columns ticker, close and sector.

    Example:
        day_df = pd.DataFrame({"ticker": ["F", "KO"], "close": [11.42, 67.82]})
        sector_df = pd.DataFrame({"sector": ["Consumer Defensive"]}, index=["KO"])
        add_sector_keep_all(day_df, sector_df)
    returns
          ticker  close              sector
        0      F  11.42                 NaN
        1     KO  67.82  Consumer Defensive
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    day_df = prices_df.loc[prices_df.date == "2025-09-10", ["ticker", "close"]].reset_index(drop=True)
    sector_df = pd.read_csv(COMPANIES).set_index("symbol")[["sector"]]
    print(add_sector_keep_all(day_df, sector_df).to_string())
