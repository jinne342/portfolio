-- 04 复购间隔：同一客户相邻两次购买的天数
WITH invoices AS (
    SELECT
        customer_id,
        invoice_no,
        MIN(invoice_date) AS invoice_date
    FROM sales
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id, invoice_no
),
with_lag AS (
    SELECT
        customer_id,
        invoice_date,
        LAG(invoice_date) OVER (PARTITION BY customer_id ORDER BY invoice_date) AS prev_date
    FROM invoices
),
intervals AS (
    SELECT
        customer_id,
        DATE_DIFF('day', prev_date, invoice_date) AS gap_days
    FROM with_lag
    WHERE prev_date IS NOT NULL
)
SELECT
    'overall' AS scope,
    COUNT(*) AS repurchase_events,
    ROUND(AVG(gap_days), 1) AS avg_gap_days,
    ROUND(MEDIAN(gap_days), 1) AS median_gap_days,
    ROUND(QUANTILE_CONT(gap_days, 0.25), 1) AS p25,
    ROUND(QUANTILE_CONT(gap_days, 0.75), 1) AS p75
FROM intervals
UNION ALL
SELECT
    'repeat_customers' AS scope,
    COUNT(*) AS repurchase_events,
    ROUND(AVG(gap_days), 1),
    ROUND(MEDIAN(gap_days), 1),
    ROUND(QUANTILE_CONT(gap_days, 0.25), 1),
    ROUND(QUANTILE_CONT(gap_days, 0.75), 1)
FROM intervals
WHERE customer_id IN (
    SELECT customer_id FROM invoices GROUP BY customer_id HAVING COUNT(*) >= 2
);
