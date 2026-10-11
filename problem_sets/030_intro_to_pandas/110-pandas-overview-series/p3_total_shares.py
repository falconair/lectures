"""
PROBLEM 3
Practises: adding two Series that do not hold the same labels.

Task: fill in the function total_shares.

To check your work, type:
    python p3_total_shares.py

It should print what total_shares returned for the two accounts at the bottom of this file:
    F       300.0
    JPM     160.0
    NVDA     65.0
    XOM     500.0
"""

import pandas as pd


def total_shares(account_a: pd.Series, account_b: pd.Series) -> pd.Series:
    """Return how many shares of each stock two accounts hold together.

    A stock held in only one account keeps that account's number of shares.

    Args:
        account_a: shares held in one account, with the ticker as the index.
        account_b: the same for another account. It may hold different stocks.

    Returns:
        A Series with every ticker of either account and the shares held in
        total, as decimal numbers. No entry is missing (NaN).

    Example:
        account_a = pd.Series([100, 50], index=["AAPL", "KO"])
        account_b = pd.Series([20, 70], index=["KO", "TSLA"])
        total_shares(account_a, account_b)
    returns
        AAPL    100.0
        KO       70.0
        TSLA     70.0
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    account_a = pd.Series([300, 150, 40], index=["F", "JPM", "NVDA"])
    account_b = pd.Series([25, 500, 10], index=["NVDA", "XOM", "JPM"])
    print(total_shares(account_a, account_b).to_string())
