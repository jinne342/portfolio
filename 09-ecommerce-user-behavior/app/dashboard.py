"""Streamlit dashboard for the Online Retail analysis."""
from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "ecommerce.duckdb"

st.set_page_config(page_title="电商用户行为分析", page_icon="🛒", layout="wide")


@st.cache_data
def query(sql: str) -> pd.DataFrame:
    con = duckdb.connect(str(DB), read_only=True)
    try:
        return con.execute(sql).df()
    finally:
        con.close()


def main() -> None:
    if not DB.exists():
        st.error("数据库不存在，请先运行 `python src/build_db.py`")
        st.stop()

    st.title("🛒 电商用户行为分析")
    st.caption("UCI Online Retail · 2010-12 至 2011-12 · SQL + DuckDB + Streamlit")

    kpi = query(
        """
        SELECT
            ROUND(SUM(revenue), 0) AS revenue,
            COUNT(DISTINCT invoice_no) AS orders,
            COUNT(DISTINCT customer_id) AS customers,
            ROUND(SUM(revenue) / NULLIF(COUNT(DISTINCT invoice_no), 0), 2) AS aov
        FROM sales
        """
    ).iloc[0]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("总收入", f"£{kpi.revenue:,.0f}")
    c2.metric("订单数", f"{kpi.orders:,.0f}")
    c3.metric("客户数", f"{kpi.customers:,.0f}")
    c4.metric("客单价", f"£{kpi.aov:,.2f}")

    tab1, tab2, tab3, tab4 = st.tabs(["📈 收入趋势", "👥 RFM 分层", "🔁 Cohort 留存", "🏷️ 品类与国家"])

    with tab1:
        weekly = query(
            """
            SELECT DATE_TRUNC('week', invoice_date) AS week,
                   SUM(revenue) AS revenue,
                   COUNT(DISTINCT invoice_no) AS orders
            FROM sales GROUP BY 1 ORDER BY 1
            """
        )
        fig = px.line(weekly, x="week", y="revenue", markers=True, title="周度收入")
        fig.update_layout(yaxis_title="收入 (£)", xaxis_title="")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(weekly.tail(12), use_container_width=True)

    with tab2:
        rfm = query(
            """
            WITH snapshot AS (SELECT MAX(invoice_date) AS max_date FROM sales),
            c AS (
                SELECT customer_id,
                       DATE_DIFF('day', MAX(invoice_date), (SELECT max_date FROM snapshot)) AS recency,
                       COUNT(DISTINCT invoice_no) AS frequency,
                       SUM(revenue) AS monetary
                FROM sales WHERE customer_id IS NOT NULL GROUP BY customer_id
            )
            SELECT *,
                   6 - NTILE(5) OVER (ORDER BY recency) AS r,
                   NTILE(5) OVER (ORDER BY frequency) AS f,
                   NTILE(5) OVER (ORDER BY monetary) AS m,
                   CASE
                     WHEN recency <= 30 AND frequency >= 5 THEN '重要价值'
                     WHEN recency <= 30 THEN '新近客户'
                     WHEN frequency >= 5 THEN '高频老客'
                     WHEN recency > 180 THEN '流失风险'
                     ELSE '一般客户'
                   END AS segment
            FROM c
            """
        )
        col1, col2 = st.columns(2)
        with col1:
            seg = rfm.groupby("segment", as_index=False).agg(
                customers=("customer_id", "count"), revenue=("monetary", "sum")
            )
            fig = px.bar(seg, x="segment", y="customers", color="segment", title="各分层客户数")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.scatter(
                rfm, x="recency", y="monetary", color="segment", size="frequency",
                hover_data=["customer_id"], title="Recency vs Monetary",
                log_y=True,
            )
            st.plotly_chart(fig, use_container_width=True)
        st.dataframe(seg.sort_values("revenue", ascending=False), use_container_width=True)

    with tab3:
        cohort = query(
            """
            WITH first_purchase AS (
                SELECT customer_id, MIN(DATE_TRUNC('week', invoice_date)) AS cohort_week
                FROM sales WHERE customer_id IS NOT NULL GROUP BY customer_id
            ),
            activity AS (
                SELECT DISTINCT customer_id, DATE_TRUNC('week', invoice_date) AS activity_week
                FROM sales WHERE customer_id IS NOT NULL
            ),
            data AS (
                SELECT f.cohort_week, f.customer_id,
                       DATE_DIFF('week', f.cohort_week, a.activity_week) AS idx
                FROM first_purchase f JOIN activity a USING (customer_id)
            ),
            size AS (
                SELECT cohort_week, COUNT(*) AS n FROM first_purchase GROUP BY cohort_week
            )
            SELECT d.cohort_week, d.idx, s.n AS cohort_size,
                   COUNT(DISTINCT d.customer_id) AS retained,
                   ROUND(COUNT(DISTINCT d.customer_id) * 100.0 / s.n, 1) AS pct
            FROM data d JOIN size s USING (cohort_week)
            WHERE d.idx BETWEEN 0 AND 6
            GROUP BY 1, 2, 3 ORDER BY 1, 2
            """
        )
        pivot = cohort.pivot(index="cohort_week", columns="idx", values="pct")
        fig = px.imshow(
            pivot, text_auto=".0f", aspect="auto",
            color_continuous_scale="Blues", title="周 Cohort 留存率（%）",
            labels={"x": "首购后第 N 周", "y": "首购周", "color": "%"},
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            products = query(
                """
                SELECT description, ROUND(SUM(revenue), 0) AS revenue
                FROM sales WHERE description <> 'UNKNOWN'
                GROUP BY 1 ORDER BY revenue DESC LIMIT 12
                """
            )
            fig = px.bar(products, x="revenue", y="description", orientation="h",
                         title="Top 12 品类（收入）")
            fig.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            countries = query(
                """
                SELECT country, ROUND(SUM(revenue), 0) AS revenue
                FROM sales GROUP BY 1 ORDER BY revenue DESC LIMIT 12
                """
            )
            fig = px.bar(countries, x="revenue", y="country", orientation="h",
                         title="Top 12 国家/地区（收入）")
            fig.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig, use_container_width=True)

    st.caption("数据源：UCI Online Retail · 代码：github.com/jinne342/portfolio")


if __name__ == "__main__":
    main()
