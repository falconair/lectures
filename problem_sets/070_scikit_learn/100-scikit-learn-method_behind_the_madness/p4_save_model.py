"""
PROBLEM 4
Practises: saving a trained model to a file and loading it back.

Task: fill in the functions save_model and load_and_predict.

To check your work, type:
    python p4_save_model.py

It trains a Pipeline, saves it to the file model.joblib in this folder, loads it
back, and prints for three test stocks the prediction before saving, the
prediction after loading, and the real size. The first two columns must match:
           before saving after loading   real
    ticker
    BRK.B          large         large  large
    BXP            small         small  small
    AU             small         small  small
"""

from pathlib import Path

from joblib import dump, load
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import PowerTransformer
from sklearn.svm import SVC

# stocks.csv sits in the same folder as this file, wherever you run it from
STOCKS_FILE = Path(__file__).parent / "stocks.csv"
MODEL_FILE = Path(__file__).parent / "model.joblib"

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


def save_model(model: Pipeline, path: str) -> None:
    """Save a whole trained Pipeline, transformers included, with joblib's dump.

    Args:
        model: a trained Pipeline.
        path: the name of the file to write, such as "model.joblib".

    Returns:
        Nothing. Afterwards the file at path holds the model.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


def load_and_predict(path: str, X: pd.DataFrame) -> np.ndarray:
    """Load a saved Pipeline with joblib's load and return its predictions for X.

    Args:
        path: the name of a file written by save_model.
        X: the rows to predict, in the form the model was trained on.

    Returns:
        One prediction per row of X. For example, for the file the program
        saves and the first three test stocks, load_and_predict returns
            ['large' 'small' 'small']
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
    model = make_pipeline(
        SimpleImputer(strategy="median"), PowerTransformer(), SVC()
    ).fit(X_train, y_train)
    before_saving = model.predict(X_test[:3])
    save_model(model, str(MODEL_FILE))
    del model  # from here on the only copy of the model is the one in the file
    report_df = pd.DataFrame(
        {
            "before saving": before_saving,
            "after loading": load_and_predict(str(MODEL_FILE), X_test[:3]),
            "real": y_test[:3],
        }
    )
    print(report_df.to_string())
