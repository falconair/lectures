"""
PROBLEM 2
Practises: choosing entries of a Series with a True/False test.

Task: fill in the function above.

To check your work, type:
    python p2_above.py 200

It should print what above returned: the stocks that closed above 200 on 2025-09-10:
    AAPL    226.79
    AMZN    230.33
    JPM     300.54
    MSFT    500.37
    TSLA    347.79
"""

import sys

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def above(closes: pd.Series, price: float) -> pd.Series:
    """Return the entries of closes that are higher than price.

    Args:
        closes: closing prices, with the ticker as the index.
        price: the price to compare with.

    Returns:
        A Series with only the entries above price, in the order they had in closes.

    Example:
        closes = pd.Series([67.82, 11.42, 300.54], index=["KO", "F", "JPM"])
        above(closes, 50.0)
    returns
        KO      67.82
        JPM    300.54
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    day_df = prices_df.loc[prices_df.date == "2025-09-10"]
    closes = pd.Series(day_df.close.tolist(), index=day_df.ticker.tolist())
    print(above(closes, float(sys.argv[1])).to_string())
