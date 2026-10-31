# 电信客户流失预测 · 机器学习课程项目

> 从数据生成、预处理、模型比较到业务建议的完整机器学习流程；附课程 LaTeX 模板原件。

## 项目内容

- **任务**：二分类预测电信客户是否流失
- **数据**：2000 条合成样本（34.95% 流失率），9 个字段
- **模型**：逻辑回归、随机森林、梯度提升树
- **评估**：Accuracy、Precision、Recall、F1、AUC、5 折 CV AUC

## 主要结果

| 模型 | Accuracy | Precision | Recall | F1 | AUC |
|---|---:|---:|---:|---:|---:|
| **逻辑回归** | **0.7275** | 0.5838 | **0.7714** | **0.6646** | **0.7646** |
| 随机森林 | 0.6950 | 0.5625 | 0.5786 | 0.5704 | 0.7327 |
| 梯度提升树 | 0.7175 | **0.6517** | 0.4143 | 0.5066 | 0.7412 |

结论：逻辑回归召回最高，适合召回优先的挽留场景；树模型精确率更高但漏判多。

## 目录

```
08-ml-course-project/
├─ README.md
├─ report.md              完整实验报告（背景/数据/方法/结果/建议/局限）
├─ data/
│  └─ sample_churn.csv    合成样本（2000 行）
├─ src/
│  ├─ generate_data.py    生成合成数据
│  └─ train.py            预处理 + 三模型训练 + 评估
├─ latex-template/        课程提供的 LaTeX 模板原件（main.tex / SJTUReport.sty / 图）
└─ requirements.txt
```

## 运行

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/train.py
```

## 说明

- 原始课程数据未随模板提供，仓库使用**合成数据**跑通流程，指标不代表真实业务。
- `latex-template/` 是课程提供的原始模板，未做改动；完整报告见 `report.md`。
- 数据字段、预处理、模型参数和结果均在 `report.md` 中详细说明。
