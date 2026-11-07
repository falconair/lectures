"""
PROBLEM 3
Practises: adding up repeated rows first, because pivot needs one row for each cell of the table.

Task: fill in the function shares_by_side.

To check your work, type:
    python p3_shares_by_side.py

It should print what shares_by_side returned for the AAPL and MSFT orders filled on 2025-09-10:
    side      buy  sell
    symbol
    AAPL    10856  6442
    MSFT      583   173
"""

from pathlib import Path

import pandas as pd

# executions.csv sits in the same folder as this file, wherever you run it from.
# It holds the AAPL and MSFT orders filled on 2025-09-10, read from a FIX log:
# one row per order, each filled in full.
EXECUTIONS = Path(__file__).parent / "executions.csv"
# the side field of a FIX message (tag 54): 1 is a buy, 2 a sale, 5 a short sale
SIDES = {1: "buy", 2: "sell", 5: "sell"}


def shares_by_side(executions_df: pd.DataFrame) -> pd.DataFrame:
    """Return how many shares were bought and how many sold, for each symbol.

    Args:
        executions_df: one row per filled order, with the columns symbol, side and
            order_qty. side is "buy" or "sell"; order_qty is the number of shares
            in the order.

    Returns:
        A table whose index is the symbol, with one column per side: buy and
        sell. Each value is the total number of shares.

    Example:
        executions_df = pd.DataFrame({"symbol": ["AAPL", "MSFT", "AAPL", "AAPL", "MSFT"],
                                      "side": ["buy", "sell", "buy", "sell", "buy"],
                                      "order_qty": [10, 5, 30, 20, 1]})
        shares_by_side(executions_df)
    returns
        side    buy  sell
        symbol
        AAPL     40    20
        MSFT      1     5
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    executions_df = pd.read_csv(EXECUTIONS)
    executions_df["side"] = executions_df["side"].map(SIDES)
    print(shares_by_side(executions_df).to_string())
