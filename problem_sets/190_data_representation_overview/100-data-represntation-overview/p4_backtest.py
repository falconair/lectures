"""
PROBLEM 4
Practises: keeping tomorrow's prices out of today's decision (lookahead bias).

Task: fill in the function strategy_returns.

To check your work, type:
    python p4_backtest.py TSLA

It should print what strategy_returns returned. These are its last 5 lines:
    2025-09-24    0.0000
    2025-09-25   -0.0438
    2025-09-26    0.0000
    2025-09-29    0.0064
    2025-09-30    0.0034
"""

import argparse
from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
WINDOW = 3  # days in the moving average


def strategy_returns(close: pd.Series, window: int) -> pd.Series:
    """Return what a simple trading rule earns on each day.

    The rule: after the market closes, compare that day's close with the
    average of the last `window` closes. If the close is above the average,
    hold the stock until the next day's close. Otherwise hold cash.

    Args:
        close: closing prices, oldest first.
        window: how many days the moving average covers.

    Returns:
        A Series as long as close, with the same index. On a day the rule
        holds the stock, the value is the stock's return on that day
        (that day's close / the day before's close - 1). On a day it holds
        cash, the value is 0.0. The first day is 0.0.

    Example. The price jumps from 100 to 150 on the fourth day. The rule was
    in cash that day, so it earns nothing from the jump. That close is above
    its average, so the rule holds the stock on the fifth day and earns the
    move from 150 to 300:
        strategy_returns(pd.Series([100.0, 100.0, 100.0, 150.0, 300.0]), 3)
    returns
        0    0.0
        1    0.0
        2    0.0
        3    0.0
        4    1.0
    """
    average = close.rolling(window=window).mean()  # the moving average, as in the lecture
    daily_return = close / close.shift(1) - 1  # each day's close against the day before's
    raise NotImplementedError  # YOUR WORK: replace this line. Use the two lines above.


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    args = parser.parse_args()

    prices_df = pd.read_csv(PRICES).set_index("date")
    close = prices_df.loc[prices_df.ticker == args.ticker, "close"]
    print(strategy_returns(close, WINDOW).round(4).to_string())
