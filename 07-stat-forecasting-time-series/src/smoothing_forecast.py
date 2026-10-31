"""Lab 2: moving average, exponential smoothing, Holt and Holt-Winters."""
from __future__ import annotations

import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from data import monthly_sales


def mape(y_true, y_pred) -> float:
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    return float(np.mean(np.abs((y_true - y_pred) / y_true)) * 100)


def main() -> None:
    df = monthly_sales()
    y = df["sales"].values
    horizon = 6
    train, test = y[:-horizon], y[-horizon:]

    # one-step-ahead moving average (window=3) using observed history
    ma_pred = [np.mean(y[i - 3 : i]) for i in range(len(train), len(y))]

    # simple exponential smoothing: grid search alpha on the training set
    best_alpha, best_mape = 0.5, float("inf")
    for alpha in np.arange(0.1, 0.95, 0.05):
        level = train[0]
        fitted = []
        for actual in train[1:]:
            fitted.append(level)
            level = alpha * actual + (1 - alpha) * level
        score = mape(train[1:], fitted)
        if score < best_mape:
            best_alpha, best_mape = alpha, score
    level = train[0]
    ses_pred = []
    for actual in train[1:]:
        level = best_alpha * actual + (1 - best_alpha) * level
    for _ in range(horizon):
        ses_pred.append(level)

    holt = ExponentialSmoothing(train, trend="add", seasonal=None, initialization_method="estimated").fit()
    holt_pred = holt.forecast(horizon)

    hw = ExponentialSmoothing(
        train, trend="add", seasonal="add", seasonal_periods=12, initialization_method="estimated"
    ).fit()
    hw_pred = hw.forecast(horizon)

    rows = []
    for name, pred in [
        ("移动平均 MA(3)", ma_pred),
        (f"一次指数平滑 α={best_alpha:.2f}", ses_pred),
        ("Holt 线性趋势", holt_pred),
        ("Holt-Winters 季节", hw_pred),
    ]:
        rows.append({"model": name, "MAPE_%": round(mape(test, pred), 2)})
    result = pd.DataFrame(rows).sort_values("MAPE_%")
    print("=== out-of-sample comparison (last 6 periods) ===")
    print(result.to_string(index=False))
    print("\nforecast next 6 (Holt-Winters):")
    print(np.round(hw_pred, 2))


if __name__ == "__main__":
    main()
