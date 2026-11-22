"""
PROBLEM 4
Practises: fixing column names with stray spaces, arithmetic on whole
columns, adding a column.

Task: fill in the functions strip_column_names and add_dollar_volume.
prices_with_spaces_in_header.csv is prices.csv with a space added to the end
of two column names, "close " and "volume ".

To check your work, type:
    python p4_dollar_volume.py

It should print four columns of the 2025-09-19 rows of what add_dollar_volume
returned:
        ticker   close     volume  dollar_volume_millions
    13    AAPL  245.50  163741300                 40198.5
    34    AMZN  231.48   97943200                 22671.9
    55       F   11.62   71676300                   832.9
    76     GME   26.08    9567600                   249.5
    97     JPM  314.78   23568600                  7418.9
    118     KO   66.43   31192900                  2072.1
    139   MSFT  517.93   52474100                 27177.9
    160   NVDA  176.67  237182100                 41903.0
    181   TSLA  426.07   93131000                 39680.3
    202    XOM  112.82   38746500                  4371.4
"""

from pathlib import Path

import pandas as pd

# the data file sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices_with_spaces_in_header.csv"


def strip_column_names(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return the table with the spaces removed from both ends of every column name.

    Args:
        prices_df: a table whose column names may start or end with spaces.

    Returns:
        The same table, with column names such as "close " changed to "close".

    Example:
        prices_df = pd.DataFrame({"ticker ": ["KO"], " close": [68.0], "volume ": [2000000]})
        strip_column_names(prices_df)
    returns
          ticker  close   volume
        0     KO   68.0  2000000
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def add_dollar_volume(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return the table with a new column, dollar_volume_millions.

    dollar_volume_millions is the value of the shares traded that day, in
    millions of dollars: close times volume, divided by 1,000,000.

    Args:
        prices_df: one row per stock per day, with the columns close and volume.

    Returns:
        The same table, with the column dollar_volume_millions added at the end.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "F"], "close": [68.0, 12.0], "volume": [2000000, 500000]})
        add_dollar_volume(prices_df)
    returns
          ticker  close   volume  dollar_volume_millions
        0     KO   68.0  2000000                   136.0
        1      F   12.0   500000                     6.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = strip_column_names(pd.read_csv(PRICES))
    prices_df = add_dollar_volume(prices_df)
    columns = ["ticker", "close", "volume", "dollar_volume_millions"]
    one_day_df = prices_df.loc[prices_df.date == "2025-09-19", columns]
    print(one_day_df.round({"dollar_volume_millions": 1}).to_string())
