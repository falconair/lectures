"""
PROBLEM 3
Practises: sorting a table by two columns.

Task: fill in the function daily_leaderboard.

To check your work, type:
    python p3_daily_leaderboard.py

It should print the first twelve rows of what daily_leaderboard returned
for September 2025:
               date ticker  change_pct
    167  2025-09-30   NVDA        2.47
    146  2025-09-30   MSFT        0.92
    188  2025-09-30   TSLA        0.72
    125  2025-09-30     KO        0.38
    83   2025-09-30    GME        0.26
    20   2025-09-30   AAPL       -0.09
    104  2025-09-30    JPM       -0.26
    209  2025-09-30    XOM       -0.53
    41   2025-09-30   AMZN       -1.11
    62   2025-09-30      F       -1.24
    40   2025-09-29   AMZN        0.95
    166  2025-09-29   NVDA        0.79
"""

from pathlib import Path

import pandas as pd

# prices.csv sits in the same folder as this file, wherever you run it from
PRICES = Path(__file__).parent / "prices.csv"


def daily_leaderboard(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Sort the rows by date, latest day first, and within each day by change_pct, largest first.

    Args:
        prices_df: one row per stock per day, with the columns ticker, date and
            change_pct (how much the stock rose that day, in percent).

    Returns:
        The same rows, in that order.

    Example:
        prices_df = pd.DataFrame({"ticker": ["KO", "KO", "F", "F"],
                                  "date": ["2025-09-02", "2025-09-03", "2025-09-02", "2025-09-03"],
                                  "change_pct": [1.5, -0.5, 2.0, 0.25]})
        daily_leaderboard(prices_df)
    returns
          ticker        date  change_pct
        3      F  2025-09-03        0.25
        1     KO  2025-09-03       -0.50
        2      F  2025-09-02        2.00
        0     KO  2025-09-02        1.50
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    prices_df = pd.read_csv(PRICES)
    # how much each stock rose from the open to the close, in percent
    prices_df["change_pct"] = (prices_df.close - prices_df.open) / prices_df.open * 100
    leaderboard_df = daily_leaderboard(prices_df)
    print(
        leaderboard_df[["date", "ticker", "change_pct"]].head(12).round(2).to_string()
    )
