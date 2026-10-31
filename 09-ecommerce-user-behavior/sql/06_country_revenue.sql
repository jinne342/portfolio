-- 06 国家/地区收入分布
WITH total AS (
    SELECT SUM(revenue) AS total_revenue FROM sales
)
SELECT
    country,
    ROUND(SUM(revenue), 2) AS revenue,
    COUNT(DISTINCT invoice_no) AS orders,
    COUNT(DISTINCT customer_id) AS customers,
    ROUND(SUM(revenue) * 100.0 / (SELECT total_revenue FROM total), 2) AS revenue_share_pct
FROM sales
GROUP BY country
ORDER BY revenue DESC
LIMIT 15;
