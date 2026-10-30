"""Generate a synthetic dataset with the same schema as cs-training.csv.

The original credit dataset is not redistributed with the report. This script
creates a small, clearly-labelled synthetic sample so the pipeline can be run
end-to-end. It intentionally injects missing values and a few dirty rows so the
cleaning rules in preprocess.py are exercised.
"""
from pathlib import Path

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

COLUMNS = [
    "SeriousDlqin2yrs",
    "RevolvingUtilizationOfUnsecuredLines",
    "age",
    "NumberOfTime30-59DaysPastDueNotWorse",
    "DebtRatio",
    "MonthlyIncome",
    "NumberOfOpenCreditLinesAndLoans",
    "NumberOfTimes90DaysLate",
    "NumberRealEstateLoansOrLines",
    "NumberOfTime60-89DaysPastDueNotWorse",
    "NumberOfDependents",
]


def main(n_rows: int = 980, out_path: str | None = None) -> None:
    n_default = int(n_rows * 0.058)

    age = RNG.normal(51, 12, n_rows).clip(22, 92).round().astype(int)
    income = RNG.lognormal(mean=8.4, sigma=0.55, size=n_rows).clip(0, 30000)
    # a few unemployed customers with zero income
    income[RNG.choice(n_rows, size=12, replace=False)] = 0

    revolving = RNG.beta(0.7, 3.0, n_rows) * 1.2
    debt_ratio = np.where(
        income > 0,
        RNG.gamma(1.2, 0.35, n_rows),
        RNG.uniform(0, 2.0, n_rows),
    )
    open_lines = RNG.poisson(8, n_rows).clip(0, 30)
    real_estate = RNG.poisson(1, n_rows).clip(0, 6)
    dependents = RNG.poisson(0.8, n_rows).clip(0, 6)

    late30 = RNG.poisson(0.25, n_rows).clip(0, 12)
    late60 = RNG.poisson(0.08, n_rows).clip(0, 8)
    late90 = RNG.poisson(0.04, n_rows).clip(0, 6)

    target = np.zeros(n_rows, dtype=int)
    risk = (
        0.9 * (revolving > 0.8)
        + 0.7 * (late30 >= 2)
        + 1.0 * (late90 >= 1)
        + 0.3 * (debt_ratio > 0.8)
    )
    risk_score = risk + RNG.normal(0, 0.5, n_rows)
    target[np.argsort(risk_score)[-n_default:]] = 1

    df = pd.DataFrame(
        {
            "SeriousDlqin2yrs": target,
            "RevolvingUtilizationOfUnsecuredLines": revolving.round(6),
            "age": age,
            "NumberOfTime30-59DaysPastDueNotWorse": late30,
            "DebtRatio": debt_ratio.round(6),
            "MonthlyIncome": income.round(0),
            "NumberOfOpenCreditLinesAndLoans": open_lines,
            "NumberOfTimes90DaysLate": late90,
            "NumberRealEstateLoansOrLines": real_estate,
            "NumberOfTime60-89DaysPastDueNotWorse": late60,
            "NumberOfDependents": dependents,
        }
    )

    # inject missing values (MCAR) to exercise imputation
    df.loc[RNG.choice(n_rows, 40, replace=False), "MonthlyIncome"] = np.nan
    df.loc[RNG.choice(n_rows, 25, replace=False), "NumberOfDependents"] = np.nan

    # inject a few dirty rows that the cleaning rules should drop
    dirty_idx = RNG.choice(n_rows, 8, replace=False)
    df.loc[dirty_idx[:3], "NumberOfTime30-59DaysPastDueNotWorse"] = 30
    df.loc[dirty_idx[3:6], "NumberOfTimes90DaysLate"] = 12
    df.loc[dirty_idx[6:], "DebtRatio"] = 2.5
    df.loc[dirty_idx[6:], "MonthlyIncome"] = np.nan

    out = Path(out_path) if out_path else Path(__file__).resolve().parents[1] / "data" / "sample_credit.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"saved {len(df)} rows -> {out}")
    print(f"default rate: {df['SeriousDlqin2yrs'].mean():.4f}")


if __name__ == "__main__":
    main()
