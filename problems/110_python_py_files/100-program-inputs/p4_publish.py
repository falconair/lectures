"""
PROBLEM 4: make the program safe on the wrong machine and honest about failing

THE PROGRAM
    It runs every evening and prints one stock's average closing price for the month.
    On the production server it also adds that result to published.csv, which other
    people read in the morning. Whether a machine is the production server is set
    once, on that machine, in the environment variable SERVER_TYPE.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. A machine where nobody set SERVER_TYPE is treated as the production server.
       Try it:  python p4_publish.py KO    then look in this folder: published.csv
       has appeared. Your laptop just published.
    2. When it fails, it says so and then carries on, publishes a made-up result,
       and reports success.
       Try it:  python p4_publish.py ZZZ   then look at published.csv again.

WHEN YOU ARE DONE, it behaves like this
    python p4_publish.py KO       prints:  KO 21 days, average close 67.04
    ...and what else happens depends on SERVER_TYPE:
        not set                   nothing is published (treat this as DEV)
        DEV                       nothing is published
        PROD                      the line  KO,21,67.04  is added to published.csv
        anything else             prints one line saying so, exits with status 1,
                                  publishes nothing
    python p4_publish.py ZZZ      (no such ticker) prints one line saying so, exits
                                  with status 1, publishes nothing, whatever SERVER_TYPE is

    (An exit status is the number a program hands back when it ends: 0 means it
    worked. To see the status of the program you just ran, type:  echo $?  )

HOW TO SET AN ENVIRONMENT VARIABLE WHILE TESTING
    Mac / Linux:          export SERVER_TYPE=DEV       (undo with: unset SERVER_TYPE)
    Windows cmd:          set SERVER_TYPE=DEV          (undo with: set SERVER_TYPE=)
    Windows PowerShell:   $env:SERVER_TYPE = "DEV"     (undo with: Remove-Item Env:SERVER_TYPE)
    Delete published.csv between tests.

YOUR TASK
    Fix the lines at the bottom, below the line marked YOUR WORK.
    Do not change anything above that line.
    Write plain top-level code. No "if __name__ == ..." is needed.
"""

import csv
import os
import sys
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"
PUBLISHED = Path(__file__).parent / "published.csv"


def average_close(ticker):
    """Return (number of days, average closing price) for ticker; (0, 0.0) if it is not in the file."""
    closes = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["ticker"] == ticker:
                closes.append(float(row["close"]))
    if not closes:
        return 0, 0.0
    return len(closes), sum(closes) / len(closes)


# ---- YOUR WORK: everything below this line ---------------------------------
ticker = sys.argv[1]
server_type = os.environ.get("SERVER_TYPE", "PROD")

days, average = average_close(ticker)
if days == 0:
    print("no data for", ticker)

print(f"{ticker} {days} days, average close {average:.2f}")

if server_type == "PROD":
    with open(PUBLISHED, "a") as out:  # "a" = append: add a line to the end of the file
        out.write(f"{ticker},{days},{average:.2f}\n")
