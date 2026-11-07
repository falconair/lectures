"""
PROBLEM 3
Practises: treating number columns and text columns differently, with a
ColumnTransformer inside a Pipeline.

Task: fill in the function train_with_text_column.

To check your work, type:
    python p3_column_transformer.py

It prints the first 3 test stocks as the model sees them after the
ColumnTransformer, then the model's score on the test stocks beside the score of
always giving one answer. Yours may differ in the last digit:
             vol  avg_dollar_vol  last_price  tier_high  tier_low  tier_mid  tier_unknown  is_outlier
    ticker
    BRK.B  -0.41            0.50       -0.05        1.0       0.0       0.0           0.0         0.0
    BXP    -0.01           -0.28       -0.06        0.0       0.0       0.0           1.0         0.0
    AU      0.15           -0.26       -0.06        1.0       0.0       0.0           0.0         0.0
    test stocks        0.74
    always one answer  0.50
"""

from pathlib import Path

import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC

# stocks.csv sits in the same folder as this file, wherever you run it from
STOCKS_FILE = Path(__file__).parent / "stocks.csv"

# the number columns to scale: volatility, dollars traded in a day, the last price
NUMBER_COLUMNS = ["vol", "avg_dollar_vol", "last_price"]


def load_stocks() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index and a size column."""
    return pd.read_csv(STOCKS_FILE, index_col="ticker")


def train_with_text_column(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    """Train an SVC on a table of number, text and True/False columns.

    Use make_column_transformer as the lecture does, for three treatments:
        scale the NUMBER_COLUMNS with StandardScaler()
        one-hot encode liquidity_tier ("high", "mid", "low" or "unknown") with
            OneHotEncoder()
        keep every other column as it is, with remainder="passthrough"
    Put that first in a make_pipeline, then SVC(), and fit it.

    Args:
        X_train: the NUMBER_COLUMNS, liquidity_tier and is_outlier of the stocks
            to train on.
        y_train: the size of those stocks, "large" or "small".

    Returns:
        The trained Pipeline. Its first step, model[0], is the ColumnTransformer.

    Example:
        X_train = pd.DataFrame({"vol": [0.01, 0.03, 0.01, 0.03],
                                "avg_dollar_vol": [3e9, 1e9, 3e9, 1e9],
                                "last_price": [200.0, 100.0, 100.0, 200.0],
                                "liquidity_tier": ["high", "mid", "high", "unknown"],
                                "is_outlier": [False, False, True, False]})
        y_train = pd.Series(["large", "small", "large", "small"])
        model = train_with_text_column(X_train, y_train)
        model[0].transform(X_train)
    returns
        array([[-1.,  1.,  1.,  1.,  0.,  0.,  0.],
               [ 1., -1., -1.,  0.,  1.,  0.,  0.],
               [-1.,  1., -1.,  1.,  0.,  0.,  1.],
               [ 1., -1.,  1.,  0.,  0.,  1.,  0.]])
    The three scaled numbers come first, then one column per tier in X_train
    (high, mid, unknown), then is_outlier as it was (True is 1).
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    stocks_df = load_stocks()
    X_train, X_test, y_train, y_test = train_test_split(
        stocks_df[NUMBER_COLUMNS + ["liquidity_tier", "is_outlier"]],
        stocks_df["size"],
        test_size=0.30,
        random_state=0,
        stratify=stocks_df["size"],
    )
    model = train_with_text_column(X_train, y_train)
    seen = pd.DataFrame(
        model[0].transform(X_test[:3]),
        columns=[
            name.split("__")[-1].replace("liquidity_tier_", "tier_")
            for name in model[0].get_feature_names_out()
        ],
        index=X_test.index[:3],
    )
    print(seen.round(2).to_string())
    print(f"test stocks        {model.score(X_test, y_test):.2f}")
    print(f"always one answer  {y_test.value_counts(normalize=True).max():.2f}")
