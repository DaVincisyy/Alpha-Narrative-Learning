# 第10章：因子工程

> 欢迎来到量化分析城！这一章学习如何构建量化因子。

## 🌱 什么是因子？

因子是用来预测股票收益的特征变量：
- 情绪因子：新闻情绪分数
- 动量因子：过去收益率
- 价值因子：市盈率、市净率

## 🔍 因子构建

### 1. 情绪因子

```python
# 计算每只股票的平均情绪
sentiment_factor = news_df.groupby('stock_code')['sentiment'].mean()
```

### 2. 因子标准化

```python
def standardize_factor(factor_series):
    """标准化因子到均值0，标准差1"""
    return (factor_series - factor_series.mean()) / factor_series.std()
```

### 3. 因子合成

```python
# 多因子加权
combined_factor = 0.5 * sentiment_factor + 0.3 * momentum_factor + 0.2 * value_factor
```

## 🎯 在 quant-NPL 项目中的应用

```python
# 构建情绪因子
daily_sentiment = news_df.groupby(['date', 'stock_code'])['sentiment'].mean()
# 标准化
daily_sentiment = daily_sentiment.groupby('date').apply(standardize_factor)
```

## 📝 本章练习

8个练习帮助你掌握因子工程。

```bash
python test.py 4.10.1
```
