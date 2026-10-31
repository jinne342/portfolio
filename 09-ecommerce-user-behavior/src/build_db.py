"""Clean the raw Online Retail CSV and load it into DuckDB."""
from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "OnlineRetail.csv"
DB = ROOT / "data" / "ecommerce.duckdb"


def load_raw(path: Path) -> pd.DataFrame:
    with open(path, "r", encoding="latin-1", errors="ignore") as fh:
        first = fh.readline()
    sep = ";" if ";" in first else ","
    decimal = "," if sep == ";" else "."

    df = pd.read_csv(
        path,
        sep=sep,
        decimal=decimal,
        encoding="latin-1",
        dtype={"CustomerID": "string"},
        on_bad_lines="skip",
        engine="python",
    )

    df.columns = [c.strip() for c in df.columns]
    df = df.rename(
        columns={
            "InvoiceNo": "invoice_no",
            "StockCode": "stock_code",
            "Description": "description",
            "Quantity": "quantity",
            "InvoiceDate": "invoice_date",
            "UnitPrice": "unit_price",
            "CustomerID": "customer_id",
            "Country": "country",
        }
    )

    df["invoice_no"] = df["invoice_no"].astype(str).str.strip()
    df["stock_code"] = df["stock_code"].astype(str).str.strip()
    df["description"] = df["description"].fillna("UNKNOWN").astype(str).str.strip()
    df["country"] = df["country"].fillna("Unknown").astype(str).str.strip()
    df["customer_id"] = (
        df["customer_id"].astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
    )
    df.loc[df["customer_id"].isin(["", "nan", "None"]), "customer_id"] = None
    df.loc[df["customer_id"].fillna("").str.fullmatch(r"0+"), "customer_id"] = None

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0.0)
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["invoice_date", "invoice_no"])

    df["revenue"] = df["quantity"] * df["unit_price"]
    df["is_cancelled"] = df["invoice_no"].str.upper().str.startswith("C")
    df["is_return"] = df["quantity"] < 0
    return df


def main() -> None:
    if not RAW.exists():
        raise SystemExit(
            f"{RAW} not found.\n"
            "Download the full dataset from https://archive.ics.uci.edu/dataset/352/online+retail "
            "and save it as data/OnlineRetail.csv, or copy data/sample_online_retail.csv."
        )

    df = load_raw(RAW)
    DB.parent.mkdir(exist_ok=True)
    if DB.exists():
        DB.unlink()

    con = duckdb.connect(str(DB))
    con.register("df", df)
    con.execute("CREATE TABLE transactions AS SELECT * FROM df")
    con.execute(
        """
        CREATE VIEW sales AS
        SELECT *
        FROM transactions
        WHERE quantity > 0 AND unit_price > 0 AND NOT is_cancelled
        """
    )
    con.close()

    print(f"rows      : {len(df):,}")
    print(f"date range: {df['invoice_date'].min()} -> {df['invoice_date'].max()}")
    print(f"customers : {df['customer_id'].nunique():,}")
    print(f"countries : {df['country'].nunique()}")
    print(f"revenue   : {df['revenue'].sum():,.2f}")
    print(f"db        : {DB}")


if __name__ == "__main__":
    main()
