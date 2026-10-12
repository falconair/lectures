"""
PROBLEM 2
Practises: splitting one long function into small ones that each do one thing.

Task: fill in load_closes, daily_returns and annualized_volatility, using code
taken from volatility_report. Then make volatility_report call the three, and
give it a docstring like theirs.

To check your work, type:
    python p2_volatility.py TSLA

It should print what it prints now:
    TSLA 21 days, last close 444.72, annualized volatility 44.8%
"""

import csv
import math
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"

TRADING_DAYS_PER_YEAR = 252


def load_closes(ticker: str) -> list[float]:
    """Return the closing prices of ticker, oldest first.

    Args:
        ticker: the stock's symbol, for example "KO".

    Returns:
        A list of prices. An empty list if ticker is not in the file.

    Example:
        load_closes("KO")[:3]
    returns
        [69.06, 68.99, 68.25]
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def daily_returns(closes: list[float]) -> list[float]:
    """Return one return for each day after the first.

    A day's return is that day's close / the day before's close - 1.

    Args:
        closes: closing prices, oldest first.

    Returns:
        A list one shorter than closes.

    Example:
        daily_returns([80.0, 100.0, 50.0])
    returns
        [0.25, -0.5]
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def annualized_volatility(returns: list[float]) -> float:
    """Return the standard deviation of returns, scaled up to a year.

    Scaling up: multiply by the square root of TRADING_DAYS_PER_YEAR.

    Args:
        returns: daily returns, at least two of them.

    Returns:
        The annualized volatility: 0.25 means 25%.

    Example:
        annualized_volatility([0.01, -0.01, 0.03])
    returns, to 4 decimal places,
        0.3175
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def volatility_report(ticker: str) -> None:
    # read the file: csv.DictReader gives one dict per line, e.g. row["close"]
    closes = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["ticker"] == ticker:
                closes.append(float(row["close"]))  # the file is in date order
    if not closes:
        print("no data for", ticker)
        sys.exit(1)

    returns = []
    for i in range(1, len(closes)):
        returns.append(closes[i] / closes[i - 1] - 1)

    mean = sum(returns) / len(returns)
    total = 0.0
    for r in returns:
        total = total + (r - mean) ** 2
    volatility = math.sqrt(total / (len(returns) - 1)) * math.sqrt(TRADING_DAYS_PER_YEAR)

    print(f"{ticker} {len(closes)} days, last close {closes[-1]:.2f}, annualized volatility {volatility:.1%}")


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python p2_volatility.py TICKER")
        sys.exit(1)
    volatility_report(sys.argv[1])
