"""
PROBLEM 4: write the tests that are missing, then fix the two bugs they find

YOUR TASK
    Change only the lines below the line marked YOUR WORK: the function and the tests.
    What is graded:
    - would_fill follows the two rules under THE PROGRAM, for BUY and for SELL
    - a side that is neither "BUY" nor "SELL" raises ValueError
    - the two BUY tests are still there, you have added tests of your own, and all pass
    - at least one of your tests fails for each wrong version listed at the end
    How it is graded: your function is called directly, and your tests are run against a
    correct would_fill and against each wrong version. You cannot run that yourself, but
    you can make each change to your function by hand and watch a test fail.
    Write the tests first and run them on the function as it is: some fail (that is the
    bug) and some pass already. Then fix the function.
    Not in the lecture, a line that stops a function with an error:
        raise ValueError(f"unknown side: {side}")

THE PROGRAM
    A backtest has to decide whether a limit order would have traded on a given day.
    would_fill answers from the day's low and high:
        a BUY at a limit price trades if the stock fell to that price or lower
        a SELL at a limit price trades if the stock rose to that price or higher
    Reaching the limit exactly counts as trading.
    The examples use AAPL on 2025-09-02: low 226.97, high 230.85.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. The tests pass, and they do not run every line of would_fill. Try:
           pytest p4_limit_fill.py
           coverage run -m pytest p4_limit_fill.py
           coverage report -m
       pytest says "2 passed". In the report, the column named Missing (-m adds it)
       gives the numbers of the lines that no test ran.
    2. The function has two bugs that the two tests do not find. The rules under
       THE PROGRAM say what it should do.

WHEN YOU ARE DONE, these commands behave like this
    python -i p4_limit_fill.py
    (-i loads the file and leaves you at the >>> prompt; leave with exit().) There:
        would_fill("SELL", 240.00, 226.97, 230.85)    prints:  False
        would_fill("SELLL", 228.00, 226.97, 230.85)   ends with:  ValueError: unknown side: SELLL
    pytest p4_limit_fill.py
        every test passes
    coverage run -m pytest p4_limit_fill.py     then     coverage report -m
        100%, and nothing in the Missing column
    The wrong versions of would_fill that your tests are run against:
        a. the function as it is now
        b. a SELL never trades
        c. a SELL trades only if the high went above the limit, not if it reached it exactly
        d. a BUY trades only if the low went below the limit, not if it reached it exactly
        e. a side that is neither "BUY" nor "SELL" returns False
    100% coverage does not show that these are caught: one SELL case runs the SELL line,
    and one SELL case cannot catch all of a, b and c. Decide which cases separate each
    wrong version from the correct function.
"""

import pytest  # you will need it for pytest.raises


# ---- YOUR WORK: everything below this line ---------------------------------
def would_fill(side, limit_price, day_low, day_high):
    """Return True if a limit order would have traded during a day with this low and high.

    Raises ValueError if side is neither "BUY" nor "SELL".
    """
    if side == "BUY":
        return day_low <= limit_price
    if side == "SELL":
        return day_low <= limit_price
    return False


def test_buy_fills_when_the_low_reaches_the_limit():
    assert would_fill("BUY", 228.00, 226.97, 230.85) is True


def test_buy_does_not_fill_when_the_low_stays_above_the_limit():
    assert would_fill("BUY", 225.00, 226.97, 230.85) is False
