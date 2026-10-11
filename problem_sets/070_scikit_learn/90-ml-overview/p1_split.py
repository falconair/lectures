"""
PROBLEM 1
Practises: holding back part of the data, so that a model is tested on rows it has not seen.

Task: fill in the function split.

To check your work, type:
    python p1_split.py

It should print how many rows are in each of the four tables that split returned:
    X_train 345, X_test 148, y_train 345, y_test 148
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

# features.csv sits in the same folder as this file, wherever you run it from
FEATURES_FILE = Path(__file__).parent / "features.csv"

# the columns a model may learn from
FEATURES = ["mean_ret", "vol", "total_ret", "avg_range", "max_abs_move", "avg_dollar_vol", "last_price", "beta"]


def load_features() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index: the FEATURES columns, market_cap and is_outlier."""
    return pd.read_csv(FEATURES_FILE, index_col="ticker")


def split(features_df: pd.DataFrame, target: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split the stocks into a part to train on and a part to test on.

    Hold back 30% of the rows for testing. Use random_state=0, so that the
    same rows are held back every time.

    Args:
        features_df: one row per stock, with the FEATURES columns and others.
        target: what the model will predict, one value per stock.

    Returns:
        X_train, X_test, y_train, y_test. The X tables hold only the FEATURES
        columns. No stock is in both the train part and the test part.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    features_df = load_features()
    X_train, X_test, y_train, y_test = split(features_df, features_df["market_cap"])
    print(f"X_train {len(X_train)}, X_test {len(X_test)}, y_train {len(y_train)}, y_test {len(y_test)}")
