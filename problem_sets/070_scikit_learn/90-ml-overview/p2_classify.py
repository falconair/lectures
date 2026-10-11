"""
PROBLEM 2
Practises: training a classifier and measuring it on rows it has not seen.

Task: fill in the function tier_accuracy.

To check your work, type:
    python p2_classify.py

It should print the accuracy that tier_accuracy returned. Yours may differ in
the last digit:
    accuracy 0.70
"""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# features.csv sits in the same folder as this file, wherever you run it from
FEATURES_FILE = Path(__file__).parent / "features.csv"

# the columns a model may learn from
FEATURES = ["mean_ret", "vol", "total_ret", "avg_range", "max_abs_move", "avg_dollar_vol", "last_price", "beta"]


def load_features() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index: the FEATURES columns, market_cap and is_outlier."""
    return pd.read_csv(FEATURES_FILE, index_col="ticker")


def tier_accuracy(X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series) -> float:
    """Train a random forest to predict a stock's size tier, and return its accuracy.

    Use RandomForestClassifier(n_estimators=100, random_state=0). Train it on
    the train part only. Measure it on the test part only.

    Args:
        X_train, y_train: the features and the tier ("small", "mid" or "large") of the stocks to train on.
        X_test, y_test: the same for the stocks held back for testing.

    Returns:
        The share of the test stocks whose tier the model predicted correctly,
        from 0.0 to 1.0.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
def load_tiers() -> tuple[pd.DataFrame, pd.Series]:
    """Return the FEATURES table and each stock's tier: the smallest, middle and largest third by market cap."""
    features_df = load_features()
    tiers = pd.qcut(features_df["market_cap"], 3, labels=["small", "mid", "large"])
    return features_df[FEATURES], tiers


if __name__ == "__main__":
    X, tiers = load_tiers()
    X_train, X_test, y_train, y_test = train_test_split(X, tiers, test_size=0.30, random_state=0, stratify=tiers)
    print(f"accuracy {tier_accuracy(X_train, X_test, y_train, y_test):.2f}")
