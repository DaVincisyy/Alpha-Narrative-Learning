# 第12章：统计检验

> 验证因子的有效性。

## 🌱 为什么需要统计检验？

统计检验帮助我们判断：
- 因子是否真的有效？
- 结果是否只是运气？
- 策略是否稳健？

## 🔍 常用检验方法

### 1. t检验

```python
from scipy import stats

# 检验因子收益是否显著大于0
t_stat, p_value = stats.ttest_1samp(factor_returns, 0)
if p_value < 0.05:
    print("因子显著有效")
```

### 2. 相关性检验

```python
# 计算因子与收益的相关系数
correlation = sentiment_factor.corr(returns)
```

### 3. IC值计算

```python
# Information Coefficient
ic = merged_df.groupby('date').apply(
    lambda x: x['sentiment'].corr(x['return'])
).mean()
```

## 🎯 在 quant-NPL 项目中的应用

```python
# 检验情绪因子的预测能力
ic_series = merged_df.groupby('date').apply(
    lambda x: x['sentiment'].corr(x['next_return'])
)
print(f"平均IC: {ic_series.mean():.4f}")
print(f"IC胜率: {(ic_series > 0).mean():.2%}")
```

## 📝 本章练习

8个练习帮助你掌握统计检验。

```bash
python test.py 4.12.1
```
