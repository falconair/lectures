"""
PROBLEM 3
Practises: testing that a function raises an error when it should.

Task: fill in the three tests of daily_returns. The function is correct.

To check your work, type:
    pytest p3_bad_prices.py

The last line it prints should say:
    3 passed
"""

import pytest


def daily_returns(closes: list[float]) -> list[float]:
    """Return one return for each day after the first: that day's close / the day before's close - 1.

    A closing price is never zero or negative: in a data file such a price is
    a mistake. Raises ValueError if any price is zero or negative.
    """
    for price in closes:
        if price <= 0:
            raise ValueError(f"bad price: {price}")
    returns = []
    for i in range(1, len(closes)):
        returns.append(closes[i] / closes[i - 1] - 1)
    return returns


# ---- YOUR WORK: the three tests below --------------------------------------
def test_good_prices() -> None:
    """Check that daily_returns([100.0, 50.0, 75.0]) is [-0.5, 0.5]."""
    raise NotImplementedError  # YOUR WORK: replace this line


def test_zero_price_is_rejected() -> None:
    """Check that daily_returns raises ValueError for [100.0, 50.0, 0.0]."""
    raise NotImplementedError  # YOUR WORK: replace this line


def test_negative_price_is_rejected() -> None:
    """Check that daily_returns raises ValueError for [100.0, -50.0, 50.0]."""
    raise NotImplementedError  # YOUR WORK: replace this line

# NOTES
#   How your tests are graded: they are run against the function above, where
#   they must pass, and against wrong versions of it, where at least one of
#   them must fail. A test that cannot fail earns nothing.
