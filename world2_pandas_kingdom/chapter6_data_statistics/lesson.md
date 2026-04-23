# 第6章：数据统计与可视化

> 学会了筛选数据后，现在我们要从数据中提取有价值的统计信息，并用图表展示出来。

## 🌱 为什么需要数据统计？

### 真实场景

在 quant-NPL 项目中，我们需要回答这些问题：

```python
# 新闻数据
   日期        股票代码  情绪分数  阅读量
0  2024-01-01  000001   0.85   10000
1  2024-01-01  000002  -0.32    5000
2  2024-01-02  000001   0.76   15000
3  2024-01-02  000003  -0.65    8000
4  2024-01-03  000001   0.92   20000
```

问题：
- 平均情绪分数是多少？
- 哪只股票的新闻最多？
- 每天的平均阅读量是多少？
- 情绪分数的分布如何？

**这就是数据统计的作用！**

## 🔍 基础统计函数

### 1. 描述性统计

```python
import pandas as pd

df = pd.DataFrame({
    '股票代码': ['000001', '000002', '000003', '000001', '000002'],
    '价格': [10.5, 20.3, 15.8, 11.2, 19.8],
    '涨跌幅': [0.05, -0.02, 0.03, 0.07, -0.01]
})

# 查看所有统计信息
print(df.describe())
#           价格      涨跌幅
# count   5.000000  5.000000
# mean   15.520000  0.024000
# std     4.486607  0.037148
# min    10.500000 -0.020000
# 25%    11.200000 -0.010000
# 50%    15.800000  0.030000
# 75%    19.800000  0.050000
# max    20.300000  0.070000
```

### 2. 单列统计

```python
# 平均值
df['价格'].mean()  # 15.52

# 中位数
df['价格'].median()  # 15.8

# 最大值
df['价格'].max()  # 20.3

# 最小值
df['价格'].min()  # 10.5

# 标准差
df['价格'].std()  # 4.49

# 求和
df['价格'].sum()  # 77.6

# 计数
df['价格'].count()  # 5
```

## 💻 分组统计（GroupBy）

### 什么是分组统计？

分组统计是 Pandas 最强大的功能之一：
1. **分组（Split）**：按某列的值分组
2. **应用（Apply）**：对每组应用统计函数
3. **合并（Combine）**：合并结果

### 基础示例

```python
# 按股票代码分组，计算平均价格
result = df.groupby('股票代码')['价格'].mean()
print(result)
# 股票代码
# 000001    10.85
# 000002    20.05
# 000003    15.80
```

### 多种统计

```python
# 多个统计指标
result = df.groupby('股票代码')['价格'].agg(['mean', 'max', 'min', 'count'])
print(result)
#          mean    max    min  count
# 股票代码
# 000001  10.85  11.2  10.5      2
# 000002  20.05  20.3  19.8      2
# 000003  15.80  15.8  15.8      1
```

### 多列分组

```python
# 按日期和股票代码分组
result = df.groupby(['日期', '股票代码'])['情绪分数'].mean()
```

## 🎨 数据可视化基础

### 为什么需要可视化？

数字很抽象，图表更直观：
- 趋势一目了然
- 异常值容易发现
- 更容易发现规律

### 1. 折线图（Line Plot）

用于展示趋势：

```python
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制折线图
df.plot(x='日期', y='价格', kind='line')
plt.title('股价走势')
plt.xlabel('日期')
plt.ylabel('价格')
plt.show()
```

### 2. 柱状图（Bar Plot）

用于比较：

```python
# 按股票代码统计新闻数量
counts = df['股票代码'].value_counts()
counts.plot(kind='bar')
plt.title('各股票新闻数量')
plt.xlabel('股票代码')
plt.ylabel('数量')
plt.show()
```

### 3. 直方图（Histogram）

用于展示分布：

```python
# 情绪分数分布
df['情绪分数'].plot(kind='hist', bins=20)
plt.title('情绪分数分布')
plt.xlabel('情绪分数')
plt.ylabel('频数')
plt.show()
```

### 4. 散点图（Scatter Plot）

用于展示相关性：

```python
# 情绪分数 vs 阅读量
df.plot(x='情绪分数', y='阅读量', kind='scatter')
plt.title('情绪分数与阅读量关系')
plt.show()
```

## 🎯 在 quant-NPL 项目中的应用

### 场景1：计算每只股票的平均情绪

```python
# 按股票代码分组，计算平均情绪分数
avg_sentiment = news_df.groupby('stock_code')['sentiment'].mean()
```

### 场景2：统计每天的新闻数量

```python
# 按日期分组，计数
daily_counts = news_df.groupby('date').size()
```

### 场景3：分析情绪与收益率的关系

```python
# 合并新闻和价格数据
merged = pd.merge(news_df, price_df, on=['date', 'stock_code'])

# 按情绪分数分组，计算平均收益率
sentiment_return = merged.groupby(
    pd.cut(merged['sentiment'], bins=[-1, -0.5, 0, 0.5, 1])
)['return'].mean()
```

### 场景4：可视化情绪趋势

```python
# 按日期统计平均情绪
daily_sentiment = news_df.groupby('date')['sentiment'].mean()

# 绘制趋势图
daily_sentiment.plot(kind='line')
plt.title('每日平均情绪趋势')
plt.show()
```

## ⚠️ 常见陷阱

### 陷阱1：忘记重置索引

```python
# groupby 后索引变成了分组列
result = df.groupby('股票代码')['价格'].mean()
print(result.index)  # Index(['000001', '000002', '000003'])

# 重置索引
result = result.reset_index()
print(result.columns)  # ['股票代码', '价格']
```

### 陷阱2：空值影响统计

```python
# 包含空值的列
df['价格'].mean()  # 自动忽略空值

# 显式处理
df['价格'].dropna().mean()
```

### 陷阱3：中文显示问题

```python
# 绘图前设置中文字体
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

## 📝 本章练习

本章包含 8 个练习，帮助你掌握数据统计：

1. **练习1**：计算平均值
2. **练习2**：计算最大值和最小值
3. **练习3**：分组统计
4. **练习4**：多指标统计
5. **练习5**：计数统计
6. **练习6**：多列分组
7. **练习7**：数据透视表
8. **练习8**：综合练习 - 新闻情绪分析

## 🚀 开始练习

```bash
# 测试单个练习
python test.py 2.6.1

# 测试整个章节
python test.py 2.6
```

掌握数据统计，你就能从数据中挖掘出有价值的洞察！
