"""
PROBLEM 1
Practises: making the date the index, so that dividing two Series matches them by date.

Task: fill in the function price_ratio.

To check your work, type:
    python p1_price_ratio.py

It should print what price_ratio returned for MSFT and AAPL in the first week of September 2025:
    date
    2025-09-02    2.199
    2025-09-03    2.119
    2025-09-04    2.118
    2025-09-05    2.065
    2025-09-08    2.094
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def price_ratio(prices_df: pd.DataFrame, first: str, second: str) -> pd.Series:
    """Return the closing price of one stock divided by that of another, date by date.

    A result that is all NaN means the two closes were matched by row number,
    not by date.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date and close.
        first: the ticker whose close is divided.
        second: the ticker whose close it is divided by.

    Returns:
        A Series whose index is the date and whose values are the first
        stock's close divided by the second stock's close on that date.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F", "KO", "F", "KO"],
                                  "date": ["2025-09-02", "2025-09-02", "2025-09-03", "2025-09-03", "2025-09-04"],
                                  "close": [66.0, 11.0, 68.0, 17.0, 67.0]})
        price_ratio(prices_df, "KO", "F")
    returns (F has no row for 2025-09-04, so that date gives NaN)
        date
        2025-09-02    6.0
        2025-09-03    4.0
        2025-09-04    NaN
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    first_week_df = prices_df[prices_df.date <= "2025-09-08"]
    print(price_ratio(first_week_df, "MSFT", "AAPL").round(3).to_string())
