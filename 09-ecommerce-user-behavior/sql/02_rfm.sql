-- 02 RFM 客户分层
WITH snapshot AS (
    SELECT MAX(invoice_date) AS max_date FROM sales
),
customer_rfm AS (
    SELECT
        customer_id,
        DATE_DIFF('day', MAX(invoice_date), (SELECT max_date FROM snapshot)) AS recency_days,
        COUNT(DISTINCT invoice_no) AS frequency,
        SUM(revenue) AS monetary
    FROM sales
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
),
scored AS (
    SELECT
        *,
        6 - NTILE(5) OVER (ORDER BY recency_days) AS r_score,
        NTILE(5) OVER (ORDER BY frequency) AS f_score,
        NTILE(5) OVER (ORDER BY monetary) AS m_score
    FROM customer_rfm
)
SELECT
    customer_id,
    recency_days,
    frequency,
    ROUND(monetary, 2) AS monetary,
    r_score,
    f_score,
    m_score,
    CASE
        WHEN r_score >= 4 AND f_score >= 4 AND m_score >= 4 THEN '重要价值客户'
        WHEN r_score >= 4 AND m_score >= 4 THEN '重要发展客户'
        WHEN r_score <= 2 AND f_score >= 4 AND m_score >= 4 THEN '重要挽留客户'
        WHEN r_score <= 2 AND f_score <= 2 THEN '流失客户'
        WHEN r_score >= 4 AND f_score <= 2 THEN '新客户'
        ELSE '一般客户'
    END AS segment
FROM scored
ORDER BY monetary DESC;
