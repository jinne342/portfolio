# 电商用户行为分析 · SQL + Python + Streamlit

> 基于 UCI Online Retail 交易数据的端到端分析：清洗 → SQL 取数 → RFM 分层 → 周 cohort 留存 → 复购分析 → 交互式看板。

## 业务问题

一家英国在线零售商（数据覆盖 2010-12 至 2011-01）面临三个问题：

1. **收入从哪来**：哪些客户、品类、国家贡献了主要销售额？
2. **客户在流失吗**：复购率、复购间隔、cohort 留存表现如何？
3. **该优先挽留谁**：如何用 RFM 把客户分层，把有限预算花在高价值客户上？

## 数据

| 项目 | 说明 |
|---|---|
| 来源 | [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) 的公开镜像子集 |
| 原始行数 | 120,158 行 |
| 清洗后 | **66,764 行**有效交易 |
| 时间范围 | **2010-12-01 至 2011-01-21（约 8 周）** |
| 客户 / 订单 | **1,150 位客户 / 2,261 笔订单** |
| 销售额 | **£1,350,127**，客单价 **£597.14** |
| 字段 | InvoiceNo、StockCode、Description、Quantity、InvoiceDate、UnitPrice、CustomerID、Country |
| 数据问题 | 退货（负数量）、取消订单（InvoiceNo 以 C 开头）、缺失 CustomerID（`000000`）、0 价格 |

> 本仓库使用的是 UCI 原版（541,909 行、2010-12 至 2011-12）的**前 8 周公开子集**。如需完整一年数据，请从 UCI 下载后覆盖 `data/OnlineRetail.csv`，代码无需修改。原始 CSV 约 7.5 MB，未提交（见 `.gitignore`）；仓库内 `data/sample_online_retail.csv` 为前 5,000 行样例。

## 分析框架

```
原始交易 → 清洗（取消/退货/缺失/异常价） → DuckDB 明细表 + sales 视图
   ├─ SQL 01 周度收入与环比
   ├─ SQL 02 RFM 分层（NTILE）
   ├─ SQL 03 周 cohort 留存
   ├─ SQL 04 复购间隔（LAG）
   ├─ SQL 05 Top 品类
   ├─ SQL 06 国家分布
   ├─ SQL 07 退货/取消分析
   └─ SQL 08 高价值客户清单
        ↓
Streamlit 看板（周趋势 / RFM / 留存热力图 / 品类与国家）
```

## 目录

```
09-ecommerce-user-behavior/
├─ README.md
├─ data/
│  └─ sample_online_retail.csv   前 5000 行样例
├─ sql/
│  ├─ 01_weekly_revenue.sql
│  ├─ 02_rfm.sql
│  ├─ 03_cohort_retention.sql
│  ├─ 04_repurchase_interval.sql
│  ├─ 05_top_products.sql
│  ├─ 06_country_revenue.sql
│  ├─ 07_returns.sql
│  └─ 08_high_value_customers.sql
├─ src/
│  ├─ build_db.py                清洗并写入 DuckDB
│  ├─ run_queries.py             批量执行 SQL、导出结果
│  └─ summarize.py               汇总关键指标
├─ app/
│  └─ dashboard.py               Streamlit 看板
├─ docs/
│  └─ one-pager.md               一页纸结论
└─ requirements.txt
```

## 运行

```bash
pip install -r requirements.txt

# 1) 把完整数据放到 data/OnlineRetail.csv
#    没有完整数据时，可复制 data/sample_online_retail.csv 先跑通（结果仅作演示）

# 2) 建库
python src/build_db.py

# 3) 执行 8 条 SQL，结果导出到 reports/sql/
python src/run_queries.py

# 4) 汇总核心指标
python src/summarize.py

# 5) 启动看板
streamlit run app/dashboard.py
```

## 核心 SQL 技巧

- **RFM**：`NTILE(5)` 分别给 R/F/M 打分，`CASE` 组合成 6 类客户
- **Cohort 留存**：首购周 + `DATE_DIFF('week', ...)` 计算第 N 周留存
- **复购间隔**：`LAG(invoice_date) OVER (PARTITION BY customer_id ORDER BY invoice_date)`
- **窗口函数**：周环比、客户消费排名、分位数
- **数据质量**：`000000` 的 CustomerID 视为缺失；取消/退货订单不进入 `sales` 视图

## 主要结论

1. **收入高度集中**：Top 20% 客户贡献 **69.6%** 的销售额；RFM 中 195 位「重要价值客户」（17%）贡献 **£457,607（33.9%）**，是预算优先项。
2. **复购是最大杠杆**：整体复购率仅 **36.0%**，人均 **1.77** 单；64% 的客户只买过一次。首购后第 1 周平均留存 **10.1%**，第 2 周 9.0%，第 3 周降至 6.8%——**首购后 7 天是召回黄金窗口**。
3. **地区高度集中**：英国本土占 **87.3%**，荷兰 2.6%、爱尔兰 2.2%；欧洲大陆是第二增长曲线，但客单价与频次仍需验证。
4. **退货与取消可控**：取消订单 1,118 笔（**1.67%**），退货 1,228 笔（1.84%），合计影响销售额约 **£198,520**，集中在少数大额订单。

## 业务建议

- 对「重要挽留客户」（56 人，£88,566）做 7 天内一对一召回，优先于泛投
- 新客首单后 7 天内发第二单优惠券，目标把第 1 周留存从 10% 提到 15%
- 英国以外市场先做荷兰/爱尔兰小规模测试，验证跨境物流与客单价
- 取消/退货订单单独监控，超过 2% 时排查商品描述与库存准确性

## 说明与局限

- 数据只有 8 周，**无法做年度季节性分析**；cohort 只能观察到首购后 6 周
- 数据无事件流（曝光/点击），因此不做点击漏斗，只做交易侧分析
- CustomerID 缺失的订单保留在销售总额中，但不参与客户级分析
- 极少数异常大额订单（如单笔 £77k）会拉高客单价，报告中已单独识别
- 看板为本地 Streamlit，运行 `streamlit run app/dashboard.py` 即可查看；如需在线版可部署到 Streamlit Community Cloud

