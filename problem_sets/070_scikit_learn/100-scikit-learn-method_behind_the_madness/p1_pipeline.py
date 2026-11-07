"""
PROBLEM 1
Practises: fitting transformers on the training rows only, by hand and then
with a Pipeline.

Task: fill in the functions fill_and_scale and train_pipeline.

To check your work, type:
    python p1_pipeline.py

It trains an SVC to say whether a stock's market cap is above the median
("large") or not ("small"), and prints its score on the test stocks, by hand and
with your Pipeline, beside the score of always giving one answer. The scores by
hand and with the pipeline must be the same. Yours may differ in the last digit:
    always one answer  0.50
    by hand            0.72
    pipeline           0.72
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# stocks.csv sits in the same folder as this file, wherever you run it from
STOCKS_FILE = Path(__file__).parent / "stocks.csv"

# the columns a model may learn from. adv (shares traded in a day) is blank for the
# 237 of the 493 stocks that have no row in the course's symbol_reference.csv
FEATURES = [
    "mean_ret",
    "vol",
    "total_ret",
    "avg_range",
    "max_abs_move",
    "avg_dollar_vol",
    "last_price",
    "beta",
    "adv",
]


def load_stocks() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index and a size column."""
    return pd.read_csv(STOCKS_FILE, index_col="ticker")


def fill_and_scale(
    X_train: pd.DataFrame, X_test: pd.DataFrame
) -> tuple[np.ndarray, np.ndarray]:
    """Fill the gaps and scale the numbers, learning only from the training rows.

    Fill each gap with its column's median, with SimpleImputer(strategy="median").
    Then scale with StandardScaler(). Fit both on X_train only, and use them on
    X_test with transform: the test rows must have no say in the numbers.

    Args:
        X_train: the rows to train on. Some cells are blank (NaN).
        X_test: the rows held back for testing, with the same columns.

    Returns:
        Two arrays, the filled and scaled X_train and X_test.

    Example:
        X_train = pd.DataFrame({"adv": [7.0, 9.0, np.nan, 11.0, 13.0]})
        X_test = pd.DataFrame({"adv": [12.0, np.nan]})
        fill_and_scale(X_train, X_test)
    returns
        (array([[-1.5], [-0.5], [ 0. ], [ 0.5], [ 1.5]]), array([[1.], [0.]]))
    The training median is 10.0, so both gaps become 10.0. With the gap filled,
    the training mean is 10.0 and the standard deviation 2.0: 12.0 becomes 1.0.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def train_pipeline(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    """Train a Pipeline that fills, scales and classifies in one object.

    Use make_pipeline with the same two transformers as fill_and_scale, then
    SVC(). Fit it on the training rows.

    Args:
        X_train: the rows to train on, with their gaps. The Pipeline fills them.
        y_train: the size of those stocks, "large" or "small".

    Returns:
        The trained Pipeline. It takes a table with gaps, as X_train was.

    Example:
        X_train = pd.DataFrame({"adv": [1.0, 2.0, np.nan, 8.0, 9.0]})
        y_train = pd.Series(["small", "small", "small", "large", "large"])
        model = train_pipeline(X_train, y_train)
        model.predict(pd.DataFrame({"adv": [1.5, 8.5, np.nan]}))
    returns
        array(['small', 'large', 'small'], dtype=object)
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    stocks_df = load_stocks()
    X_train, X_test, y_train, y_test = train_test_split(
        stocks_df[FEATURES],
        stocks_df["size"],
        test_size=0.30,
        random_state=0,
        stratify=stocks_df["size"],
    )
    train_filled, test_filled = fill_and_scale(X_train, X_test)
    by_hand = SVC().fit(train_filled, y_train).score(test_filled, y_test)
    model = train_pipeline(X_train, y_train)
    print(f"always one answer  {y_test.value_counts(normalize=True).max():.2f}")
    print(f"by hand            {by_hand:.2f}")
    print(f"pipeline           {model.score(X_test, y_test):.2f}")
