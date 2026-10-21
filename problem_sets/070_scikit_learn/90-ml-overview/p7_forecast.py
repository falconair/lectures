"""
PROBLEM 7
Practises: splitting a time series by time, and comparing a forecast with a naive one.

Task: fill in the function forecast_last_minutes.

To check your work, type:
    python p7_forecast.py

It should print the first 5 rows of the table that forecast_last_minutes
returned, and how far each forecast was from the actual prices (the root
mean squared error, smaller is better). Yours may differ in the last digit:
                         actual   naive  regression
    minute
    2025-09-10 19:30:00  226.08  226.18      226.19
    2025-09-10 19:31:00  226.04  226.18      226.19
    2025-09-10 19:32:00  226.24  226.18      226.20
    2025-09-10 19:33:00  226.26  226.18      226.22
    2025-09-10 19:34:00  226.15  226.18      226.22
    error: naive 0.40, regression 0.26
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

# aapl_minutes.csv sits in the same folder as this file, wherever you run it from
PRICES_FILE = Path(__file__).parent / "aapl_minutes.csv"


def load_prices() -> pd.Series:
    """Return AAPL's last trade price in each minute of 10 September 2025, indexed by the minute (UTC)."""
    return pd.read_csv(PRICES_FILE, index_col="minute", parse_dates=True)["price"]


def regression_forecast(past: pd.Series, horizon: int) -> list[float]:
    """Given: forecast the next `horizon` prices after `past`, one minute at a time.

    A linear regression learns the next price from the 10 prices before it.
    Each forecast is then used as an input for the next one. This is what the
    lecture's RegressionForecaster(window=10, regressor=LinearRegression()) does.
    """
    window = 10
    values = past.to_numpy(float)
    X = np.array([values[i:i + window] for i in range(len(values) - window)])
    model = LinearRegression().fit(X, values[window:])
    history = list(values)
    for _ in range(horizon):
        history.append(float(model.predict(np.array([history[-window:]]))[0]))
    return history[len(values):]


def forecast_last_minutes(prices: pd.Series, horizon: int) -> pd.DataFrame:
    """Hold back the last `horizon` minutes as the "future", and forecast them from the minutes before.

    The split is by time: the past is every minute before the last `horizon`
    minutes. A random split would let the model see minutes that come after
    the ones it forecasts. Make two forecasts of the future from the past only:

        naive       the last price of the past, repeated
        regression  regression_forecast(past, horizon), given above

    Args:
        prices: one price per minute, in time order, indexed by the minute.
        horizon: how many minutes to hold back and forecast.

    Returns:
        A table with one row per held-back minute, indexed by the minute, and
        the columns actual (the real price), naive and regression. For
        example, with the 390 minutes of the day and a horizon of 30, the
        past ends at 19:29, when the price was 226.18, so the first row is
        19:30 with actual 226.08, naive 226.18 and regression 226.19.
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    forecasts_df = forecast_last_minutes(load_prices(), 30)
    print(forecasts_df.head(5).round(2).to_string())
    naive_error = root_mean_squared_error(forecasts_df["actual"], forecasts_df["naive"])
    regression_error = root_mean_squared_error(forecasts_df["actual"], forecasts_df["regression"])
    print(f"error: naive {naive_error:.2f}, regression {regression_error:.2f}")
