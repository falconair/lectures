"""
PROBLEM 5
Practises: turning a table of daily prices into one row of features per stock, with groupby.

Task: fill in the function stock_features.

To check your work, type:
    python p5_stock_features.py

It should print the table that stock_features returned:
               vol  avg_range  avg_dollar_vol  beta
    ticker
    AAPL    0.0182     0.0180     14623674932  1.00
    JPM     0.0103     0.0170      2679405072  0.76
    KO      0.0065     0.0123      1246074589 -0.08
    MSFT    0.0102     0.0145     10265836345  0.84
    TSLA    0.0282     0.0365     37571290517  2.99
    XOM     0.0144     0.0167      1896541141  0.48
"""

from pathlib import Path

import pandas as pd

# daily_prices.csv sits in the same folder as this file, wherever you run it from
PRICES_FILE = Path(__file__).parent / "daily_prices.csv"


def load_prices() -> pd.DataFrame:
    """Return one row per stock per day of September 2025: date, ticker, high, low, close and volume."""
    return pd.read_csv(PRICES_FILE, parse_dates=["date"])


def stock_features(prices_df: pd.DataFrame) -> pd.DataFrame:
    """Return one row per stock, with four numbers that describe how it traded.

    A stock's daily return is its close divided by its own previous close,
    minus 1. The market return of a day is the average daily return of all
    the stocks in prices_df on that day.

    Args:
        prices_df: one row per stock per day, with the columns date, ticker,
            high, low, close and volume.

    Returns:
        A table with the ticker as the index and these columns:
            vol             the standard deviation of the stock's daily returns
            avg_range       the average of (high - low) / close
            avg_dollar_vol  the average of close * volume, in dollars
            beta            the covariance of the stock's daily return with
                            the market return, divided by the variance of
                            the market return
        For example, TSLA's row is vol 0.0282, avg_range 0.0365,
        avg_dollar_vol 37571290517 and beta 2.99: on a typical day TSLA
        moved about three times as much as the average of the six stocks.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    features_df = stock_features(load_prices())
    features_df["avg_dollar_vol"] = features_df["avg_dollar_vol"].round().astype("int64")
    print(features_df.round({"vol": 4, "avg_range": 4, "beta": 2}).to_string())
