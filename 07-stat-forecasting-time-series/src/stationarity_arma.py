"""Lab 3: stationarity, white-noise tests, ACF/PACF and ARMA modelling."""
from __future__ import annotations

import numpy as np
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf, adfuller, pacf

from data import ar_series


def main() -> None:
    s = ar_series()["value"]

    adf_stat, adf_p, used_lag, nobs, crit, _ = adfuller(s, autolag="AIC")
    print("=== ADF test ===")
    print(f"statistic={adf_stat:.4f}  p-value={adf_p:.4f}  lags={used_lag}  nobs={nobs}")
    print("critical values:", {k: round(v, 4) for k, v in crit.items()})
    print("stationary" if adf_p < 0.05 else "non-stationary")

    print("\n=== ACF / PACF (lags 1-6) ===")
    for lag in range(1, 7):
        print(f"lag {lag}: acf={acf(s, nlags=lag)[lag]: .4f}  pacf={pacf(s, nlags=lag)[lag]: .4f}")

    model = ARIMA(s, order=(1, 0, 1)).fit()
    print("\n=== ARMA(1,1) ===")
    print(model.summary().tables[1])

    lb = acorr_ljungbox(model.resid, lags=[10], return_df=True)
    print("\nLjung-Box (lag=10):")
    print(lb.round(4).to_string(index=False))
    print("residuals are white noise" if lb["lb_pvalue"].iloc[0] > 0.05 else "residuals not white noise")


if __name__ == "__main__":
    main()
