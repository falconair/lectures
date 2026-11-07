"""
PROBLEM 2
Practises: grid search over a whole pipeline, with step__parameter names.

Task: fill in the function tune_pipeline.

To check your work, type:
    python p2_grid_search.py

It prints the best settings tune_pipeline found, their score across the five
folds of the training stocks, their score on the test stocks, and the score of
always giving one answer. Yours may differ in the last digit:
    best settings      {'simpleimputer__strategy': 'mean', 'svc__C': 1, 'svc__kernel': 'rbf'}
    across the folds   0.83
    test stocks        0.80
    always one answer  0.50
"""

from pathlib import Path

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PowerTransformer
from sklearn.svm import SVC

# stocks.csv sits in the same folder as this file, wherever you run it from
STOCKS_FILE = Path(__file__).parent / "stocks.csv"

# the columns a model may learn from. adv (shares traded in a day) has gaps
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


def tune_pipeline(X_train: pd.DataFrame, y_train: pd.Series) -> GridSearchCV:
    """Search for the best settings of a whole pipeline, transformers included.

    The pipeline is make_pipeline(SimpleImputer(), PowerTransformer(), SVC()).
    Search it with GridSearchCV over all the combinations of:
        the strategy of the SimpleImputer: "mean" or "median"
        the C of the SVC: 0.1, 1 or 10
        the kernel of the SVC: "rbf" or "linear"
    Name each setting as the lecture does: the step, two underscores, the
    parameter. make_pipeline calls each step by its class name in lower case.

    Args:
        X_train: the rows to train on, with their gaps.
        y_train: the size of those stocks, "large" or "small".

    Returns:
        The fitted GridSearchCV. For the program's training stocks,
        tune_pipeline(X_train, y_train).best_params_ is
            {'simpleimputer__strategy': 'mean', 'svc__C': 1, 'svc__kernel': 'rbf'}
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
    search = tune_pipeline(X_train, y_train)
    print(f"best settings      {search.best_params_}")
    print(f"across the folds   {search.best_score_:.2f}")
    print(f"test stocks        {search.score(X_test, y_test):.2f}")
    print(f"always one answer  {y_test.value_counts(normalize=True).max():.2f}")
