# 统计预测与时间序列分析 · 课程实验合集

> 应用统计学专业四份实验报告的整理与代码化：回归预测、平滑/趋势/季节预测、平稳性与 ARMA、SARIMA 季节预测。

## 实验一览

| # | 实验 | 核心内容 | 文档 |
|---|---|---|---|
| 1 | 统计预测 · 实验一 | 一元/多元/非线性回归；人寿保险购买额 vs 年均收入、风险反感度；5 个模型对比 MAPE | [PDF](./docs/stat-forecast-exp1.pdf) · [Markdown](./docs/stat-forecast-exp1.md) |
| 2 | 统计预测 · 实验二 | 简单平均、移动平均、一次/二次指数平滑、趋势外推、季节变动；MAPE 评价 | [PDF](./docs/stat-forecast-exp2.pdf) · [Markdown](./docs/stat-forecast-exp2.md) |
| 3 | 时间序列分析 · 实验 1 | 平稳性检验、纯随机性检验、ACF/PACF 定阶、AR/MA/ARMA 建模与检验 | [PDF](./docs/time-series-lab1.pdf) · [Markdown](./docs/time-series-lab1.md) |
| 4 | 时间序列分析 · 实验 2 | 时间序列分解（趋势/季节/随机）、ARIMA 季节模型、5 期预测 | [PDF](./docs/time-series-lab2.pdf) · [Markdown](./docs/time-series-lab2.md) |

## 代码

| 文件 | 对应实验 | 说明 |
|---|---|---|
| `src/data.py` | — | 生成四组同结构示例数据（原始数据未随报告提供） |
| `src/regression_forecast.py` | 实验 1 | 5 个回归模型：含交互项二次多项式、无交互二次、教材多项式、对数、幂函数；输出 R²、MAPE、预测值 |
| `src/smoothing_forecast.py` | 实验 2 | 移动平均、一次指数平滑、Holt 线性趋势、Holt-Winters 季节模型；样本外 MAPE |
| `src/stationarity_arma.py` | 实验 3 | ADF 平稳性检验、ACF/PACF、ARMA(1,1) 拟合、Ljung-Box 白噪声检验 |
| `src/sarima_forecast.py` | 实验 4 | 季节分解、SARIMA(1,1,1)(1,1,1,12)、5 期预测与误差评价 |

```bash
pip install -r requirements.txt
python src/regression_forecast.py
python src/smoothing_forecast.py
python src/stationarity_arma.py
python src/sarima_forecast.py
```

## 方法要点

- **回归预测**：OLS 估计 → t 检验/F 检验 → 残差诊断 → 点预测与区间预测；用 MAPE 横向比较模型
- **平滑预测**：移动平均消除随机波动；指数平滑对近期数据加权；Holt 处理趋势；Holt-Winters 处理趋势 + 季节
- **平稳性**：时序图 + ADF 单位根检验；ACF 拖尾/PACF 截尾定 AR 阶，反之定 MA 阶
- **SARIMA**：先分解看趋势与季节，再用差分平稳化，最后用 AIC/BIC 与残差检验选参

## 说明与局限

1. **原始数据未公开**：四份报告中的原始数据未随文件提供，`src/data.py` 生成同结构示例数据，用于跑通方法；示例结果不代表报告原始结论。
2. **报告已脱敏**：封面姓名替换为 `XXX`、学号替换为 `XXXXXXXXXX`、指导教师替换为 `XXX`，文档作者元数据已清空。
3. 实验报告中的 SPSS 截图保留在 PDF 中，Markdown 为文字版。
4. 代码用于方法复现与教学，不构成预测结论。
