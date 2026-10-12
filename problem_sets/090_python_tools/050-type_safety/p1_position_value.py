"""
PROBLEM 1
Practises: annotating a function's arguments and what it returns.

Task: add type annotations to position_value and describe. Each docstring
says what the types are. Change nothing else.

To check your work, type these two commands:
    mypy --strict p1_position_value.py
    python p1_position_value.py

They should print:
    Success: no issues found in 1 source file
    AAPL: 100 shares at 229.72 = 22,972.00
"""


def position_value(shares, price):
    """Return the dollar value of a position: the number of shares times the price.

    shares is a whole number. price is a decimal number, and so is the value.
    """
    return shares * price


def describe(ticker, shares, price):
    """Print one line about a position. It returns nothing.

    ticker is text, for example "AAPL". shares and price are as in position_value.
    """
    print(f"{ticker}: {shares} shares at {price:.2f} = {position_value(shares, price):,.2f}")


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    describe("AAPL", 100, 229.72)

# NOTES
#   Not in the lecture: --strict makes mypy also report a function that has no
#   type annotations. Without it, mypy says nothing about such a function.
