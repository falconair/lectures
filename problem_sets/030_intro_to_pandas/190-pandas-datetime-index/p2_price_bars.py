"""
PROBLEM 2
Practises: resampling trades into bars of a fixed length, one aggregator per column.

Task: fill in the function price_bars.

To check your work, type:
    python p2_price_bars.py AAPL 5min

It should print what price_bars returned for AAPL's trades from 10:00 to 10:20:
                           open    high     low   close  volume
    sip_timestamp
    2025-09-10 10:00:00  233.45  233.58  233.40  233.53     856
    2025-09-10 10:05:00  233.54  233.54  233.45  233.48    1329
    2025-09-10 10:10:00  233.48  233.60  233.45  233.53    2496
    2025-09-10 10:15:00  233.57  233.58  233.51  233.56    1601
"""

import sys
from pathlib import Path

import pandas as pd

# trades.csv sits in the same folder as this file, wherever you run it from.
# It holds every AAPL and MSFT trade on 2025-09-10 from 10:00 to 10:20 (UTC),
# before the market opened.
TRADES = Path(__file__).parent / "trades.csv"


def price_bars(trades_df: pd.DataFrame, length: str) -> pd.DataFrame:
    """Return a price bar for each period of the given length.

    Args:
        trades_df: one stock's trades, with the columns price and size, and the time
            of each trade as the index (a datetime index).
        length: the length of each bar, as pandas writes it: "1min", "5min", "30s".

    Returns:
        One row per bar, with the bar's start time as the index and the columns
        open (the first price), high, low, close (the last price) and volume (the
        number of shares traded).

    Example:
        trades_df = pd.DataFrame({"price": [233.5, 234.0, 233.0, 233.25, 233.75],
                                  "size": [10, 20, 30, 40, 50]},
                                 index=pd.to_datetime(["2025-09-10 10:00:05",
                                                       "2025-09-10 10:00:20",
                                                       "2025-09-10 10:00:40",
                                                       "2025-09-10 10:00:55",
                                                       "2025-09-10 10:01:30"]))
        price_bars(trades_df, "1min")
    returns
                               open    high     low   close  volume
        2025-09-10 10:00:00  233.50  234.00  233.00  233.25     100
        2025-09-10 10:01:00  233.75  233.75  233.75  233.75      50
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    ticker, length = sys.argv[1], sys.argv[2]
    trades_df = pd.read_csv(TRADES)
    trades_df["sip_timestamp"] = pd.to_datetime(trades_df["sip_timestamp"])
    trades_df = trades_df.set_index("sip_timestamp")
    one_stock_df = trades_df.loc[trades_df["ticker"] == ticker, ["price", "size"]]
    print(price_bars(one_stock_df, length).to_string())

# NOTES
#   "first" and "last" work as aggregators, like "max" and "min": they give the
#   first and the last value in each bar.
