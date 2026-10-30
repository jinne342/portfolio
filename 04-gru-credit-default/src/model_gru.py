"""Two-layer GRU with Focal Loss for credit-default prediction.

Hyper-parameters follow the original report:
- GRU units 24 -> 12, dropout 0.35, L2 0.001
- Dense 12 + ReLU, Sigmoid output
- Focal Loss gamma=1.5, alpha=0.75
- Adam lr=8e-4, batch=128, max 20 epochs, early stopping on val AUC
- decision threshold tuned on validation G-mean instead of 0.5
"""
from __future__ import annotations

import numpy as np


def focal_loss(gamma: float = 1.5, alpha: float = 0.75):
    """Binary focal loss. Imported lazily so the module works without TF."""
    import tensorflow as tf

    def loss(y_true, y_pred):
        y_true = tf.cast(y_true, tf.float32)
        y_pred = tf.clip_by_value(y_pred, 1e-7, 1 - 1e-7)
        pt = tf.where(tf.equal(y_true, 1), y_pred, 1 - y_pred)
        at = tf.where(tf.equal(y_true, 1), alpha, 1 - alpha)
        return -tf.reduce_mean(at * tf.pow(1 - pt, gamma) * tf.math.log(pt))

    return loss


def build_model(n_steps: int, n_features: int = 1):
    import tensorflow as tf
    from tensorflow.keras import layers, regularizers

    reg = regularizers.l2(1e-3)
    inputs = tf.keras.Input(shape=(n_steps, n_features))
    x = layers.GRU(24, return_sequences=True, kernel_regularizer=reg)(inputs)
    x = layers.Dropout(0.35)(x)
    x = layers.GRU(12, return_sequences=False, kernel_regularizer=reg)(x)
    x = layers.Dropout(0.35)(x)
    x = layers.Dense(12, activation="relu", kernel_regularizer=reg)(x)
    x = layers.Dropout(0.35)(x)
    outputs = layers.Dense(1, activation="sigmoid")(x)

    model = tf.keras.Model(inputs, outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=8e-4),
        loss=focal_loss(),
        metrics=[tf.keras.metrics.AUC(name="auc")],
    )
    return model


def gmean(y_true, y_pred) -> float:
    from sklearn.metrics import confusion_matrix

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    specificity = tn / (tn + fp) if (tn + fp) else 0.0
    return float(np.sqrt(recall * specificity))


def search_threshold(y_true, y_prob, low: float = 0.05, high: float = 0.95, step: float = 0.01):
    best_th, best_score = 0.5, -1.0
    for th in np.arange(low, high + 1e-9, step):
        score = gmean(y_true, (y_prob >= th).astype(int))
        if score > best_score:
            best_th, best_score = float(th), float(score)
    return best_th, best_score


def evaluate(y_true, y_prob, threshold: float) -> dict:
    from sklearn.metrics import (
        accuracy_score,
        f1_score,
        precision_score,
        recall_score,
        roc_auc_score,
    )

    y_pred = (y_prob >= threshold).astype(int)
    tn = int(((y_true == 0) & (y_pred == 0)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "auc": float(roc_auc_score(y_true, y_prob)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "misclassification": float((fp + fn) / max(len(y_true), 1)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "gmean": gmean(y_true, y_pred),
        "threshold": float(threshold),
        "confusion": {"tn": tn, "fp": fp, "fn": fn, "tp": tp},
    }


def train_and_evaluate(X_train, y_train, X_test, y_test, epochs: int = 20):
    """Train FL-GRU, tune the threshold on a validation split, evaluate on test."""
    import tensorflow as tf
    from sklearn.model_selection import train_test_split

    tf.random.set_seed(42)
    np.random.seed(42)

    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=0.1, random_state=42, stratify=y_train
    )

    model = build_model(n_steps=X_tr.shape[1], n_features=X_tr.shape[2])
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_auc", mode="max", patience=5, min_delta=1e-3, restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.6, patience=3, min_lr=1e-6
        ),
    ]
    model.fit(
        X_tr,
        y_tr,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=128,
        verbose=0,
        callbacks=callbacks,
    )

    val_prob = model.predict(X_val, verbose=0).ravel()
    threshold, val_gmean = search_threshold(y_val, val_prob)

    test_prob = model.predict(X_test, verbose=0).ravel()
    metrics = evaluate(y_test, test_prob, threshold)
    metrics["val_gmean"] = val_gmean
    return model, metrics
