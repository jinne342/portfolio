-- 01 周度收入趋势与环比（数据覆盖 8 周）
WITH weekly AS (
    SELECT
        DATE_TRUNC('week', invoice_date) AS week,
        SUM(revenue) AS revenue,
        COUNT(DISTINCT invoice_no) AS orders,
        COUNT(DISTINCT customer_id) AS customers
    FROM sales
    GROUP BY 1
)
SELECT
    week,
    ROUND(revenue, 2) AS revenue,
    orders,
    customers,
    ROUND(revenue / NULLIF(orders, 0), 2) AS avg_order_value,
    ROUND(revenue - LAG(revenue) OVER (ORDER BY week), 2) AS wow_delta,
    ROUND((revenue / LAG(revenue) OVER (ORDER BY week) - 1) * 100, 1) AS wow_pct
FROM weekly
ORDER BY week;
