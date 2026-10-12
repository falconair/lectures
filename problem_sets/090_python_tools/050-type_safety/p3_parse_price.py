"""
PROBLEM 3
Practises: annotating a value that is sometimes None.

Task: add type annotations to parse_price and price_or_last. Each docstring
says what the types are. Change nothing else.

To check your work, type these two commands:
    mypy --strict p3_parse_price.py
    python p3_parse_price.py

They should print:
    Success: no issues found in 1 source file
    [229.72, 229.72, 238.47]
"""


def parse_price(text):
    """Return the price written in text. Return None if text is empty.

    text is text, for example "229.72" or "". The price is a decimal number.
    """
    if text == "":
        return None
    return float(text)


def price_or_last(text, last_price):
    """Return the price written in text. If text is empty, return last_price.

    text is text. last_price is a decimal number. A decimal number is always returned.
    """
    price = parse_price(text)
    if price is None:
        return last_price
    return price


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    cells = ["229.72", "", "238.47"]  # one cell of a data file per day; the second day is missing
    prices: list[float] = []
    last_price = 0.0
    for cell in cells:
        last_price = price_or_last(cell, last_price)
        prices.append(last_price)
    print(prices)

# NOTES
#   Not in the lecture: --strict makes mypy also report a function that has no
#   type annotations. Without it, mypy says nothing about such a function.
