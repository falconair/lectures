"""
PROBLEM 1
Practises: reading a command-line argument from sys.argv.

Task: fill in the function ticker_from.

To check your work, type:
    python p1_last_close.py MSFT

It should print the ticker that ticker_from returned, then that stock's last closing price:
    MSFT 517.95
"""

import csv
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def ticker_from(argv: list[str]) -> str:
    """Return the ticker the user typed on the command line.

    If the user typed no ticker, print one line that says how to run the
    program, then exit with status 1.

    Args:
        argv: the command line as a list of text, as in sys.argv. Its first
            item is the program's name.

    Returns:
        The ticker.

    Example:
        ticker_from(["p1_last_close.py", "MSFT"])
    returns
        'MSFT'
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
def last_close(ticker: str) -> float:
    """Return the most recent closing price of ticker (nan if it is not in the file)."""
    price = float("nan")
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):  # one dict per line: row["close"]
            if row["ticker"] == ticker:
                price = float(row["close"])  # the file is in date order, so the last one wins
    return price


if __name__ == "__main__":
    ticker = ticker_from(sys.argv)
    print(ticker, last_close(ticker))
