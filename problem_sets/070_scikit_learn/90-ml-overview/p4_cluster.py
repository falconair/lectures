"""
PROBLEM 4
Practises: scaling the columns before clustering, so that no column decides the result by its size.

Task: fill in the function cluster_stocks.

To check your work, type:
    python p4_cluster.py

It should print how many stocks are in each of the 3 clusters that
cluster_stocks made, largest first:
    [290, 119, 59]
"""

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# features.csv sits in the same folder as this file, wherever you run it from
FEATURES_FILE = Path(__file__).parent / "features.csv"

# the columns a model may learn from
FEATURES = ["mean_ret", "vol", "total_ret", "avg_range", "max_abs_move", "avg_dollar_vol", "last_price", "beta"]


def load_features() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index: the FEATURES columns, market_cap and is_outlier."""
    return pd.read_csv(FEATURES_FILE, index_col="ticker")


def cluster_stocks(features_df: pd.DataFrame, n_clusters: int) -> pd.Series:
    """Put each stock in one of n_clusters groups of similar stocks.

    First scale the FEATURES columns with StandardScaler: avg_dollar_vol is
    in the billions and vol is around 0.02, and unscaled the clusters would
    depend on avg_dollar_vol alone. Then cluster the scaled columns with
    KMeans(n_clusters=n_clusters, random_state=0, n_init=10).

    Args:
        features_df: one row per stock, with the FEATURES columns and others.
        n_clusters: how many clusters to make.

    Returns:
        A Series with the same index as features_df: each stock's cluster,
        a whole number from 0 to n_clusters - 1.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    features_df = load_features()
    features_df = features_df[~features_df["is_outlier"]]  # leave out the 25 most unusual stocks, as the lecture does
    clusters = cluster_stocks(features_df, 3)
    print(sorted(clusters.value_counts().tolist(), reverse=True))
