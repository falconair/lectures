"""
PROBLEM 3: make the function reject a zero or negative price with ValueError, and test that it does

YOUR TASK
    Change only the lines below the line marked YOUR WORK: the function and the tests.
    What is graded:
    - daily_returns raises ValueError if any price is zero or negative, in any position
    - for good prices it returns what it returns now
    - test_daily_returns_good_prices is unchanged and passes
    - test_daily_returns_bad_prices is replaced by one test function for a zero price and
      another for a negative price, so the file has at least three tests; all of them pass
    - at least one of your tests fails for each wrong version listed at the end
    How it is graded: your function is called directly, and your tests are run against a
    correct daily_returns and against each wrong version. You cannot run that yourself,
    but you can make each change to your function by hand and watch a test fail.
    Not in the lecture, a line that stops a function with an error (any message is fine):
        raise ValueError(f"bad price: {price}")

THE PROGRAM
    daily_returns gives a stock's return for each day. A closing price is never zero or
    negative. In a data file such a price means "missing" or "typing mistake", and no
    return can be calculated from it.

WHAT IS WRONG WITH IT (this is the bug you are fixing)
    1. The function does not reject bad prices with an error. Try:
           python -i p3_bad_prices.py
       (-i loads the file and leaves you at the >>> prompt, where you can call its
       functions.) At the prompt type:
           daily_returns([100.0, -50.0, 50.0])
       It prints [-1.5, -2.0]. Then type:
           daily_returns([100.0, 50.0, 0.0])
       It prints [-0.5, -1.0]. There is no error either time. Leave with:  exit()
    2. The tests do not show it. Try:
           pytest p3_bad_prices.py
       The last line says "2 passed". One of the two is test_daily_returns_bad_prices.
       (try/except is not in the lecture: if a line under try raises an error, the
       lines under except run instead.)

WHEN YOU ARE DONE, these commands behave like this
    python -i p3_bad_prices.py            then, at the >>> prompt:
        daily_returns([100.0, -50.0, 50.0])    ends with:  ValueError: bad price: -50.0
        daily_returns([100.0, 50.0, 0.0])      ends with:  ValueError: bad price: 0.0
    pytest p3_bad_prices.py
        3 passed
    (a larger number if you wrote more than three tests)
    The wrong versions of daily_returns that your tests are run against:
        a. the function as it is now, with no check at all
        b. it rejects a zero price and accepts a negative one
        c. it rejects a negative price and accepts a zero one
"""

import pytest


# ---- YOUR WORK: everything below this line ---------------------------------
def daily_returns(closes):
    """Return one return for each day after the first: that day's close / the day before's close - 1."""
    returns = []
    for i in range(1, len(closes)):
        returns.append(closes[i] / closes[i - 1] - 1)
    return returns


def test_daily_returns_good_prices():
    # AAPL's first three closes of September 2025
    assert daily_returns([229.72, 238.47, 239.78]) == pytest.approx(
        [0.03809, 0.00549], abs=0.00001
    )


def test_daily_returns_bad_prices():
    try:
        daily_returns([100.0, 0.0, 50.0])
    except Exception:
        pass
