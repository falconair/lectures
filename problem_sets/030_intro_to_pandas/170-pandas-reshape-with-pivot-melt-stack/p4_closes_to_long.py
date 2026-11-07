"""
PROBLEM 4
Practises: turning a wide table back into long data, with melt.

Task: fill in the function closes_to_long.

To check your work, type:
    python p4_closes_to_long.py 2025-09-10

It should print the rows of what closes_to_long returned for that date:
          date ticker  close
    2025-09-10   AAPL 226.79
    2025-09-10   AMZN 230.33
    2025-09-10      F  11.42
    2025-09-10    GME  24.37
    2025-09-10    JPM 300.54
    2025-09-10     KO  67.82
    2025-09-10   MSFT 500.37
    2025-09-10   NVDA 177.33
    2025-09-10   TSLA 347.79
    2025-09-10    XOM 112.50
"""

import argparse
from pathlib import Path

import pandas as pd

# closes_wide.csv sits in the same folder as this file, wherever you run it from.
# It holds September 2025's closes laid out as a Bloomberg sheet is: one row per
# date, one column per ticker.
CLOSES_WIDE = Path(__file__).parent / "closes_wide.csv"


def closes_to_long(closes_wide_df: pd.DataFrame) -> pd.DataFrame:
    """Return the closes as long data: one row per stock per date.

    Args:
        closes_wide_df: a column date, then one column per ticker holding its closes.

    Returns:
        A table with three columns: date, ticker and close.

    Example:
        closes_wide_df = pd.DataFrame({"date": ["2025-09-02", "2025-09-03"],
                                       "F": [11.5, 11.75], "KO": [69.0, 69.25]})
        closes_to_long(closes_wide_df)
    returns
                 date ticker  close
        0  2025-09-02      F  11.50
        1  2025-09-03      F  11.75
        2  2025-09-02     KO  69.00
        3  2025-09-03     KO  69.25
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("date")
    args = parser.parse_args()

    closes_wide_df = pd.read_csv(CLOSES_WIDE)
    closes_df = closes_to_long(closes_wide_df)
    print(closes_df.loc[closes_df["date"] == args.date].to_string(index=False))
