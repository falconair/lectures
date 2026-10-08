"""
PROBLEM 4: stop the backtest from using a closing price before it was known

YOUR TASK
    Change the function strategy_returns, below the line marked YOUR WORK. Do not
    change anything else, and keep the function's name and its two arguments.
    Your work is checked by running the program with TSLA and other tickers, and by
    calling strategy_returns with made-up prices. Each of these is checked:
    - the decision to hold the stock on a day uses only closes from earlier days;
    - on a day the rule holds the stock, its return is the stock's return on that
      day, a gain or a loss. On a day it holds cash, its return is 0.0 or NaN.
    Decide what has to change. The moving average and the daily return are
    computed correctly: do not change those two lines.

THE PROGRAM
    It tests a simple trading rule on one stock for September 2025:
        python p4_backtest.py TICKER
    The rule: after the market closes, compare today's close with the average of
    the last 3 closes (the 3-day moving average). If the close is above the
    average, hold the stock from today's close to tomorrow's close. Otherwise hold
    cash, which earns nothing. The program prints one row per day, then what the
    rule earned over the month and what holding the stock all month earned.
    NaN in the table means "no value": the first day has no return, and the first
    two days have no 3-day average.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p4_backtest.py TSLA
       Look at the rows for 2025-09-24 and 2025-09-25. On the 24th the close
       (442.79) was above the average (434.28), so the rule holds TSLA from the
       close of the 24th to the close of the 25th. On the 25th TSLA fell 4.38%.
       The rule must take that loss, but the program prints a rule_return of 0.0000.
    2. The last two lines of the same run say that the rule made +44.78% and that
       holding the stock all month made +35.03%. A rule this simple that earns so
       much more than the stock is a warning. The fault is called lookahead bias.
    3. python -i p4_backtest.py F
       The program needs a ticker to start. -i runs it (it prints its table) and
       then stops at a >>> prompt, where you can use its functions. Type there:
           strategy_returns(pd.Series([100.0, 100.0, 100.0, 150.0, 150.0]), 3).tolist()
       These made-up prices jump from 100 to 150 on the fourth day. The fourth
       number of the answer is 0.5: the rule earned the jump, although the close
       was never above its average before that day. Leave the prompt with exit().

WHEN YOU ARE DONE, these commands behave like this
    python p4_backtest.py TSLA
    The row for 2025-09-25 shows a rule_return of -0.0438. The last two lines are:
        rule         +18.55%
        buy and hold +35.03%
    python -i p4_backtest.py F
    At the >>> prompt, each of these two lines gives the answer shown under it
    (a nan may be 0.0 instead):
        strategy_returns(pd.Series([100.0, 100.0, 100.0, 150.0, 150.0]), 3).tolist()
            [nan, 0.0, 0.0, 0.0, 0.0]
        strategy_returns(pd.Series([100.0, 100.0, 100.0, 150.0, 300.0]), 3).tolist()
            [nan, 0.0, 0.0, 0.0, 1.0]
"""

import argparse
import sys
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
WINDOW = 3  # days in the moving average


def load_closes(ticker):
    """Return the closing prices of ticker as a Series whose index is the date, oldest first."""
    prices_df = pd.read_csv(PRICES).set_index("date")
    return prices_df.loc[prices_df.ticker == ticker, "close"]


def above(a, b):
    """Compare two Series row by row: 1.0 where a is above b, otherwise 0.0.

    Comparing Series is not in the lecture. Where either value is missing (NaN),
    the answer is 0.0.
    """
    return (a > b).astype(float)


def total_return(daily_returns):
    """Return what a month of daily returns adds up to: (1 + r1) * (1 + r2) * ... - 1.

    A missing value (NaN) counts as a day with no return.
    """
    return (1 + daily_returns.fillna(0)).prod() - 1


# ---- YOUR WORK: everything below this line ---------------------------------
def strategy_returns(close, window):
    """Return the rule's return on each day.

    Args:
        close: a Series of closing prices, oldest first.
        window: how many days the moving average covers.

    Returns:
        A Series as long as close: the stock's return on the days the rule
        holds the stock, 0.0 (or missing) on the days it holds cash.
    """
    average = close.rolling(window=window).mean()  # the moving average, as in the lecture
    daily_return = close / close.shift(1) - 1  # today's close against yesterday's
    in_market = above(close, average)  # 1.0 on the days the rule holds the stock
    return daily_return * in_market


parser = argparse.ArgumentParser()
parser.add_argument("ticker")
args = parser.parse_args()

close = load_closes(args.ticker)
if len(close) == 0:
    print("no data for", args.ticker)
    sys.exit(1)

rule = strategy_returns(close, WINDOW)
table_df = pd.DataFrame(
    {
        "close": close,
        "average": close.rolling(window=WINDOW).mean(),
        "stock_return": close / close.shift(1) - 1,
        "rule_return": rule,
    }
)
print((table_df.round(4) + 0).to_string())  # + 0 so that a zero never prints as -0.0
print(f"rule         {total_return(rule):+.2%}")
print(f"buy and hold {close.iloc[-1] / close.iloc[0] - 1:+.2%}")  # .iloc[-1]: the last value, by position
