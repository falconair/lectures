"""
PROBLEM 3
Practises: generating dates with pandas, here every business day between two dates.

Task: fill in the function days_without_prices.

To check your work, type:
    python p3_days_without_prices.py 2025-09-01 2025-09-30

It should print each day days_without_prices returned, with its weekday:
    2025-09-01 Monday
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def days_without_prices(
    prices_df: pd.DataFrame, start: str, end: str
) -> pd.DatetimeIndex:
    """Return the business days from start to end on which there are no prices.

    Business days are Monday to Friday. In September 2025 the only one without
    prices is Labor Day, 2025-09-01, when the market was closed.

    Args:
        prices_df: one row per stock per day, with the column date, as text.
        start: the first day, as text, such as "2025-09-01".
        end: the last day, as text.

    Returns:
        The business days from start to end, both included, on which prices_df
        has no row.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "KO", "F"],
                                  "date": ["2025-09-02", "2025-09-04", "2025-09-04"]})
        days_without_prices(prices_df, "2025-09-01", "2025-09-07")
    returns
        DatetimeIndex(['2025-09-01', '2025-09-03', '2025-09-05'], dtype='datetime64[ns]', freq=None)
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    for day in days_without_prices(prices_df, sys.argv[1], sys.argv[2]):
        print(day.date(), day.day_name())
