"""
PROBLEM 2: split one long function into three small ones, each with a docstring

YOUR TASK
    Change the lines below the line marked YOUR WORK, and nothing above it.
    Your work is checked by running the program and by calling your functions by
    the names below; a person then reads the code.
    - Write three functions with exactly these names and arguments:
        load_closes(ticker)             the closing prices of ticker, oldest first,
                                        as a list of numbers; an empty list if the
                                        ticker is not in the file
        daily_returns(closes)           one return for each day after the first:
                                        that day's close / the day before's close - 1
        annualized_volatility(returns)  the standard deviation of the returns,
                                        times the square root of 252 (it is
                                        always given at least two returns)
    - volatility_report becomes a few lines that call the three and print, like
      analyze_market_volatility_regimes in the lecture's "Good" example.
    - The program prints exactly what it prints now, with the same exit status.
    - Each of the four has a docstring like the lecture's: one sentence, Args,
      and Returns if it returns something.
    - 252 (trading days in a year) is a named constant, written as the lecture does.
    - The lines that run the program stay at the bottom of the file, outside any
      function, as they are now. No "if __name__ == ..." is needed.

THE PROGRAM
    It prints how volatile one stock was over the month: the standard deviation of
    its daily returns, scaled up to a year (annualized volatility).
    Try it:  python p2_volatility.py TSLA

WHAT IS WRONG WITH IT (this is what you are fixing)
    The answers are right. One function, volatility_report, does all the work.
    1. No part of it can be used or checked alone. Try it:
           python -i p2_volatility.py TSLA
       (-i runs the program and then leaves you at the >>> prompt with everything
       the program defined still loaded.) At the prompt type:
           daily_returns([80.0, 100.0, 50.0])
       You get a NameError.
    2. At the same prompt, help(volatility_report) shows the function's name and
       nothing about what it does. (If help fills the screen, press q.)
       Leave the prompt with:  exit()

WHEN YOU ARE DONE, these commands behave like this
    python p2_volatility.py TSLA
        TSLA 21 days, last close 444.72, annualized volatility 44.8%
    python p2_volatility.py KO
        KO 21 days, last close 66.32, annualized volatility 10.4%
    python p2_volatility.py ZZZ
        no data for ZZZ
    That last command ends with exit status 1. To see the status, type:  echo $?
    python -i p2_volatility.py TSLA       then, at the >>> prompt:
        load_closes("KO")[:3]                                    [69.06, 68.99, 68.25]
        load_closes("ZZZ")                                       []
        daily_returns([80.0, 100.0, 50.0])                       [0.25, -0.5]
        daily_returns([])                                        []
        round(annualized_volatility([0.01, -0.01, 0.03]), 4)     0.3175
        help(daily_returns)                                      your docstring
"""

import csv
import math
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


# ---- YOUR WORK: everything below this line ---------------------------------


def volatility_report(ticker):
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
    volatility = math.sqrt(total / (len(returns) - 1)) * math.sqrt(252)

    print(
        f"{ticker} {len(closes)} days, last close {closes[-1]:.2f}, annualized volatility {volatility:.1%}"
    )


if len(sys.argv) != 2:
    print("usage: python p2_volatility.py TICKER")
    sys.exit(1)

volatility_report(sys.argv[1])
