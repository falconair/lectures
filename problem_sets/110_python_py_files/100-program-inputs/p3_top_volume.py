"""
PROBLEM 3: make argparse refuse a badly written date or --top, and give --top a default of 3

YOUR TASK
    Change the lines below the line marked YOUR WORK. Do not change anything above it.
    Your work is checked by running the commands at the end of this comment.
    These are graded:
      - without --top, it prints the 3 most traded stocks
      - with --top N, it prints the N most traded stocks; N is a whole number, 1 or more
      - --top with any other value (five, 0): argparse error message, exit status 2
      - a date that is not written exactly YYYY-MM-DD (9/10/2025, 2025-9-10):
        argparse error message, exit status 2
    "argparse error message" means: argparse prints a line that starts with "usage:"
    and a line that starts with "error:", followed by your message. You choose only
    your message.
    Not part of the task: a correctly written date with no trading (2025-09-06, a
    Saturday) prints nothing, with exit status 0. That is correct; leave it.
    You need three things the lecture did not show: see the comments above YOUR WORK.
    You will write one or two small functions below the line; the rest is plain code,
    not inside a function. No "if __name__ == ..." is needed.

THE PROGRAM
    It prints the most heavily traded stocks on one day, busiest first.
    It already uses argparse: a date, and an optional --top for how many to print.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. python p3_top_volume.py 2025-09-10            prints all 10 stocks
    2. python p3_top_volume.py 2025-09-10 --top 5    ends with a TypeError
    3. python p3_top_volume.py 9/10/2025             prints nothing; the exit status is 0

WHEN YOU ARE DONE, these commands behave like this
    python p3_top_volume.py 2025-09-10
        NVDA 226852000
        AAPL 83440800
        TSLA 72121700
    python p3_top_volume.py 2025-09-10 --top 5
        (the same three lines, then two more)
    Each of the next four: argparse error message, exit status 2
        python p3_top_volume.py 2025-09-10 --top five
        python p3_top_volume.py 2025-09-10 --top 0
        python p3_top_volume.py 9/10/2025
        python p3_top_volume.py 2025-9-10

    Exit status: a number a program returns when it ends (0 = it worked). To see it, the
    very next command must be:  echo $?
"""

import argparse
import csv
import datetime
from pathlib import Path

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def top_by_volume(day, top):
    """Return the `top` most traded tickers on day (text, "YYYY-MM-DD"), busiest first.

    The result is a list of (ticker, volume) pairs. `top` is a whole number.
    """
    rows = []
    with open(PRICES, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["date"] == day:
                rows.append((row["ticker"], int(row["volume"])))
    rows.sort(key=lambda pair: -pair[1])  # minus: largest volume first
    return rows[:top]


# NOT IN THE LECTURE (1 and 2): two more things that add_argument accepts.
#   default=VALUE    the value used when the user leaves an optional argument out
#   type=FUNCTION    argparse calls FUNCTION with the text the user typed, and whatever
#                    FUNCTION returns becomes the value in args. (The lecture's
#                    program6.py used type=str.) FUNCTION can be one you write. To
#                    refuse the text, your function runs this line:
#                        raise argparse.ArgumentTypeError("your message")
#                    argparse then prints its error message and exits with status 2.
#
# NOT IN THE LECTURE (3): checking that a text is a date. This function is correct;
# use it as it is.
def is_date(text):
    """Return True if text is a real date written exactly YYYY-MM-DD, such as "2025-09-10"."""
    try:  # try the indented line; if it fails with a ValueError, do the "except" part
        datetime.datetime.strptime(text, "%Y-%m-%d")  # ValueError if text is not a date
    except ValueError:
        return False
    return len(text) == 10  # strptime also accepts "2025-9-10"; this refuses it


# ---- YOUR WORK: everything below this line ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("date")
parser.add_argument("--top")
args = parser.parse_args()

for ticker, volume in top_by_volume(args.date, args.top):
    print(ticker, volume)
