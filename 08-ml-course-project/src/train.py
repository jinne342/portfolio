"""Telecom churn prediction: preprocessing, model comparison and evaluation.

Models: logistic regression, random forest, gradient boosting.
Metrics: accuracy, precision, recall, F1, ROC-AUC, 5-fold CV AUC.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
TARGET = "churn"
NUM = ["tenure_months", "monthly_charges", "total_charges", "support_calls"]
CAT = ["contract", "internet_service", "payment_method", "online_security"]


def build_preprocessor() -> ColumnTransformer:
    numeric = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    categorical = Pipeline(
        [("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]
    )
    return ColumnTransformer([("num", numeric, NUM), ("cat", categorical, CAT)])


def metrics(y_true, y_pred, y_prob) -> dict:
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return {
        "accuracy": round(float(accuracy_score(y_true, y_pred)), 4),
        "precision": round(float(precision_score(y_true, y_pred, zero_division=0)), 4),
        "recall": round(float(recall_score(y_true, y_pred, zero_division=0)), 4),
        "f1": round(float(f1_score(y_true, y_pred, zero_division=0)), 4),
        "auc": round(float(roc_auc_score(y_true, y_prob)), 4),
        "confusion": {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp)},
    }


def main() -> None:
    data_path = ROOT / "data" / "sample_churn.csv"
    if not data_path.exists():
        from generate_data import main as gen

        gen()

    df = pd.read_csv(data_path)
    X, y = df.drop(columns=[TARGET]), df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "LogisticRegression": LogisticRegression(max_iter=2000, class_weight="balanced"),
        "RandomForest": RandomForestClassifier(
            n_estimators=300, min_samples_leaf=3, class_weight="balanced", random_state=42, n_jobs=-1
        ),
        "GradientBoosting": GradientBoostingClassifier(random_state=42),
    }

    results = {}
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    for name, clf in models.items():
        pipe = Pipeline([("prep", build_preprocessor()), ("clf", clf)])
        pipe.fit(X_train, y_train)
        prob = pipe.predict_proba(X_test)[:, 1]
        pred = (prob >= 0.5).astype(int)
        res = metrics(y_test, pred, prob)
        res["cv_auc"] = round(float(cross_val_score(pipe, X, y, cv=cv, scoring="roc_auc").mean()), 4)
        results[name] = res
        print(f"\n[{name}]")
        print(json.dumps(res, ensure_ascii=False, indent=2))

    # feature importance from random forest
    rf = Pipeline([("prep", build_preprocessor()), ("clf", RandomForestClassifier(
        n_estimators=300, min_samples_leaf=3, class_weight="balanced", random_state=42, n_jobs=-1))])
    rf.fit(X_train, y_train)
    names = rf.named_steps["prep"].get_feature_names_out()
    imp = rf.named_steps["clf"].feature_importances_
    top = sorted(zip(names, imp), key=lambda x: x[1], reverse=True)[:10]
    print("\n=== top 10 feature importance ===")
    for n, v in top:
        print(f"  {n:45s} {v:.4f}")

    out = ROOT / "reports"
    out.mkdir(exist_ok=True)
    (out / "metrics.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nsaved -> {out / 'metrics.json'}")


if __name__ == "__main__":
    main()
