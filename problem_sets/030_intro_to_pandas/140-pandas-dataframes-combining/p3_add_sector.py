"""
PROBLEM 3
Practises: joining two tables on a column that has a different name in each.

Task: fill in the function add_sector.

To check your work, type:
    python p3_add_sector.py

It should print what add_sector returned for the closes of 2025-09-10. F and
GME are not in companies.csv, so they are not in the result:
      ticker   close symbol              sector
    0   AAPL  226.79   AAPL          Technology
    1   AMZN  230.33   AMZN   Consumer Cyclical
    2    JPM  300.54    JPM  Financial Services
    3     KO   67.82     KO  Consumer Defensive
    4   MSFT  500.37   MSFT          Technology
    5   NVDA  177.33   NVDA          Technology
    6   TSLA  347.79   TSLA   Consumer Cyclical
    7    XOM  112.50    XOM              Energy
"""

from pathlib import Path

import pandas as pd

# the data files sit in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
COMPANIES = Path(__file__).parent / "companies.csv"


def add_sector(day_df: pd.DataFrame, companies_df: pd.DataFrame) -> pd.DataFrame:
    """Return the rows of day_df with the columns of companies_df added to them.

    A row of day_df is matched with the row of companies_df for the same
    stock. A stock that is not in both tables is left out.

    Args:
        day_df: one row per stock, with the columns ticker and close.
        companies_df: one row per stock, with the columns symbol and sector.
            symbol holds the same values as day_df's ticker.

    Returns:
        A table with the columns ticker, close, symbol and sector.

    Example:
        day_df = pd.DataFrame({"ticker": ["F", "KO"], "close": [11.42, 67.82]})
        companies_df = pd.DataFrame({"symbol": ["KO"], "sector": ["Consumer Defensive"]})
        add_sector(day_df, companies_df)
    returns
          ticker  close symbol              sector
        0     KO  67.82     KO  Consumer Defensive
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    day_df = prices_df.loc[prices_df.date == "2025-09-10", ["ticker", "close"]].reset_index(drop=True)
    companies_df = pd.read_csv(COMPANIES)[["symbol", "sector"]]
    print(add_sector(day_df, companies_df).to_string())
