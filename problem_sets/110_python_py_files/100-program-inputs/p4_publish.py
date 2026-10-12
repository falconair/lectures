"""
PROBLEM 4
Practises: reading an environment variable, with a safe answer when it is not set.

Task: fill in the function should_publish.

To check your work, type these two commands:
    python p4_publish.py KO
    SERVER_TYPE=PROD python p4_publish.py KO

Each prints KO's average close, then what should_publish returned. The first should print:
    KO 21 days, average close 67.04
    publish: False
and the second:
    KO 21 days, average close 67.04
    publish: True
"""

import csv
import os
import sys
from collections.abc import Mapping
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def should_publish(environ: Mapping[str, str]) -> bool:
    """Return True only on the production server.

    The environment variable SERVER_TYPE says what kind of machine this is.
    Only the value "PROD" means the production server. A machine on which
    SERVER_TYPE is not set is not the production server.

    Args:
        environ: the environment variables, as in os.environ.

    Returns:
        True if the results should be published, otherwise False.

    Examples:
        should_publish({"SERVER_TYPE": "PROD"})   returns   True
        should_publish({"SERVER_TYPE": "DEV"})    returns   False
        should_publish({})                        returns   False
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
def average_close(ticker: str) -> tuple[int, float]:
    """Return (number of days, average closing price) for ticker."""
    closes = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["ticker"] == ticker:
                closes.append(float(row["close"]))
    return len(closes), sum(closes) / len(closes)


if __name__ == "__main__":
    days, average = average_close(sys.argv[1])
    print(f"{sys.argv[1]} {days} days, average close {average:.2f}")
    print("publish:", should_publish(os.environ))
