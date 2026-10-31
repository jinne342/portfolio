"""Synthetic datasets with the same structure as the four lab reports."""
from __future__ import annotations

import numpy as np
import pandas as pd

RNG = np.random.default_rng(2024)


def insurance(n: int = 18) -> pd.DataFrame:
    """Life-insurance purchase vs annual income and risk aversion."""
    income = np.linspace(20, 80, n)
    risk = RNG.integers(1, 11, n).astype(float)
    y = 2.2 * income + 1.8 * risk**2 - 0.02 * income**2 + RNG.normal(0, 6, n) + 30
    return pd.DataFrame({"income": income.round(1), "risk": risk, "purchase": y.round(2)})


def monthly_sales(n: int = 48) -> pd.DataFrame:
    """Monthly sales with linear trend and 12-month seasonality."""
    t = np.arange(1, n + 1)
    seasonal = 12 * np.sin(2 * np.pi * t / 12) + 6 * np.cos(2 * np.pi * t / 12)
    y = 100 + 1.8 * t + seasonal + RNG.normal(0, 3, n)
    return pd.DataFrame({"period": t, "sales": y.round(2)})


def ar_series(n: int = 200, phi: float = 0.6) -> pd.DataFrame:
    """Stationary AR(1) series for ACF/PACF and ARMA practice."""
    y = np.zeros(n)
    for i in range(1, n):
        y[i] = phi * y[i - 1] + RNG.normal(0, 1)
    return pd.DataFrame({"t": np.arange(1, n + 1), "value": y.round(4)})


def seasonal_series(n: int = 60) -> pd.DataFrame:
    """Trend + multiplicative-ish seasonality for SARIMA practice."""
    t = np.arange(1, n + 1)
    y = 50 + 0.5 * t + 8 * np.sin(2 * np.pi * t / 12) + RNG.normal(0, 2, n)
    return pd.DataFrame({"period": t, "value": y.round(3)})
