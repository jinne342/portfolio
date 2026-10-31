-- 07 退货与取消订单分析
WITH base AS (
    SELECT
        COUNT(*) AS all_rows,
        SUM(CASE WHEN is_cancelled THEN 1 ELSE 0 END) AS cancelled_rows,
        SUM(CASE WHEN is_return THEN 1 ELSE 0 END) AS return_rows,
        SUM(CASE WHEN is_cancelled THEN revenue ELSE 0 END) AS cancelled_revenue,
        SUM(CASE WHEN is_return THEN revenue ELSE 0 END) AS return_revenue
    FROM transactions
)
SELECT
    all_rows,
    cancelled_rows,
    ROUND(cancelled_rows * 100.0 / all_rows, 2) AS cancelled_pct,
    return_rows,
    ROUND(return_rows * 100.0 / all_rows, 2) AS return_pct,
    ROUND(cancelled_revenue, 2) AS cancelled_revenue,
    ROUND(return_revenue, 2) AS return_revenue
FROM base;
