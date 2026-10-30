"""Run market sizing, financial projection and AHP ranking."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import ahp_brand  # noqa: E402
import market_model  # noqa: E402


def main() -> None:
    market = market_model.run()
    brand = ahp_brand.run()

    print("=" * 60)
    print("Market sizing (TAM/SAM/SOM, 万元)")
    print(json.dumps(market["market"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("Three-year projection")
    print(json.dumps(market["projection"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("Break-even")
    print(json.dumps(market["break_even"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("Scenarios")
    print(json.dumps(market["scenarios"], ensure_ascii=False, indent=2))
    print("=" * 60)
    print("AHP brand-upgrade ranking")
    print(json.dumps(brand, ensure_ascii=False, indent=2))

    out = ROOT / "reports"
    out.mkdir(exist_ok=True)
    (out / "results.json").write_text(
        json.dumps({"market": market, "brand": brand}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("\nsaved -> reports/results.json")


if __name__ == "__main__":
    main()
