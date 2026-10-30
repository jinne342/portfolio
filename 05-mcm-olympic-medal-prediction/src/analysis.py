"""Analysis toolkit for the MCM Olympic medal paper.

Implements the four analytical pieces described in the paper:
1. GBDT medal-table prediction (R^2 / RMSE, feature importance)
2. First-time medal winners and forecast confidence
3. Herfindahl index of sport concentration
4. AHP weights for the "great coach" effect + Mann-Whitney U test
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FEATURES = ["athletes", "host", "prev_medals", "gdp_index"]


def train_gbdt(panel: pd.DataFrame) -> dict:
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.metrics import mean_squared_error, r2_score

    years = sorted(panel["year"].unique())
    test_year = years[-1]
    train = panel[panel["year"] < test_year]
    test = panel[panel["year"] == test_year]

    model = GradientBoostingRegressor(
        n_estimators=300, learning_rate=0.05, max_depth=3, random_state=42
    )
    model.fit(train[FEATURES], train["medals"])
    pred = model.predict(test[FEATURES])

    result = {
        "test_year": int(test_year),
        "r2": float(r2_score(test["medals"], pred)),
        "rmse": float(np.sqrt(mean_squared_error(test["medals"], pred))),
        "feature_importance": dict(zip(FEATURES, model.feature_importances_.round(4).tolist())),
    }
    test = test.copy()
    test["predicted"] = pred
    result["top10"] = (
        test.sort_values("predicted", ascending=False)
        .head(10)[["country", "predicted", "medals"]]
        .round(2)
        .to_dict("records")
    )
    return result


def first_medal(panel: pd.DataFrame) -> dict:
    """Count countries winning their first medal in each edition."""
    df = panel.sort_values(["country", "year"]).copy()
    df["cum_before"] = df.groupby("country")["medals"].cumsum() - df["medals"]
    firsts = df[(df["cum_before"] <= 0) & (df["medals"] > 0)]
    counts = firsts.groupby("year").size().reindex(sorted(df["year"].unique()), fill_value=0)

    # linear trend on historical counts (exclude the last, unobserved edition)
    hist = counts.iloc[:-1]
    if len(hist) >= 2:
        x = np.arange(len(hist))
        slope, intercept = np.polyfit(x, hist.values, 1)
        forecast = max(0.0, intercept + slope * len(hist))
    else:
        forecast = float(hist.mean()) if len(hist) else 0.0

    # convert RMSE of the trend into a rough probability (paper uses normalised MSE)
    resid = hist.values - (intercept + slope * np.arange(len(hist))) if len(hist) >= 2 else np.array([0.0])
    rmse = float(np.sqrt(np.mean(resid**2))) if len(resid) else 0.0
    prob = float(1 - 0.5 * (1 + math.erf(rmse / (math.sqrt(2) * max(forecast, 1e-6)))))

    return {
        "counts_by_year": {int(k): int(v) for k, v in counts.items()},
        "forecast_next": round(forecast, 2),
        "confidence": round(max(0.0, min(1.0, prob)), 4),
        "trend_rmse": round(rmse, 4),
    }


def herfindahl(sport_df: pd.DataFrame) -> dict:
    """HHI = sum of squared sport shares of a country's medals (0-1)."""
    last_year = sport_df["year"].max()
    df = sport_df[sport_df["year"] == last_year]
    totals = df.groupby("country")["medals"].sum().replace(0, np.nan)
    shares = df.groupby(["country", "sport"])["medals"].sum().div(totals, level="country").fillna(0)
    hhi = shares.groupby("country").apply(lambda s: float((s**2).sum())).sort_values(ascending=False)
    return {
        "year": int(last_year),
        "hhi_top10": hhi.head(10).round(4).to_dict(),
        "interpretation": "越接近 1 表示奖牌越集中在少数项目",
    }


def ahp() -> dict:
    """AHP for great-coach effect: 4 criteria, consistency ratio check."""
    criteria = ["执教经验", "项目匹配度", "训练科学性", "团队管理"]
    # pairwise matrix (row vs column), Saaty 1-9 scale
    m = np.array(
        [
            [1, 2, 3, 4],
            [1 / 2, 1, 2, 3],
            [1 / 3, 1 / 2, 1, 2],
            [1 / 4, 1 / 3, 1 / 2, 1],
        ]
    )
    eigvals, eigvecs = np.linalg.eig(m)
    idx = np.argmax(eigvals.real)
    weights = np.abs(eigvecs[:, idx].real)
    weights = weights / weights.sum()
    n = len(criteria)
    ci = (eigvals[idx].real - n) / (n - 1)
    ri = {3: 0.58, 4: 0.90, 5: 1.12}.get(n, 0.90)
    return {
        "criteria": criteria,
        "weights": dict(zip(criteria, weights.round(4).tolist())),
        "lambda_max": round(float(eigvals[idx].real), 4),
        "consistency_ratio": round(float(ci / ri), 4),
        "consistent": bool(ci / ri < 0.1),
    }


def mann_whitney(sport_df: pd.DataFrame, country: str = "C03", sport: str = "diving") -> dict:
    """Compare medal counts before/after a hypothetical coach appointment (2016)."""
    from scipy.stats import mannwhitneyu

    s = sport_df[(sport_df["country"] == country) & (sport_df["sport"] == sport)]
    before = s[s["year"] < 2016]["medals"].values
    after = s[s["year"] >= 2016]["medals"].values
    if len(before) < 2 or len(after) < 2:
        return {"error": "not enough observations"}
    stat, p = mannwhitneyu(before, after, alternative="two-sided")
    return {
        "country": country,
        "sport": sport,
        "before_mean": round(float(before.mean()), 3),
        "after_mean": round(float(after.mean()), 3),
        "u_stat": float(stat),
        "p_value": round(float(p), 4),
        "significant_at_0.05": bool(p < 0.05),
    }


def run_all() -> dict:
    panel = pd.read_csv(ROOT / "data" / "olympic_panel.csv")
    sport_df = pd.read_csv(ROOT / "data" / "sport_medals.csv")
    results = {
        "gbdt": train_gbdt(panel),
        "first_medal": first_medal(panel),
        "herfindahl": herfindahl(sport_df),
        "ahp": ahp(),
        "mann_whitney": mann_whitney(sport_df),
    }
    out = ROOT / "reports"
    out.mkdir(exist_ok=True)
    (out / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return results
