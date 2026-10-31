"""Lab 1: five regression models for life-insurance purchase prediction."""
from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from data import insurance

MODELS = {
    "M1 二次多项式(含交互)": "purchase ~ income + risk + I(income**2) + I(risk**2) + income:risk",
    "M2 二次多项式(无交互)": "purchase ~ income + risk + I(income**2) + I(risk**2)",
    "M3 教材多项式": "purchase ~ income + I(risk**2)",
    "M4 对数模型": "purchase ~ np.log(income) + np.log(risk)",
    "M5 幂函数模型": "np.log(purchase) ~ np.log(income) + np.log(risk)",
}


def mape(y_true, y_pred) -> float:
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    mask = y_true != 0
    return float(np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100)


def main() -> None:
    df = insurance()
    print(df.head().to_string(index=False))
    rows = []
    for name, formula in MODELS.items():
        fit = smf.ols(formula, data=df).fit()
        fitted = fit.fittedvalues
        if name.startswith("M5"):
            fitted = np.exp(fitted)
        rows.append(
            {
                "model": name,
                "R2": round(fit.rsquared, 4),
                "adj_R2": round(fit.rsquared_adj, 4),
                "F_pvalue": round(float(fit.f_pvalue), 6),
                "MAPE_%": round(mape(df["purchase"], fitted), 2),
            }
        )
    result = pd.DataFrame(rows).sort_values("MAPE_%")
    print("\n=== model comparison ===")
    print(result.to_string(index=False))

    best = smf.ols(MODELS["M3 教材多项式"], data=df).fit()
    new = pd.DataFrame({"income": [50.0], "risk": [5.0]})
    pred = best.get_prediction(new).summary_frame(alpha=0.05)
    print("\n=== forecast (income=50, risk=5) ===")
    print(pred[["mean", "mean_ci_lower", "mean_ci_upper"]].round(2).to_string(index=False))


if __name__ == "__main__":
    main()
