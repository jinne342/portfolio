"""Logistic-regression baseline for comparison with FL-GRU."""
from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


def train_and_evaluate(X_train, y_train, X_test, y_test):
    X_tr = X_train.reshape(X_train.shape[0], -1)
    X_te = X_test.reshape(X_test.shape[0], -1)

    clf = LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42)
    clf.fit(X_tr, y_train)

    prob = clf.predict_proba(X_te)[:, 1]
    pred = (prob >= 0.5).astype(int)

    return {
        "accuracy": float(accuracy_score(y_test, pred)),
        "precision": float(precision_score(y_test, pred, zero_division=0)),
        "auc": float(roc_auc_score(y_test, prob)),
        "recall": float(recall_score(y_test, pred, zero_division=0)),
        "f1": float(f1_score(y_test, pred, zero_division=0)),
        "threshold": 0.5,
    }
