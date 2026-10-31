"""Run every SQL file in sql/, print a preview and export results to reports/sql/."""
from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "ecommerce.duckdb"
SQL_DIR = ROOT / "sql"
OUT_DIR = ROOT / "reports" / "sql"


def main() -> None:
    if not DB.exists():
        raise SystemExit("database not found, run: python src/build_db.py")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(DB), read_only=True)

    for path in sorted(SQL_DIR.glob("*.sql")):
        query = path.read_text(encoding="utf-8")
        try:
            df = con.execute(query).df()
        except Exception as exc:  # noqa: BLE001
            print(f"[FAIL] {path.name}: {exc}")
            continue
        out = OUT_DIR / f"{path.stem}.csv"
        df.to_csv(out, index=False, encoding="utf-8-sig")
        print(f"\n=== {path.name}  ({len(df):,} rows) ===")
        print(df.head(8).to_string(index=False))

    con.close()
    print(f"\nresults saved -> {OUT_DIR}")


if __name__ == "__main__":
    main()
