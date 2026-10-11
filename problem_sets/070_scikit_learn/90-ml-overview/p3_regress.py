"""
PROBLEM 3
Practises: taking the log of a skewed target before training a regression model.

Task: fill in the function train_market_cap_model.

To check your work, type:
    python p3_regress.py

It trains your model, then prints three stocks the model has not seen: what
the model predicts for each, and the log of its real market cap. Your
predictions may differ in the last digit:
            predicted   real
    ticker
    MDLZ        10.59  10.83
    ZTS         10.52  10.62
    GOOG        11.51  11.90
"""

from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# features.csv sits in the same folder as this file, wherever you run it from
FEATURES_FILE = Path(__file__).parent / "features.csv"

# the columns a model may learn from
FEATURES = ["mean_ret", "vol", "total_ret", "avg_range", "max_abs_move", "avg_dollar_vol", "last_price", "beta"]


def load_features() -> pd.DataFrame:
    """Return one row per stock, with the ticker as the index: the FEATURES columns, market_cap and is_outlier."""
    return pd.read_csv(FEATURES_FILE, index_col="ticker")


def train_market_cap_model(X_train: pd.DataFrame, market_cap_train: pd.Series) -> RandomForestRegressor:
    """Train a random forest to predict the log (base 10) of a stock's market cap.

    Market cap is very skewed: a few companies are hundreds of times larger
    than most. So the model is trained on np.log10 of the market cap, not on
    the market cap itself.

    Use RandomForestRegressor(n_estimators=100, random_state=0).

    Args:
        X_train: the features of the stocks to train on.
        market_cap_train: the market cap of those same stocks, in dollars.

    Returns:
        The trained model. Its predictions are logs: 10.0 means 10 billion
        dollars, 11.0 means 100 billion.

    A quick check of your own: the model's predictions for any stocks should
    all be between about 7 and 12. Predictions in the billions mean the model
    was trained on market cap itself.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    features_df = load_features()
    X_train, X_test, market_cap_train, market_cap_test = train_test_split(
        features_df[FEATURES], features_df["market_cap"], test_size=0.30, random_state=0
    )
    model = train_market_cap_model(X_train, market_cap_train)
    report_df = pd.DataFrame(
        {"predicted": model.predict(X_test[:3]), "real": np.log10(market_cap_test[:3])}, index=X_test.index[:3]
    )
    print(report_df.round(2).to_string())
