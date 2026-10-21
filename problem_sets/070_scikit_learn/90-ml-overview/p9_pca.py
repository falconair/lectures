"""
PROBLEM 9
Practises: scaling the columns before PCA, and reading how many columns are worth keeping.

Task: fill in the function cumulative_variance.

To check your work, type:
    python p9_pca.py

It should print what cumulative_variance returned, then how many PCA
columns keep 90% of the variance. Yours may differ in the last digit:
    1    0.389
    2    0.600
    3    0.734
    4    0.862
    5    0.957
    6    0.994
    7    1.000
    8    1.000
    5 of the 8 columns keep 90% of the variance
"""

from pathlib import Path

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# features.csv sits in the same folder as this file, wherever you run it from
FEATURES_FILE = Path(__file__).parent / "features.csv"

# the columns a model may learn from
FEATURES = ["mean_ret", "vol", "total_ret", "avg_range", "max_abs_move", "avg_dollar_vol", "last_price", "beta"]


def load_features() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index: the FEATURES columns, market_cap and is_outlier."""
    return pd.read_csv(FEATURES_FILE, index_col="ticker")


def cumulative_variance(features_df: pd.DataFrame) -> pd.Series:
    """Return the share of the variance kept by the first 1, 2, 3, ... PCA columns.

    First scale the FEATURES columns with StandardScaler: avg_dollar_vol is
    in the billions and vol is around 0.02, and unscaled the first PCA
    column would be avg_dollar_vol alone. Then fit PCA() to the scaled
    columns. Its explained_variance_ratio_ is the share of the variance
    in each PCA column, largest first.

    Args:
        features_df: one row per stock, with the FEATURES columns and others.

    Returns:
        A Series indexed 1, 2, ... up to the number of FEATURES columns.
        The value at k is the share of the variance kept by the first k PCA
        columns, from 0.0 to 1.0, so the last value is 1.0. For example,
        for the stocks of features.csv without the outliers, the value at 1
        is 0.389 and the value at 5 is 0.957. A value of 1.000 at 1 means
        the columns were not scaled.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    features_df = load_features()
    features_df = features_df[~features_df["is_outlier"]]  # leave out the 25 most unusual stocks, as the lecture does
    kept = cumulative_variance(features_df)
    print(kept.round(3).to_string())
    print(f"{(kept < 0.9).sum() + 1} of the {len(FEATURES)} columns keep 90% of the variance")
