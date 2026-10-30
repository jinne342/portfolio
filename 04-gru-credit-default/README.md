# 基于 FL-GRU 的信用卡违约预警模型

> 专业导论课程报告的项目化整理：从数据清洗、特征工程、类别不平衡处理，到双层 GRU + Focal Loss 建模与阈值寻优。

## 项目背景

信用卡业务的信用风险具有**信息不对称强、个人偿债能力波动大**的特点。传统评分卡多把违约当作静态分类问题，而违约风险实际上是历史还款行为、负债水平、收入变化等因素逐步累积的结果。本项目把 11 维客户特征构造为**伪时序序列**，用 GRU 提取特征间的非线性依赖，并用 Focal Loss 缓解违约样本极少（5.83%）带来的类别不平衡。

## 数据

| 项目 | 说明 |
|---|---|
| 原始数据 | `cs-training.csv`（Kaggle *Give Me Some Credit* 同 schema 数据） |
| 原始样本 | 980 位客户 × 11 个指标 |
| 清洗后 | **801 条**有效样本 |
| 违约占比 | **5.83%** |
| 过采样后 | **1054 条**（违约/正常各 527） |
| 划分 | 训练集 : 测试集 = 8 : 2 |

> 原始数据未随报告提供。仓库内 `data/sample_credit.csv` 是**同 schema 的合成样本**，仅用于跑通流程；其中的指标分布与结论不代表真实业务。

### 字段说明

| 字段 | 含义 | 类型 |
|---|---|---|
| `SeriousDlqin2yrs` | 2 年内是否严重逾期（目标变量） | 0/1 |
| `RevolvingUtilizationOfUnsecuredLines` | 无担保信贷循环利用率 | 连续 |
| `age` | 年龄 | 连续 |
| `NumberOfTime30-59DaysPastDueNotWorse` | 2 年内逾期 30–59 天次数 | 计数 |
| `DebtRatio` | 债务比率 | 连续 |
| `MonthlyIncome` | 月收入 | 连续 |
| `NumberOfOpenCreditLinesAndLoans` | 信用账户总数 | 计数 |
| `NumberOfTimes90DaysLate` | 2 年内逾期 90 天以上次数 | 计数 |
| `NumberRealEstateLoansOrLines` | 房地产相关贷款/额度数 | 计数 |
| `NumberOfTime60-89DaysPastDueNotWorse` | 2 年内逾期 60–89 天次数 | 计数 |
| `NumberOfDependents` | 受抚养人数 | 计数 |

## 方法

### 1. 数据清洗（按报告口径）
- 逾期 30–59 天次数 > 24 视为脏数据，剔除
- 逾期 90 天以上次数 > 8 视为脏数据，剔除
- `DebtRatio > 1` 且 `MonthlyIncome` 缺失：负债率计算失真，剔除
- `NumberOfDependents` 缺失：按年龄分层（20–30、30–40、40–50、50–60、60–100）用组内均值填补
- 箱线图识别出的极端值**保留**（符合真实业务中的长尾）

### 2. 特征工程
- 三段逾期次数加权求和，得到「逾期严重度」核心信号
- 逾期次数分箱，转为类别特征
- 最终保留 **9 个核心特征**

### 3. 类别不平衡
- `BorderlineSMOTE`：只对决策边界附近的少数类样本插值扩增，避免把合成样本放进多数类区域
- 过采样比例 50%，得到 1054 条平衡样本

### 4. FL-GRU 模型
| 组件 | 设置 |
|---|---|
| 结构 | 双层 GRU（24 → 12）+ Dense(12, ReLU) + Sigmoid |
| 正则 | Dropout 0.35，L2 0.001 |
| 损失 | Focal Loss，γ = 1.5，α = 0.75 |
| 优化器 | Adam，学习率 0.0008 |
| 训练 | 20 epochs，batch 128，早停（验证 AUC，patience 5） |
| 阈值 | 在验证集上以 **G-mean** 最大为目标搜索，而非固定 0.5 |

## 报告结果（原始数据）

| 模型 | 准确率 | 精确率 | AUC | 召回率 | 误判率 | F1 | G-mean |
|---|---:|---:|---:|---:|---:|---:|---:|
| **FL-GRU** | **0.8930** | **0.3384** | **0.7965** | **0.6429** | **0.3571** | **0.6725** | **0.6500** |

- 最优分类阈值 **0.6500**
- 预警分层：绿色 < 0.5987（安全）、黄色 0.5987–0.6381（关注）、红色 ≥ 0.6381（高危）
- 结论：在保持较高准确率的同时，召回率达到 64.29%，更适合“宁可误判、不可漏判”的风控场景

> 以上指标来自报告原文，基于未公开的原始数据。运行本仓库的合成样本会得到不同数值。

## 目录结构

```
04-gru-credit-default/
├─ README.md
├─ report.pdf              报告技术正文（已脱敏，17 页）
├─ report.md               报告正文 Markdown（便于检索/引用）
├─ data/
│  ├─ README.md            数据来源与字段说明
│  └─ sample_credit.csv    合成样本（980 行，跑通用）
├─ src/
│  ├─ generate_sample.py   生成同 schema 合成数据
│  ├─ preprocess.py        清洗、缺失填补、特征工程、SMOTE
│  ├─ model_gru.py         FL-GRU 模型、训练、阈值寻优
│  ├─ baseline.py          逻辑回归基线
│  └─ run_all.py           一键运行
└─ requirements.txt
```

## 运行

```bash
pip install -r requirements.txt

# 1) 生成合成样本（如已有真实 cs-training.csv，可跳过）
python src/generate_sample.py

# 2) 一键跑通：清洗 → 描述统计 → 基线 → FL-GRU
python src/run_all.py

# 只想看数据处理（不装 TensorFlow 也能跑）
python src/run_all.py --skip-model
```

## 说明与局限

1. **数据是横截面的**：报告把 11 个特征视为序列的 11 个时间步，属于“伪时序”。这能让 GRU 跑起来，但并不等同于真实的还款序列；更严谨的做法是使用按月还款记录构造真实时间序列。
2. **样本量小**：980 条（清洗后 801 条），深度模型容易过拟合，报告用 Dropout、L2、早停和 Focal Loss 缓解。
3. **原始数据未公开**：仓库只提供合成样本；复现报告指标需要原始 `cs-training.csv`。
4. 报告中的个人感想、培养方案建议等非技术章节未收录。

## 参考

- Cho et al. (2014). Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation.
- Lin et al. (2017). Focal Loss for Dense Object Detection.
- Han et al. (2005). Borderline-SMOTE: A New Over-Sampling Method in Imbalanced Data Sets Learning.
