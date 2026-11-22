"""
PROBLEM 2
Practises: turning text into dates with pd.to_datetime, then taking a part of
each date with .dt.

Task: fill in the function weekday_volume.

To check your work, type:
    python p2_weekday_volume.py AAPL

It should print what weekday_volume returned for AAPL in September 2025, in
millions of shares, Monday first:
    weekday
    Monday       59.3
    Tuesday      54.4
    Wednesday    59.7
    Thursday     49.3
    Friday       80.1
"""

import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def weekday_volume(prices_df: pd.DataFrame) -> pd.Series:
    """Return the average volume on each day of the week.

    Args:
        prices_df: one row per day for one stock, with the columns date and
            volume. date is text, such as "2025-09-02".

    Returns:
        A Series whose index is the name of the day of the week, such as
        "Tuesday", and whose values are the average volume on those days.

    Example:
        prices_df = pd.DataFrame({"date": ["2025-09-08", "2025-09-09", "2025-09-15"],
                                  "volume": [10, 40, 30]})
        weekday_volume(prices_df)
    returns
        weekday
        Monday     20.0
        Tuesday    40.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    ticker = sys.argv[1]
    prices_df = pd.read_csv(PRICES)
    stock_df = prices_df[prices_df.ticker == ticker]
    volume = weekday_volume(stock_df).reindex(WEEKDAYS)
    print((volume / 1e6).round(1).to_string())

# NOTES
#   The lecture uses .dt.year. .dt.day_name() works the same way and gives the
#   name of the day, such as "Monday".
