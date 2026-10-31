-- 05 Top 品类：按收入排序
SELECT
    description,
    ROUND(SUM(revenue), 2) AS revenue,
    SUM(quantity) AS units,
    COUNT(DISTINCT invoice_no) AS orders,
    COUNT(DISTINCT customer_id) AS customers
FROM sales
WHERE description <> 'UNKNOWN'
GROUP BY description
ORDER BY revenue DESC
LIMIT 20;
