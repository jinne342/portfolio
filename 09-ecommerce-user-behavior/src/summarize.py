"""Compute the headline numbers used in README / one-pager."""
from __future__ import annotations

from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "ecommerce.duckdb"
con = duckdb.connect(str(DB), read_only=True)

overall = con.execute(
    """
    SELECT ROUND(SUM(revenue),0) revenue,
           COUNT(DISTINCT invoice_no) orders,
           COUNT(DISTINCT customer_id) customers,
           ROUND(SUM(revenue)/COUNT(DISTINCT invoice_no),2) aov
    FROM sales
    """
).fetchone()
print(f"revenue={overall[0]:,.0f} orders={overall[1]:,} customers={overall[2]:,} aov={overall[3]}")

repeat = con.execute(
    """
    WITH c AS (
        SELECT customer_id, COUNT(DISTINCT invoice_no) n
        FROM sales WHERE customer_id IS NOT NULL GROUP BY customer_id
    )
    SELECT ROUND(AVG(CASE WHEN n>=2 THEN 1 ELSE 0 END)*100,1),
           ROUND(AVG(n),2), COUNT(*)
    FROM c
    """
).fetchone()
print(f"repeat_rate={repeat[0]}% avg_orders_per_customer={repeat[1]} customers={repeat[2]}")

share = con.execute(
    """
    WITH c AS (
        SELECT customer_id, SUM(revenue) m FROM sales
        WHERE customer_id IS NOT NULL GROUP BY customer_id
    ),
    r AS (SELECT m, NTILE(5) OVER (ORDER BY m DESC) b FROM c)
    SELECT ROUND(SUM(CASE WHEN b=1 THEN m END)*100.0/SUM(m),1) FROM r
    """
).fetchone()
print(f"top20pct_revenue_share={share[0]}%")

segments = con.execute(
    """
    WITH snapshot AS (SELECT MAX(invoice_date) d FROM sales),
    c AS (
        SELECT customer_id,
               DATE_DIFF('day', MAX(invoice_date), (SELECT d FROM snapshot)) recency,
               COUNT(DISTINCT invoice_no) frequency, SUM(revenue) monetary
        FROM sales WHERE customer_id IS NOT NULL GROUP BY customer_id
    ),
    s AS (
        SELECT *, 6-NTILE(5) OVER (ORDER BY recency) r,
               NTILE(5) OVER (ORDER BY frequency) f,
               NTILE(5) OVER (ORDER BY monetary) m
        FROM c
    )
    SELECT CASE
             WHEN r>=4 AND f>=4 AND m>=4 THEN '重要价值客户'
             WHEN r>=4 AND m>=4 THEN '重要发展客户'
             WHEN r<=2 AND f>=4 AND m>=4 THEN '重要挽留客户'
             WHEN r<=2 AND f<=2 THEN '流失客户'
             WHEN r>=4 AND f<=2 THEN '新客户'
             ELSE '一般客户' END segment,
           COUNT(*) customers, ROUND(SUM(monetary),0) revenue
    FROM s GROUP BY 1 ORDER BY revenue DESC
    """
).fetchall()
for row in segments:
    print(f"segment={row[0]} customers={row[1]} revenue={row[2]:,.0f}")

cohort = con.execute(
    """
    WITH f AS (
        SELECT customer_id, MIN(DATE_TRUNC('week', invoice_date)) cw
        FROM sales WHERE customer_id IS NOT NULL GROUP BY customer_id
    ),
    a AS (SELECT DISTINCT customer_id, DATE_TRUNC('week', invoice_date) aw FROM sales),
    d AS (SELECT f.cw, DATE_DIFF('week', f.cw, a.aw) idx, f.customer_id FROM f JOIN a USING(customer_id)),
    s AS (SELECT cw, COUNT(*) n FROM f GROUP BY cw)
    SELECT idx, ROUND(AVG(retained*100.0/n),1) FROM (
        SELECT d.cw, d.idx, s.n, COUNT(DISTINCT d.customer_id) retained
        FROM d JOIN s USING(cw) WHERE idx BETWEEN 1 AND 4 GROUP BY 1,2,3
    ) GROUP BY idx ORDER BY idx
    """
).fetchall()
print("cohort_avg_retention:", {int(i): p for i, p in cohort})

country = con.execute(
    """
    SELECT country, ROUND(SUM(revenue)*100.0/(SELECT SUM(revenue) FROM sales),2)
    FROM sales GROUP BY 1 ORDER BY 2 DESC LIMIT 3
    """
).fetchall()
print("top_countries:", country)

con.close()
