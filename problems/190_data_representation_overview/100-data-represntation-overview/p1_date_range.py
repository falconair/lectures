"""
PROBLEM 1: look prices up by date, not by position in the array

YOUR TASK
    Change the lines below the line marked YOUR WORK. Do not change anything above it.
    Write your code directly below that line, not inside a function.
    Your work is checked by running the program with several tickers and dates,
    including some that are not listed here. Each of these is checked:
    - the trading days counted include both START and END;
    - START and END do not have to be trading days;
    - a stock with fewer trading days than the month (VIA) is counted on its own
      trading days only;
    - when no trading day falls in the range, the program prints the
      "no trading days" line shown at the end and exits with status 1 (sys.exit(1)).

THE PROGRAM
    It prints how many trading days a stock had between two dates (both dates
    included) and its average closing price over those days:
        python p1_date_range.py TICKER START END
    Dates are written YYYY-MM-DD. prices.csv holds September 2025.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p1_date_range.py AAPL 2025-09-08 2025-09-12
       prints "4 trading days". The 8th was a Monday and the 12th a Friday.
    2. python p1_date_range.py VIA 2025-09-15 2025-09-19
       prints "average close 48.42", a believable price. Compare it with VIA's
       closes on those dates (close is the sixth column):  grep VIA prices.csv
    3. python p1_date_range.py AAPL 2025-09-01 2025-09-05
       stops with a ValueError. The 1st was a holiday (Labor Day): no prices.
    The lecture's part on giving a Series a date index is the place to look.
    If you meet an AssertionError with no message: your True/False test and the
    table you use it on have different indexes. If you meet "Cannot get left slice
    bound for non-unique label": you sliced by date while the index still held
    every stock's dates.
    Leave TRADING_DAYS where it is, even if your code no longer uses it.

WHEN YOU ARE DONE, these commands behave like this
    python p1_date_range.py AAPL 2025-09-08 2025-09-12
        AAPL 2025-09-08 to 2025-09-12: 5 trading days, average close 232.62
    python p1_date_range.py VIA 2025-09-15 2025-09-19
        VIA 2025-09-15 to 2025-09-19: 5 trading days, average close 50.32
    python p1_date_range.py AAPL 2025-09-01 2025-09-05
        AAPL 2025-09-01 to 2025-09-05: 4 trading days, average close 236.92
    python p1_date_range.py VIA 2025-09-02 2025-09-05
        VIA 2025-09-02 to 2025-09-05: no trading days
    The last command exits with status 1. To see the exit status of the program
    you just ran, type:  echo $?
    A START later than END also gives the "no trading days" line, and a date typed
    without its zeros (2025-9-8) gives that line or a wrong count. You do not have to handle
    these two cases.
"""

import argparse
import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"

parser = argparse.ArgumentParser()
parser.add_argument("ticker")
parser.add_argument("start", help="first date, YYYY-MM-DD")
parser.add_argument("end", help="last date, YYYY-MM-DD")
args = parser.parse_args()

# one row per ticker per day: ticker, date, open, high, low, close, volume.
# The rows of each ticker are in date order. The dates are text, like "2025-09-02".
prices_df = pd.read_csv(PRICES)

if args.ticker not in prices_df.ticker.tolist():
    print("no data for", args.ticker)
    sys.exit(1)

# the 21 trading days of the month, oldest first, as a plain list of text dates
TRADING_DAYS = sorted(set(prices_df.date.tolist()))


# ---- YOUR WORK: everything below this line ---------------------------------
closes_v = prices_df.loc[prices_df.ticker == args.ticker, "close"].to_numpy()

first = TRADING_DAYS.index(args.start)  # position of START in the month: 0, 1, 2, ...
last = TRADING_DAYS.index(args.end)
in_range = closes_v[first:last]

print(f"{args.ticker} {args.start} to {args.end}: {len(in_range)} trading days, average close {in_range.mean():.2f}")
