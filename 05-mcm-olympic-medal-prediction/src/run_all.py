"""Run the full Olympic medal analysis and print a summary."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from analysis import run_all  # noqa: E402


def main() -> None:
    results = run_all()
    print("=" * 60)
    print("GBDT medal prediction")
    print(json.dumps(results["gbdt"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("First-time medal winners")
    print(json.dumps(results["first_medal"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("Herfindahl index (sport concentration)")
    print(json.dumps(results["herfindahl"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("AHP (great-coach effect)")
    print(json.dumps(results["ahp"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("Mann-Whitney U test")
    print(json.dumps(results["mann_whitney"], ensure_ascii=False, indent=2))
    print("\nsaved -> reports/results.json")


if __name__ == "__main__":
    main()
