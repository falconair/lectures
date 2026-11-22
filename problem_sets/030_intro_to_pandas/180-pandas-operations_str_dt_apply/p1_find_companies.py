"""
PROBLEM 1
Practises: string operations on a whole column, with .str.

Task: fill in the function find_companies.

To check your work, type:
    python p1_find_companies.py corp

It should print what find_companies returned:
    symbol                 company     sector
      MSFT   Microsoft Corporation Technology
      NVDA      NVIDIA Corporation Technology
       XOM Exxon Mobil Corporation     Energy
"""

import sys
from pathlib import Path

import pandas as pd

# companies.csv sits in the same folder as this file, wherever you run it from
COMPANIES = Path(__file__).parent / "companies.csv"


def find_companies(companies_df: pd.DataFrame, word: str) -> pd.DataFrame:
    """Return the companies whose name contains word, whatever its case.

    Args:
        companies_df: one row per company, with the columns symbol, company
            and sector.
        word: the text to look for, such as "corp" or "NVIDIA".

    Returns:
        The rows of companies_df whose company contains word, in upper or
        lower case.

    Example:
        companies_df = pd.DataFrame({"symbol": ["KO", "MSFT"],
                                     "company": ["Coca-Cola Company (The)", "Microsoft Corporation"],
                                     "sector": ["Consumer Defensive", "Technology"]})
        find_companies(companies_df, "COMPANY")
    returns
          symbol                  company              sector
        0     KO  Coca-Cola Company (The)  Consumer Defensive
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    word = sys.argv[1]
    companies_df = pd.read_csv(COMPANIES)
    print(find_companies(companies_df, word).to_string(index=False))
