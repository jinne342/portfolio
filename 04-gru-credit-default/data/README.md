# 数据说明

## 原始数据

报告使用的原始文件为 `cs-training.csv`，字段与 Kaggle **Give Me Some Credit** 竞赛数据一致：

- 980 位客户、11 个字段（含目标变量 `SeriousDlqin2yrs`）
- 违约样本占比约 5.83%
- 原始数据**未随报告公开**，因此不在本仓库中

如需复现报告中的指标，请自行获取同 schema 数据，放到本目录并命名为 `cs-training.csv`，然后运行：

```bash
python src/run_all.py --data data/cs-training.csv
```

## 合成样本

`sample_credit.csv` 由 `src/generate_sample.py` 生成，用于：

- 在没有原始数据时跑通「清洗 → 特征工程 → SMOTE → 建模」全流程
- 演示缺失值填补与脏数据剔除规则

**注意**：合成样本的分布、违约率与模型指标均为模拟结果，**不代表报告中的真实结论**。报告指标请以 `README.md` 中引用的数值为准。

## 字段

| 字段 | 含义 |
|---|---|
| `SeriousDlqin2yrs` | 2 年内是否严重逾期（1 = 是） |
| `RevolvingUtilizationOfUnsecuredLines` | 无担保信贷循环利用率 |
| `age` | 年龄 |
| `NumberOfTime30-59DaysPastDueNotWorse` | 2 年内逾期 30–59 天次数 |
| `DebtRatio` | 债务比率 |
| `MonthlyIncome` | 月收入 |
| `NumberOfOpenCreditLinesAndLoans` | 信用账户总数 |
| `NumberOfTimes90DaysLate` | 2 年内逾期 90 天以上次数 |
| `NumberRealEstateLoansOrLines` | 房地产相关贷款/额度数 |
| `NumberOfTime60-89DaysPastDueNotWorse` | 2 年内逾期 60–89 天次数 |
| `NumberOfDependents` | 受抚养人数 |

## 隐私

原始数据包含个人金融信息，本仓库不存储、不分发任何真实客户记录。
