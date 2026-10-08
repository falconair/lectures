"""
PROBLEM 3: make the sector totals add up to the total of the whole file

YOUR TASK
    Change the function sector_totals, below the line marked YOUR WORK. Do not
    change anything else, and keep the function's name and its two arguments.
    Your work is checked by running the program, and by calling sector_totals
    with other small tables. Each of these is checked:
    - the sector totals add up to the total of the whole table of prices;
    - a stock with no row in the sectors table is counted under the name in NO_SECTOR;
    - a stock whose sector is empty in the sectors table is counted there too;
    - the totals of the other sectors do not change.

THE PROGRAM
    It prints the dollars traded in each sector in September 2025 and each sector's
    share. It joins two tables, as the lecture does: prices.csv (one row per stock
    per day) and sectors.csv (one row per stock, with the sector of that stock).

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p3_sector_totals.py
       Read the last two lines. The sectors add up to 2,358.7 billion dollars, but
       the file holds 3,414.7 billion. There is no error and no warning.
    Those two lines are the check that the parts add up to the whole. They are
    already written: you add no code for that check.
    To see where rows and dollars are lost, add this inside the function, after
    the merge, and remove it when you have finished:
        print(len(prices_df), len(merged_df), merged_df["dollars"].sum())
    The lecture's merge call differs from this one (how="left" keeps every row of
    the table on the left of .merge, matched or not). name_missing is written for
    you above the YOUR WORK line; you decide which table to use it on. One fact the lecture does not give: pandas reads an empty cell
    of a csv file as "missing" and prints it as NaN.

WHEN YOU ARE DONE, these commands behave like this
    python p3_sector_totals.py
        Technology              1,207.3 bn   35.4%
        no sector               1,056.0 bn   30.9%
        Consumer Cyclical       1,029.1 bn   30.1%
        Financial Services         56.3 bn    1.6%
        Energy                     39.8 bn    1.2%
        Consumer Defensive         26.2 bn    0.8%
        sum of the lines above  3,414.7 bn
        whole file              3,414.7 bn
    python -i p3_sector_totals.py
    -i runs the program and then stops at a >>> prompt, where you can use its
    functions. Type these three lines there:
        p = pd.DataFrame({"ticker": ["AAA", "BBB", "CCC"], "dollars": [1.0, 2.0, 4.0]})
        s = pd.DataFrame({"ticker": ["AAA", "BBB"], "sector": ["Energy", None]})
        sector_totals(p, s)
    The answer is a Series, printed as four lines: a header, the rows  Energy 1.0
    and  no sector 6.0,  and a last line that starts with Name. Leave with exit().
"""

from pathlib import Path

import pandas as pd

# both files sit in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
SECTORS = Path(__file__).parent / "sectors.csv"

NO_SECTOR = "no sector"


def name_missing(column):
    """Return a copy of a column in which every missing value is replaced by NO_SECTOR.

    fillna is not in the lecture: it fills in the missing values (NaN) of a column.
    Use it like this:   some_df["sector"] = name_missing(some_df["sector"])
    """
    return column.fillna(NO_SECTOR)


def print_report(totals, whole_file):
    """Print one line per sector, largest first, then the two totals that must agree.

    totals is what sector_totals returns: a Series of dollars whose index is the sector.
    """
    for sector, dollars in totals.sort_values(ascending=False).items():
        print(f"{sector:22s} {dollars / 1e9:8,.1f} bn  {dollars / whole_file:6.1%}")
    print(f"{'sum of the lines above':22s} {totals.sum() / 1e9:8,.1f} bn")
    print(f"{'whole file':22s} {whole_file / 1e9:8,.1f} bn")


# ---- YOUR WORK: everything below this line ---------------------------------
def sector_totals(prices_df, sectors_df):
    """Return the dollars traded in each sector.

    Args:
        prices_df: a row per stock per day, with at least the columns ticker and dollars.
        sectors_df: a row per stock, with at least the columns ticker and sector.

    Returns:
        A Series: its index is the sector, its values are the sum of dollars.
    """
    merged_df = prices_df.merge(sectors_df, on="ticker")
    return merged_df.groupby("sector")["dollars"].sum()


prices_df = pd.read_csv(PRICES)
prices_df["dollars"] = prices_df["close"] * prices_df["volume"]  # roughly the dollars traded that day
sectors_df = pd.read_csv(SECTORS, usecols=["ticker", "sector"])

print_report(sector_totals(prices_df, sectors_df), prices_df["dollars"].sum())
