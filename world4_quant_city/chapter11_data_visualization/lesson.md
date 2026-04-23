# 第11章：数据可视化

> 用图表展示量化分析结果。

## 🌱 为什么需要可视化？

可视化帮助我们：
- 发现数据规律
- 验证策略逻辑
- 展示回测结果

## 🔍 常用图表

### 1. 因子分布图

```python
import matplotlib.pyplot as plt
plt.hist(sentiment_factor, bins=50)
plt.title('情绪因子分布')
plt.show()
```

### 2. 收益率曲线

```python
cumulative_return = (1 + returns).cumprod()
cumulative_return.plot()
plt.title('累计收益率')
plt.show()
```

### 3. 因子IC分析

```python
ic_series.plot(kind='bar')
plt.title('因子IC值')
plt.show()
```

## 🎯 在 quant-NPL 项目中的应用

```python
# 可视化情绪与收益的关系
plt.scatter(merged_df['sentiment'], merged_df['return'])
plt.xlabel('情绪分数')
plt.ylabel('收益率')
plt.show()
```

## 📝 本章练习

8个练习帮助你掌握数据可视化。

```bash
python test.py 4.11.1
```
