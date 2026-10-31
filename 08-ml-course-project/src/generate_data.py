"""Generate a synthetic telecom churn dataset for the course project."""
from pathlib import Path

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)


def main(n: int = 2000) -> None:
    tenure = RNG.integers(1, 72, n)
    monthly = RNG.normal(70, 25, n).clip(20, 150)
    total = (tenure * monthly * RNG.uniform(0.9, 1.1, n)).round(2)
    contract = RNG.choice(["month-to-month", "one-year", "two-year"], n, p=[0.55, 0.25, 0.20])
    internet = RNG.choice(["fiber", "dsl", "none"], n, p=[0.45, 0.35, 0.20])
    payment = RNG.choice(["electronic", "mailed", "bank"], n, p=[0.55, 0.25, 0.20])
    support_calls = RNG.poisson(1.2, n)
    online_security = RNG.choice(["yes", "no"], n, p=[0.35, 0.65])

    logit = (
        -1.2
        - 0.045 * tenure
        + 0.012 * monthly
        + 0.35 * support_calls
        + 1.1 * (contract == "month-to-month")
        + 0.5 * (internet == "fiber")
        + 0.3 * (payment == "electronic")
        - 0.6 * (online_security == "yes")
        + RNG.normal(0, 0.6, n)
    )
    prob = 1 / (1 + np.exp(-logit))
    churn = (RNG.random(n) < prob).astype(int)

    df = pd.DataFrame(
        {
            "tenure_months": tenure,
            "monthly_charges": monthly.round(2),
            "total_charges": total,
            "contract": contract,
            "internet_service": internet,
            "payment_method": payment,
            "support_calls": support_calls,
            "online_security": online_security,
            "churn": churn,
        }
    )
    out = Path(__file__).resolve().parents[1] / "data" / "sample_churn.csv"
    out.parent.mkdir(exist_ok=True)
    df.to_csv(out, index=False)
    print(f"saved {len(df)} rows -> {out}")
    print(f"churn rate: {df['churn'].mean():.4f}")


if __name__ == "__main__":
    main()
