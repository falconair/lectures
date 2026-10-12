"""
PROBLEM 2
Practises: putting two tables side by side, matched by their index.

Task: fill in the function side_by_side.

To check your work, type:
    python p2_side_by_side.py

It should print what side_by_side returned for the closes and the volumes of 2025-09-10:
             close     volume
    ticker
    AAPL    226.79   83440800
    AMZN    230.33   60907700
    F        11.42   47021300
    GME      24.37   46254000
    JPM     300.54    7787300
    KO       67.82   16041900
    MSFT    500.37   21611800
    NVDA    177.33  226852000
    TSLA    347.79   72121700
    XOM     112.50   15837600
"""

from pathlib import Path

import pandas as pd

# the data files sit in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
COMPANIES = Path(__file__).parent / "companies.csv"


def side_by_side(closes_df: pd.DataFrame, volumes_df: pd.DataFrame) -> pd.DataFrame:
    """Return one table with the columns of closes_df, then the columns of volumes_df.

    Rows are matched by their index, not by their position.

    Args:
        closes_df: a table whose index is the ticker.
        volumes_df: another table whose index is the ticker. Its rows may be in a different order.

    Returns:
        A table with one row per ticker and the columns of both tables.

    Example:
        closes_df = pd.DataFrame({"close": [67.82, 11.42]}, index=["KO", "F"])
        volumes_df = pd.DataFrame({"volume": [47021300, 16041900]}, index=["F", "KO"])
        side_by_side(closes_df, volumes_df)
    returns
            close    volume
        KO  67.82  16041900
        F   11.42  47021300
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    day_df = prices_df.loc[prices_df.date == "2025-09-10"].set_index("ticker")
    closes_df = day_df[["close"]]
    volumes_df = day_df[["volume"]].sort_values("volume")  # in a different order from closes_df
    print(side_by_side(closes_df, volumes_df).to_string())
