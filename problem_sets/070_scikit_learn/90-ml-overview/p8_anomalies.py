"""
PROBLEM 8
Practises: finding the rows that are unlike the rest, with an isolation forest.

Task: fill in the function find_anomalies.

To check your work, type:
    python p8_anomalies.py

It should print the stocks that find_anomalies marked True, with four of
their columns. Yours may differ a little:
              vol  total_ret  max_abs_move  last_price
    ticker
    AEO     0.092      0.266         0.380       17.11
    BE      0.067      0.647         0.149       84.57
    LAC     0.226      1.018         0.958        5.71
    LEU     0.061      0.521         0.141      310.07
    MARA    0.052      0.137         0.157       18.26
    ORCL    0.088      0.248         0.359      281.24
    QURE    0.556      2.432         2.477       58.37
    SNPS    0.095     -0.167         0.358      493.39
    TSLA    0.028      0.350         0.074      444.72
    UUUU    0.054      0.351         0.158       15.35
"""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import IsolationForest

# features.csv sits in the same folder as this file, wherever you run it from
FEATURES_FILE = Path(__file__).parent / "features.csv"

# the columns a model may learn from
FEATURES = ["mean_ret", "vol", "total_ret", "avg_range", "max_abs_move", "avg_dollar_vol", "last_price", "beta"]


def load_features() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index: the FEATURES columns, market_cap and is_outlier."""
    return pd.read_csv(FEATURES_FILE, index_col="ticker")


def find_anomalies(features_df: pd.DataFrame, share: float) -> pd.Series:
    """Mark the stocks that are most unlike the others.

    Use IsolationForest(contamination=share, random_state=0), trained on
    all the rows of features_df. Its predict method returns -1 for an
    anomaly and 1 for a usual row.

    Args:
        features_df: one row per stock, with the FEATURES columns only.
        share: the share of the stocks to mark, from 0.0 to 0.5.

    Returns:
        A Series with the same index as features_df: True for each stock
        that is an anomaly, False for the others. For example, with the
        493 stocks of features.csv and a share of 0.02, 10 stocks are True.
        One is QURE, whose price rose 243% in the month (total_ret 2.432).
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    features_df = load_features()[FEATURES]
    anomalies = find_anomalies(features_df, 0.02)
    print(features_df[anomalies][["vol", "total_ret", "max_abs_move", "last_price"]].round(3).to_string())
