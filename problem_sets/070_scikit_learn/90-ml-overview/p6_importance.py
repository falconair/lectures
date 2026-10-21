"""
PROBLEM 6
Practises: asking a trained model which columns it relied on.

Task: fill in the function feature_importance.

To check your work, type:
    python p6_importance.py

It trains the market cap model of problem 3, then prints what
feature_importance returned. Yours may differ in the last digit:
    avg_range         0.498
    avg_dollar_vol    0.287
    last_price        0.045
    vol               0.041
    beta              0.038
    mean_ret          0.034
    max_abs_move      0.029
    total_ret         0.027
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# features.csv sits in the same folder as this file, wherever you run it from
FEATURES_FILE = Path(__file__).parent / "features.csv"

# the columns a model may learn from
FEATURES = ["mean_ret", "vol", "total_ret", "avg_range", "max_abs_move", "avg_dollar_vol", "last_price", "beta"]


def load_features() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index: the FEATURES columns, market_cap and is_outlier."""
    return pd.read_csv(FEATURES_FILE, index_col="ticker")


def feature_importance(model: RandomForestRegressor, feature_names: list[str]) -> pd.Series:
    """Return how much the trained model relied on each column, most important first.

    A trained random forest keeps one importance per column in its
    feature_importances_ attribute, in the order of the columns it was
    trained on. The importances add up to 1.

    Args:
        model: a random forest that has been trained.
        feature_names: the names of the columns it was trained on, in order.

    Returns:
        A Series with one value per column, indexed by the column's name,
        sorted from the largest importance to the smallest. For example,
        for the model of problem 3 the first value is avg_range, 0.498:
        about half of what the model learned came from that column.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    features_df = load_features()
    X_train, _, market_cap_train, _ = train_test_split(
        features_df[FEATURES], features_df["market_cap"], test_size=0.30, random_state=0
    )
    model = RandomForestRegressor(n_estimators=100, random_state=0).fit(X_train, np.log10(market_cap_train))
    print(feature_importance(model, FEATURES).round(3).to_string())
