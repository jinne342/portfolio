"""End-to-end runner: clean -> describe -> baseline -> FL-GRU.

Usage:
    python src/run_all.py                 # full pipeline (needs TensorFlow)
    python src/run_all.py --skip-model    # data checks + baseline only
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402

import baseline  # noqa: E402
import preprocess  # noqa: E402


def describe(df: pd.DataFrame) -> pd.DataFrame:
    """Descriptive statistics used in the report (max/min/median/var/skew/kurt)."""
    rows = []
    for col in preprocess.RAW_FEATURES:
        s = df[col].dropna()
        rows.append(
            {
                "feature": col,
                "max": s.max(),
                "min": s.min(),
                "median": s.median(),
                "var": s.var(),
                "skew": s.skew(),
                "kurt": s.kurt(),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=str(ROOT / "data" / "sample_credit.csv"))
    parser.add_argument("--skip-model", action="store_true")
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        print(f"{data_path} not found, generating synthetic sample ...")
        from generate_sample import main as gen

        gen(out_path=str(data_path))

    df_raw = pd.read_csv(data_path)
    df_clean = preprocess.engineer(preprocess.clean(df_raw))

    print("=" * 60)
    print(f"raw rows        : {len(df_raw)}")
    print(f"cleaned rows    : {len(df_clean)}")
    print(f"default rate    : {df_clean[preprocess.TARGET].mean():.4%}")
    print("=" * 60)

    stats = describe(df_clean)
    pd.set_option("display.width", 160)
    print(stats.round(4).to_string(index=False))

    X_train, X_test, y_train, y_test, features, meta = preprocess.prepare(str(data_path))
    print(f"\ntrain: {X_train.shape}  test: {X_test.shape}")
    print(f"features: {features}")

    results = {"meta": meta}
    results["logistic"] = baseline.train_and_evaluate(X_train, y_train, X_test, y_test)
    print("\n[logistic] ", json.dumps(results["logistic"], ensure_ascii=False, indent=2))

    if not args.skip_model:
        try:
            import model_gru

            _, metrics = model_gru.train_and_evaluate(X_train, y_train, X_test, y_test)
            results["fl_gru"] = metrics
            print("\n[FL-GRU] ", json.dumps(metrics, ensure_ascii=False, indent=2))
        except ImportError as exc:
            print(f"\n[skip] TensorFlow not available: {exc}")
            print("       install it with: pip install tensorflow")

    out_dir = ROOT / "reports"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "metrics.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nsaved -> {out_dir / 'metrics.json'}")


if __name__ == "__main__":
    main()
