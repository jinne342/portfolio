"""Generate a synthetic country-level Olympic panel and sport-level medal table.

The original dataset is not redistributed with the paper. This sample keeps the
same structure so the analysis pipeline can be executed end-to-end.
"""
from pathlib import Path

import numpy as np
import pandas as pd

RNG = np.random.default_rng(7)
COUNTRIES = [f"C{i:02d}" for i in range(1, 31)]
YEARS = [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028]
SPORTS = ["swimming", "athletics", "gymnastics", "diving", "tennis", "shooting"]


def main() -> None:
    rows = []
    base_strength = {c: RNG.gamma(2.0, 1.0) for c in COUNTRIES}

    for year in YEARS:
        host = "C01" if year == 2028 else ("C05" if year == 2024 else None)
        for c in COUNTRIES:
            athletes = int(max(5, RNG.normal(120, 40)))
            prev = base_strength[c] * 8 + RNG.normal(0, 2)
            host_bonus = 4.0 if c == host else 0.0
            medals = max(0.0, prev + 0.02 * athletes + host_bonus + RNG.normal(0, 2))
            rows.append(
                {
                    "country": c,
                    "year": year,
                    "athletes": athletes,
                    "host": int(c == host),
                    "prev_medals": round(max(0.0, prev), 2),
                    "gdp_index": round(float(RNG.lognormal(10, 0.4)), 2),
                    "medals": round(medals, 2),
                }
            )

    panel = pd.DataFrame(rows)
    root = Path(__file__).resolve().parents[1]
    (root / "data").mkdir(exist_ok=True)
    panel.to_csv(root / "data" / "olympic_panel.csv", index=False)

    sport_rows = []
    for year in YEARS:
        for c in COUNTRIES:
            for s in SPORTS:
                strength = base_strength[c] * (0.5 + RNG.random())
                sport_rows.append(
                    {
                        "country": c,
                        "year": year,
                        "sport": s,
                        "medals": int(max(0, RNG.poisson(strength / len(SPORTS)))),
                    }
                )
    sport_df = pd.DataFrame(sport_rows)
    sport_df.to_csv(root / "data" / "sport_medals.csv", index=False)
    print(f"panel: {panel.shape} -> data/olympic_panel.csv")
    print(f"sport: {sport_df.shape} -> data/sport_medals.csv")


if __name__ == "__main__":
    main()
