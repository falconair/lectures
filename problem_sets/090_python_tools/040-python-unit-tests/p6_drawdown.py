"""
PROBLEM 6
Practises: letting Hypothesis find the inputs your own examples missed.

Task: fill in the property test of max_drawdown. Run it: Hypothesis finds
closes for which max_drawdown is wrong, although the two example tests pass.
Then repair max_drawdown until every test passes.

To check your work, type:
    pytest p6_drawdown.py

The last line it prints should say:
    3 passed
"""

from hypothesis import given
from hypothesis import strategies as st


def max_drawdown(closes: list[float]) -> float:
    """Return the largest fall from a peak to a later close, as a fraction of that peak.

    Args:
        closes: closing prices, oldest first; at least one.

    Returns:
        The largest (peak - later close) / peak, where the peak is the highest
        close so far. 0.0 if the price never falls.

    Example. The price rises to 120, then falls to 90, a fall of 30 from 120:
        max_drawdown([100.0, 120.0, 90.0])
    returns
        0.25
    """
    # YOUR WORK: repair the lines below
    highest = max(closes)
    lowest = min(closes)
    return (highest - lowest) / highest


def test_rise_then_fall() -> None:
    assert max_drawdown([100.0, 120.0, 90.0]) == 0.25


def test_one_fall() -> None:
    assert max_drawdown([100.0, 50.0]) == 0.5


# ---- YOUR WORK: the test below ---------------------------------------------
def test_never_falls_means_no_drawdown() -> None:
    """Check that max_drawdown is 0.0 for any closes that never fall.

    Let Hypothesis make the closes: a list of at least one float between 1 and
    1000. Sort it from low to high, so that the price never falls.
    """
    raise NotImplementedError  # YOUR WORK: replace this line

# NOTES
#   How your test is graded: it is run against a correct max_drawdown, where it
#   must pass, and against wrong versions of it, where it must fail.
#   Not in the lecture: st.lists(st.floats(min_value=1, max_value=1000), min_size=1)
#   makes lists of at least one float between 1 and 1000.
