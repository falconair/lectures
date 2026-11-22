"""
PROBLEM 1
Practises: turning a timestamp column into a datetime index, and selecting rows by time.

Task: fill in the function trades_between.

To check your work, type:
    python p1_trades_between.py "2025-09-10 10:07:10" "2025-09-10 10:07:30"

It should print what trades_between returned:
                                  ticker   price  size
    sip_timestamp
    2025-09-10 10:07:11.715316496   MSFT  498.56     1
    2025-09-10 10:07:11.834225753   AAPL  233.45     3
    2025-09-10 10:07:12.769505116   MSFT  498.61     2
    2025-09-10 10:07:23.766311335   AAPL  233.48   118
    2025-09-10 10:07:25.718667581   MSFT  498.61     1
    2025-09-10 10:07:25.719285559   MSFT  498.63    20
"""

import sys
from pathlib import Path

import pandas as pd

# trades.csv sits in the same folder as this file, wherever you run it from.
# It holds every AAPL and MSFT trade on 2025-09-10 from 10:00 to 10:20 (UTC),
# before the market opened.
TRADES = Path(__file__).parent / "trades.csv"


def trades_between(trades_df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    """Return the trades from start to end, both included, with their time as the index.

    Args:
        trades_df: one row per trade, as read from trades.csv: the columns ticker,
            price, size and sip_timestamp (nanoseconds since 1970, a whole number).
        start: the first time wanted, as text, such as "2025-09-10 10:00".
        end: the last time wanted, as text. "2025-09-10 10:01" means the whole
            of that minute.

    Returns:
        The trades from start to end, with the columns ticker, price and size,
        and the time of each trade (sip_timestamp, as a datetime) as the index.

    Example:
        trades_df = pd.DataFrame({"ticker": ["AAPL", "AAPL", "MSFT"],
                                  "price": [233.5, 233.75, 498.5],
                                  "size": [10, 20, 30],
                                  "sip_timestamp": [1757498400000000000,
                                                    1757498490000000000,
                                                    1757498520000000000]})
        trades_between(trades_df, "2025-09-10 10:00", "2025-09-10 10:01")
    returns
                            ticker   price  size
        sip_timestamp
        2025-09-10 10:00:00   AAPL  233.50    10
        2025-09-10 10:01:30   AAPL  233.75    20
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    trades_df = pd.read_csv(TRADES)
    print(trades_between(trades_df, sys.argv[1], sys.argv[2]).to_string())
