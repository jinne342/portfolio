-- 03 周 Cohort 留存：按首购周分组，观察后续每周留存
WITH first_purchase AS (
    SELECT customer_id, MIN(DATE_TRUNC('week', invoice_date)) AS cohort_week
    FROM sales
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
),
activity AS (
    SELECT DISTINCT
        customer_id,
        DATE_TRUNC('week', invoice_date) AS activity_week
    FROM sales
    WHERE customer_id IS NOT NULL
),
cohort_data AS (
    SELECT
        f.cohort_week,
        a.activity_week,
        DATE_DIFF('week', f.cohort_week, a.activity_week) AS week_index,
        f.customer_id
    FROM first_purchase f
    JOIN activity a USING (customer_id)
),
cohort_size AS (
    SELECT cohort_week, COUNT(DISTINCT customer_id) AS cohort_customers
    FROM first_purchase
    GROUP BY cohort_week
)
SELECT
    c.cohort_week,
    c.week_index,
    s.cohort_customers,
    COUNT(DISTINCT c.customer_id) AS retained_customers,
    ROUND(COUNT(DISTINCT c.customer_id) * 100.0 / s.cohort_customers, 1) AS retention_pct
FROM cohort_data c
JOIN cohort_size s USING (cohort_week)
WHERE c.week_index BETWEEN 0 AND 6
GROUP BY c.cohort_week, c.week_index, s.cohort_customers
ORDER BY c.cohort_week, c.week_index;
