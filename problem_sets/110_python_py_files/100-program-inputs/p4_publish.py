"""
PROBLEM 4: publish only on the production server, and exit with status 1 on bad input

YOUR TASK
    Change the lines below the line marked YOUR WORK. Do not change anything above it.
    Your work is checked by running the commands at the end of this comment with
    several values of SERVER_TYPE, and by reading published.csv after each run.
    These are graded:
      - SERVER_TYPE is not set, or is DEV: it prints the average line, publishes nothing
      - SERVER_TYPE is PROD: it prints the average line and adds one line to published.csv
      - SERVER_TYPE has any other value (for example prod in small letters, or set but
        empty): it prints one line that says the value is not accepted, exit status 1
      - the ticker is not in prices.csv, whatever SERVER_TYPE is: it prints one line that
        says so, exit status 1
      - in the last two cases it does not print the average line and publishes nothing
    If the ticker and SERVER_TYPE are both wrong, either of the two messages will do.
    A ticker is always given on the command line. You need not handle a missing one.
    Write your code directly below the line, not inside a function, as the lecture's
    programs do. No "if __name__ == ..." is needed.

THE PROGRAM
    Every evening it prints one stock's average closing price for the month. On the
    production server it also adds that result to published.csv, which other people read
    in the morning. The environment variable SERVER_TYPE says which machine this is.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p4_publish.py KO     (SERVER_TYPE not set)
       published.csv appears in this folder. This machine is not the production server.
    2. python p4_publish.py ZZZ    (SERVER_TYPE not set)
       It prints "no data for ZZZ" and then "ZZZ 0 days, average close 0.00", adds the
       line ZZZ,0,0.00 to published.csv, and the exit status is 0.

WHEN YOU ARE DONE, these commands behave like this
    python p4_publish.py KO
        SERVER_TYPE   it prints                            added to published.csv   exit status
        not set       KO 21 days, average close 67.04      nothing                  0
        DEV           KO 21 days, average close 67.04      nothing                  0
        PROD          KO 21 days, average close 67.04      KO,21,67.04              0
        other value   (one line: value not accepted)       nothing                  1
    python p4_publish.py ZZZ
        any value     (one line: no such ticker)           nothing                  1

HOW TO SET AN ENVIRONMENT VARIABLE WHILE TESTING
    Mac / Linux:          export SERVER_TYPE=DEV       (undo with: unset SERVER_TYPE)
                          Without the word export, the program does not see the value.
                          To set it to empty:  export SERVER_TYPE=
    Windows cmd:          set SERVER_TYPE=DEV          (undo with: set SERVER_TYPE=)
    Windows PowerShell:   $env:SERVER_TYPE = "DEV"     (undo with: Remove-Item Env:SERVER_TYPE)
    Delete published.csv between tests.

    Exit status: a number a program returns when it ends (0 = it worked). To see it, the
    very next command must be:  echo $?
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
