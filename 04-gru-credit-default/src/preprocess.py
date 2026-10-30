"""Cleaning, imputation and feature engineering for the credit-default task.

The rules follow the original report:
- drop impossible overdue counts (>24 for 30-59 days, >8 for 90+ days)
- drop rows where DebtRatio > 1 and MonthlyIncome is missing (ratio is unreliable)
- impute NumberOfDependents with age-stratified group means
- keep statistical outliers (they are plausible in real credit data)
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

TARGET = "SeriousDlqin2yrs"
AGE_BINS = [20, 30, 40, 50, 60, 100]
AGE_LABELS = ["20-30", "30-40", "40-50", "50-60", "60-100"]

RAW_FEATURES = [
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

# 9 core features used by the model
MODEL_FEATURES = [
    "RevolvingUtilizationOfUnsecuredLines",
    "age",
    "DebtRatio",
    "MonthlyIncome",
    "NumberOfOpenCreditLinesAndLoans",
    "NumberRealEstateLoansOrLines",
    "NumberOfDependents",
    "OverdueScore",
    "OverdueBin",
]


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the report's dirty-data rules and stratified imputation."""
    df = df.copy()

    df = df[df["NumberOfTime30-59DaysPastDueNotWorse"] <= 24]
    df = df[df["NumberOfTimes90DaysLate"] <= 8]
    mask_bad_ratio = (df["DebtRatio"] > 1) & (df["MonthlyIncome"].isna())
    df = df[~mask_bad_ratio]

    # age-stratified mean imputation for dependents
    age_group = pd.cut(df["age"], bins=AGE_BINS, labels=AGE_LABELS, right=False)
    group_mean = df.groupby(age_group, observed=False)["NumberOfDependents"].transform("mean")
    df["NumberOfDependents"] = df["NumberOfDependents"].fillna(group_mean)
    df["NumberOfDependents"] = df["NumberOfDependents"].fillna(df["NumberOfDependents"].median())

    # remaining missing income -> median
    df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].median())

    return df.reset_index(drop=True)


def engineer(df: pd.DataFrame) -> pd.DataFrame:
    """Build the weighted overdue score and its binned version."""
    df = df.copy()
    df["OverdueScore"] = (
        1 * df["NumberOfTime30-59DaysPastDueNotWorse"]
        + 2 * df["NumberOfTime60-89DaysPastDueNotWorse"]
        + 3 * df["NumberOfTimes90DaysLate"]
    )
    df["OverdueBin"] = pd.cut(
        df["OverdueScore"], bins=[-1, 0, 2, 5, 100], labels=[0, 1, 2, 3]
    ).astype(int)
    return df


def prepare(
    csv_path: str,
    test_size: float = 0.2,
    balance: bool = True,
    random_state: int = 42,
):
    """Load, clean, engineer and split the data.

    Returns X_train, X_test, y_train, y_test, feature_names, meta.
    X is shaped (n_samples, n_features, 1) for the GRU.
    """
    df = pd.read_csv(csv_path)
    n_raw = len(df)
    default_rate_raw = df[TARGET].mean()

    df = clean(df)
    df = engineer(df)
    n_clean = len(df)

    X = df[MODEL_FEATURES].astype(float).values
    y = df[TARGET].astype(int).values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    if balance:
        try:
            from imblearn.over_sampling import BorderlineSMOTE

            smote = BorderlineSMOTE(random_state=random_state, sampling_strategy=1.0)
            X_train, y_train = smote.fit_resample(X_train, y_train)
        except ImportError:
            print("[warn] imbalanced-learn not installed, skip BorderlineSMOTE")

    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    meta = {
        "n_raw": n_raw,
        "n_clean": n_clean,
        "default_rate_raw": float(default_rate_raw),
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "features": MODEL_FEATURES,
    }
    return X_train, X_test, y_train, y_test, MODEL_FEATURES, meta
