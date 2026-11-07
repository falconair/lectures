"""
PROBLEM 1
Practises: making a DataFrame with labels for its rows and its columns.

Task: fill in the function closes_table.

To check your work, type:
    python p1_closes_table.py

It should print what closes_table returned for the closes at the bottom of this file:
                  AAPL    MSFT    NVDA
    2025-09-02  229.72  505.12  170.78
    2025-09-03  238.47  505.35  170.62
    2025-09-04  239.78  507.97  171.66
    2025-09-05  239.69  495.00  167.02
"""

import pandas as pd


def closes_table(
    closes: list[list[float]], dates: list[str], tickers: list[str]
) -> pd.DataFrame:
    """Return a table of closing prices with one row per date and one column per ticker.

    Args:
        closes: one list per date; each holds the closes of the stocks, in the order of tickers.
        dates: the date of each of those lists, as text.
        tickers: the ticker of each column.

    Returns:
        A table of the closes whose index is the date and whose columns are the tickers.

    Example:
        closes_table([[67.5, 11.25], [68.0, 11.5]], ["2025-09-02", "2025-09-03"], ["KO", "F"])
    returns
                      KO      F
        2025-09-02  67.5  11.25
        2025-09-03  68.0  11.50
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    # the closes of AAPL, MSFT and NVDA in the first week of September 2025, from prices.csv
    tickers = ["AAPL", "MSFT", "NVDA"]
    dates = ["2025-09-02", "2025-09-03", "2025-09-04", "2025-09-05"]
    closes = [
        [229.72, 505.12, 170.78],
        [238.47, 505.35, 170.62],
        [239.78, 507.97, 171.66],
        [239.69, 495.00, 167.02],
    ]
    print(closes_table(closes, dates, tickers).to_string())
