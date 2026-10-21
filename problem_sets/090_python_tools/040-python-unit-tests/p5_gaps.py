"""
PROBLEM 5
Practises: using coverage to find the lines that no test runs.

Task: one test of gap_label is given. Add tests until coverage reports that
every line of this file runs. The function gap_label is correct.

To check your work, type these two commands:
    coverage run -m pytest p5_gaps.py
    coverage report -m

The second should print a report that ends in 100% (your Stmts count
depends on how many tests you wrote):
    Name         Stmts   Miss  Cover   Missing
    ------------------------------------------
    p5_gaps.py      18      0   100%
    ------------------------------------------
    TOTAL           18      0   100%
"""

import pytest


def gap_label(previous_close: float, open_price: float) -> str:
    """Say whether a stock opened far from where it closed the day before.

    Args:
        previous_close: the closing price of the day before.
        open_price: the opening price of the day.

    Returns:
        "gap up" if the open is more than 2% above the previous close,
        "gap down" if it is more than 2% below, and "no gap" otherwise.

    Raises:
        ValueError: if either price is zero or negative.

    Example. AAPL closed at 229.72 on 2025-09-02 and opened at 237.21 the next day:
        gap_label(229.72, 237.21)
    returns
        'gap up'
    """
    if previous_close <= 0 or open_price <= 0:
        raise ValueError(f"bad price: {previous_close}, {open_price}")
    if open_price > previous_close * 1.02:
        return "gap up"
    if open_price < previous_close * 0.98:
        return "gap down"
    return "no gap"


def test_gap_up() -> None:
    assert gap_label(229.72, 237.21) == "gap up"


# ---- YOUR WORK: add tests below, until coverage reports 100% ---------------


# NOTES
#   How your tests are graded: they are run against the function above, where
#   they must pass, and against wrong versions of it, where at least one of
#   them must fail. A test that runs a line but checks nothing earns nothing.
#   coverage report -m lists, under Missing, the numbers of the lines no test ran.
#   With only the given test, it says 64%.
