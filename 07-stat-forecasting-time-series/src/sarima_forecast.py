"""Lab 4: seasonal decomposition, SARIMA model and 5-step forecast."""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX

from data import seasonal_series

warnings.filterwarnings("ignore")


def mape(y_true, y_pred) -> float:
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    return float(np.mean(np.abs((y_true - y_pred) / y_true)) * 100)


def main() -> None:
    s = seasonal_series()["value"]
    horizon = 5
    train, test = s[:-horizon], s[-horizon:]

    dec = seasonal_decompose(train, model="additive", period=12)
    print("=== decomposition (first 12 observed / trend) ===")
    print(pd.DataFrame({"observed": train[:12], "trend": dec.trend[:12], "seasonal": dec.seasonal[:12]}).round(2).to_string(index=False))

    model = SARIMAX(
        train,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)
    print(f"\nAIC={model.aic:.2f}  BIC={model.bic:.2f}")

    forecast = model.get_forecast(horizon)
    pred = forecast.predicted_mean
    ci = forecast.conf_int(alpha=0.05)

    print("\n=== 5-step forecast ===")
    out = pd.DataFrame(
        {
            "period": range(len(train) + 1, len(train) + horizon + 1),
            "forecast": np.round(pred, 2),
            "lower": np.round(ci.iloc[:, 0], 2),
            "upper": np.round(ci.iloc[:, 1], 2),
            "actual": np.round(test, 2),
        }
    )
    print(out.to_string(index=False))
    print(f"\nMAPE = {mape(test, pred):.2f}%")


if __name__ == "__main__":
    main()
