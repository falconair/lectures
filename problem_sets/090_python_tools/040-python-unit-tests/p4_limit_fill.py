"""
PROBLEM 4
Practises: writing the tests first, then using them to repair the code.

Task: fill in the four tests of would_fill. Run them: some fail, because
would_fill has two faults. Then repair would_fill until every test passes.

To check your work, type:
    pytest p4_limit_fill.py

The last line it prints should say:
    6 passed
"""

import pytest


def would_fill(side: str, limit_price: float, day_low: float, day_high: float) -> bool:
    """Return True if a limit order would have traded on a day with this low and high.

    A BUY trades if the stock fell to the limit price or lower.
    A SELL trades if the stock rose to the limit price or higher.
    Reaching the limit exactly counts as trading.

    Args:
        side: "BUY" or "SELL".
        limit_price: the price of the order.
        day_low: the lowest price of the day.
        day_high: the highest price of the day.

    Raises:
        ValueError: if side is neither "BUY" nor "SELL".

    Example. On 2025-09-02 AAPL's low was 226.97 and its high was 230.85:
        would_fill("SELL", 240.00, 226.97, 230.85)
    returns
        False
    """
    # YOUR WORK: repair the lines below
    if side == "BUY":
        return day_low <= limit_price
    if side == "SELL":
        return day_low <= limit_price
    return False


def test_buy_fills_when_the_low_reaches_below_the_limit() -> None:
    assert would_fill("BUY", 228.00, 226.97, 230.85) is True


def test_buy_does_not_fill_when_the_low_stays_above_the_limit() -> None:
    assert would_fill("BUY", 225.00, 226.97, 230.85) is False


# ---- YOUR WORK: the four tests below ---------------------------------------
def test_sell_fills_when_the_high_reaches_above_the_limit() -> None:
    """Check a SELL whose limit is between the day's low and high: it trades."""
    raise NotImplementedError  # YOUR WORK: replace this line


def test_sell_does_not_fill_when_the_high_stays_below_the_limit() -> None:
    """Check a SELL whose limit is above the day's high: it does not trade."""
    raise NotImplementedError  # YOUR WORK: replace this line


def test_reaching_the_limit_exactly_counts() -> None:
    """Check a BUY at exactly the day's low, and a SELL at exactly the day's high: both trade."""
    raise NotImplementedError  # YOUR WORK: replace this line


def test_unknown_side_is_rejected() -> None:
    """Check that a side that is neither "BUY" nor "SELL" raises ValueError."""
    raise NotImplementedError  # YOUR WORK: replace this line

# NOTES
#   How your tests are graded: they are run against a correct would_fill, where
#   they must pass, and against wrong versions of it, where at least one of
#   them must fail. A test that cannot fail earns nothing.
