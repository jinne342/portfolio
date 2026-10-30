"""AHP evaluation of brand-upgrade priorities for the Huayu Beijing plan."""
from __future__ import annotations

import numpy as np

CRITERIA = ["文化IP", "产品创新", "渠道", "数字化"]

# Saaty pairwise matrix (row vs column)
MATRIX = np.array(
    [
        [1, 2, 3, 4],
        [1 / 2, 1, 2, 3],
        [1 / 3, 1 / 2, 1, 2],
        [1 / 4, 1 / 3, 1 / 2, 1],
    ]
)

# option scores per criterion (1-5)
OPTIONS = {
    "A. 纹样IP + 联名": [5, 3, 3, 2],
    "B. 产品分层 + 体验课": [3, 5, 4, 2],
    "C. 数字内容 + 直播": [3, 3, 4, 5],
}


def weights() -> dict:
    eigvals, eigvecs = np.linalg.eig(MATRIX)
    idx = np.argmax(eigvals.real)
    w = np.abs(eigvecs[:, idx].real)
    w = w / w.sum()
    n = len(CRITERIA)
    ci = (eigvals[idx].real - n) / (n - 1)
    ri = {3: 0.58, 4: 0.90, 5: 1.12}.get(n, 0.90)
    return {
        "weights": dict(zip(CRITERIA, w.round(4).tolist())),
        "lambda_max": round(float(eigvals[idx].real), 4),
        "consistency_ratio": round(float(ci / ri), 4),
        "consistent": bool(ci / ri < 0.1),
    }


def rank_options() -> dict:
    w = np.array(list(weights()["weights"].values()))
    scores = {}
    for name, s in OPTIONS.items():
        scores[name] = round(float(np.dot(np.array(s), w)), 4)
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return {"scores": scores, "ranking": [k for k, _ in ranked]}


def run() -> dict:
    return {"criteria": CRITERIA, **weights(), "options": rank_options()}
