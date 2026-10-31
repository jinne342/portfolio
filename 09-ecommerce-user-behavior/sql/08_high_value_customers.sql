-- 08 高价值客户清单（RFM 555 或 消费 Top 10%）
WITH customer_rfm AS (
    SELECT
        customer_id,
        MAX(invoice_date) AS last_purchase,
        COUNT(DISTINCT invoice_no) AS frequency,
        SUM(revenue) AS monetary
    FROM sales
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
),
ranked AS (
    SELECT
        *,
        NTILE(10) OVER (ORDER BY monetary DESC) AS monetary_decile,
        6 - NTILE(5) OVER (ORDER BY last_purchase DESC) AS r_score,
        NTILE(5) OVER (ORDER BY frequency) AS f_score,
        NTILE(5) OVER (ORDER BY monetary) AS m_score
    FROM customer_rfm
)
SELECT
    customer_id,
    last_purchase,
    frequency,
    ROUND(monetary, 2) AS monetary,
    r_score, f_score, m_score,
    ROUND(monetary / NULLIF(frequency, 0), 2) AS avg_order_value
FROM ranked
WHERE monetary_decile = 1
ORDER BY monetary DESC;
