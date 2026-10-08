"""
PROBLEM 2: take each average along the correct axis of the array

YOUR TASK
    Change the lines below the line marked YOUR WORK. Do not change anything above it.
    Write your code directly below that line, not inside a function.
    Your work is checked by running the program with several values of DAYS,
    including some that are not listed here. Each of these is checked:
    - each stock's average open and average close;
    - the basket's best day and worst day, with the basket's return on each.
    The grader also reads your code for one thing that no program checks:
    - a comment above each of the two .mean() calls with: the shape going in, the
      shape coming out, and what each dimension counts (stocks, kinds of price,
      days). You may print .shape while you work; remove those prints at the end.
    The line that works out `returns` is correct. Do not change it.

THE PROGRAM
    It holds prices for five stocks in a 3-dimensional numpy array, built the way
    the lecture builds threed_mat. It uses the first DAYS trading days of
    September 2025 (DAYS is a number from 1 to 21; 21 is the whole month):
        python p2_axis.py DAYS
    It prints (a) each stock's average opening and average closing price over those
    days, and (b) the best and the worst day of a basket that holds the same dollar
    amount of each stock. In this program a stock's return on a day is close / open - 1, and
    the basket's return on a day is the average of the five stocks' returns.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p2_axis.py 21
       prints   AAPL  average open   229.49   average close   237.84
       and python p2_axis.py 2 prints the same line (and then stops, see 3).
       Compare with the file (open is the third column, close the sixth):
           grep AAPL prices.csv | head -3
    2. python p2_axis.py 21 says the basket's best day was 2025-09-05 and its worst
       2025-09-04. Whatever DAYS is, the program never names a day later than
       2025-09-08.
    3. python p2_axis.py 3 stops with an IndexError. So do 1 and 2.

WHEN YOU ARE DONE, these commands behave like this
    python p2_axis.py 21
        AAPL  average open   241.90   average close   242.49
        JPM   average open   306.95   average close   307.54
        KO    average open    67.11   average close    67.04
        TSLA  average open   394.12   average close   395.89
        XOM   average open   113.14   average close   113.09
        basket best day  2025-09-11 +1.67%
        basket worst day 2025-09-18 -0.96%
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"

TICKERS = ["AAPL", "JPM", "KO", "TSLA", "XOM"]  # in alphabetical order, as the rows of the array will be
OPEN, CLOSE = 0, 1  # positions of the two kinds of price along dimension 1

parser = argparse.ArgumentParser()
parser.add_argument("days", type=int, help="how many trading days to use: 1 to 21")  # type=int: a number, not text
args = parser.parse_args()
if args.days < 1 or args.days > 21:
    print("DAYS must be a number from 1 to 21")
    sys.exit(1)

prices_df = pd.read_csv(PRICES)
prices_df = prices_df.loc[prices_df.ticker.isin(TICKERS)]
first_days = sorted(set(prices_df.date.tolist()))[: args.days]  # the first DAYS trading days of the month
prices_df = prices_df.loc[prices_df.date.isin(first_days)]

# Build the 3-dimensional array exactly as the lecture builds threed_mat:
# one small matrix per date (a row per stock, columns open and close), then stack them.
DATES = []
matrix_per_date = []
for date, group in prices_df.groupby("date"):
    DATES.append(date)
    matrix_per_date.append(group.sort_values(by="ticker")[["open", "close"]].to_numpy())
cube = np.stack(matrix_per_date, axis=2)
# cube.shape is (5, 2, DAYS):
#   dimension 0 has 5 entries: the stocks, in the order of TICKERS
#   dimension 1 has 2 entries: open, close
#   dimension 2 has DAYS entries: the trading days, in the order of DATES
# so cube[0, CLOSE, 2] is AAPL's close on the third trading day.


def print_best_and_worst(basket_returns):
    """Print the best and the worst day, given a vector with the basket's return on each day.

    argmax and argmin are not in the lecture: they give the POSITION of the largest
    and of the smallest number in a vector.
    """
    best = basket_returns.argmax()
    worst = basket_returns.argmin()
    print(f"basket best day  {DATES[best]} {basket_returns[best]:+.2%}")
    print(f"basket worst day {DATES[worst]} {basket_returns[worst]:+.2%}")


# ---- YOUR WORK: everything below this line ---------------------------------
# a. each stock's average open and average close over the DAYS days
averages = cube.mean(axis=1)
for i in range(len(TICKERS)):
    print(f"{TICKERS[i]:5s} average open {averages[i, OPEN]:8.2f}   average close {averages[i, CLOSE]:8.2f}")

# b. the basket's return on each day, then its best and worst day
returns = cube[:, CLOSE, :] / cube[:, OPEN, :] - 1  # each stock's open-to-close return on each day
basket_returns = returns.mean(axis=1)
print_best_and_worst(basket_returns)
