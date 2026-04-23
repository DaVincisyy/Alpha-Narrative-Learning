# 第4章：DataFrame 入门

> 欢迎来到 Pandas 数据王国！这一章我们将学习 Pandas 的核心数据结构 DataFrame。

## 🌱 什么是 DataFrame？

### 最简单的理解

想象一下 Excel 表格：
- 有行和列
- 每列有列名
- 每行有数据

**DataFrame 就是 Python 中的 Excel 表格！**

```python
# 一个简单的 DataFrame
   姓名  年龄  城市
0  张三  25  北京
1  李四  30  上海
2  王五  28  深圳
```

### 为什么需要 DataFrame？

在 quant-NPL 项目中，我们处理的是这样的数据：

```python
# 股票新闻数据
   日期        股票代码  标题                情绪分数
0  2024-01-01  000001  公司业绩大涨          0.85
1  2024-01-02  000002  市场波动加剧         -0.32
2  2024-01-03  000001  新产品发布成功        0.76
```

用列表和字典处理这种数据会很麻烦，但 DataFrame 让一切变得简单！

## 🔍 DataFrame 的组成部分

### 1. 数据（Data）

DataFrame 的核心是数据，通常来自：
- 字典（最常用）
- 列表
- CSV 文件
- 数据库

### 2. 索引（Index）

每一行都有一个索引（默认是 0, 1, 2...）：

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['张三', '李四'],
    '年龄': [25, 30]
})

print(df)
#    姓名  年龄
# 0  张三  25    <- 0 是索引
# 1  李四  30    <- 1 是索引
```

### 3. 列名（Columns）

每一列都有名字：

```python
print(df.columns)
# Index(['姓名', '年龄'], dtype='object')
```

## 💻 创建 DataFrame

### 方法1：从字典创建（最常用）

```python
import pandas as pd

# 字典的键 = 列名
# 字典的值 = 列数据（列表）
data = {
    '股票代码': ['000001', '000002', '000003'],
    '价格': [10.5, 20.3, 15.8],
    '涨跌幅': [0.05, -0.02, 0.03]
}

df = pd.DataFrame(data)
print(df)
```

输出：
```
   股票代码    价格  涨跌幅
0  000001  10.5  0.05
1  000002  20.3 -0.02
2  000003  15.8  0.03
```

### 方法2：从列表创建

```python
# 列表的列表
data = [
    ['张三', 25, '北京'],
    ['李四', 30, '上海']
]

df = pd.DataFrame(data, columns=['姓名', '年龄', '城市'])
print(df)
```

### 方法3：从 CSV 文件读取（实战常用）

```python
# 读取 CSV 文件
df = pd.read_csv('data.csv')

# 查看前几行
print(df.head())
```

## 🎯 DataFrame 基本操作

### 1. 查看数据

```python
# 查看前 5 行
df.head()

# 查看前 3 行
df.head(3)

# 查看后 5 行
df.tail()

# 查看数据形状（行数，列数）
df.shape  # 返回 (3, 3) 表示 3 行 3 列

# 查看数据信息
df.info()

# 查看统计信息
df.describe()
```

### 2. 选择列

```python
# 选择单列（返回 Series）
prices = df['价格']
print(type(prices))  # <class 'pandas.core.series.Series'>

# 选择多列（返回 DataFrame）
subset = df[['股票代码', '价格']]
print(type(subset))  # <class 'pandas.core.frame.DataFrame'>
```

### 3. 选择行

```python
# 通过索引选择（iloc = integer location）
first_row = df.iloc[0]  # 第一行
first_three = df.iloc[0:3]  # 前三行

# 通过标签选择（loc = location）
row = df.loc[0]  # 索引为 0 的行
```

### 4. 选择特定单元格

```python
# 方法1：先列后行
value = df['价格'][0]  # 第一行的价格

# 方法2：使用 iloc
value = df.iloc[0, 1]  # 第 0 行，第 1 列

# 方法3：使用 loc
value = df.loc[0, '价格']  # 索引 0，列名 '价格'
```

## ⚠️ 常见陷阱

### 陷阱1：Series vs DataFrame

```python
# 单列 = Series（一维）
s = df['价格']
print(type(s))  # Series

# 多列 = DataFrame（二维）
d = df[['价格']]  # 注意双层方括号
print(type(d))  # DataFrame
```

### 陷阱2：索引从 0 开始

```python
# 第一行是 iloc[0]，不是 iloc[1]
first = df.iloc[0]

# 切片不包含结束位置
first_two = df.iloc[0:2]  # 只包含索引 0 和 1
```

### 陷阱3：修改数据要小心

```python
# ❌ 错误：链式索引
df['价格'][0] = 100  # 可能不会生效

# ✅ 正确：使用 loc
df.loc[0, '价格'] = 100
```

## 🎯 在 quant-NPL 项目中的应用

在 quant-NPL 项目中，DataFrame 用于：

### 1. 存储新闻数据

```python
# 新闻数据 DataFrame
news_df = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-02'],
    'stock_code': ['000001', '000002'],
    'title': ['公司业绩大涨', '市场波动'],
    'sentiment': [0.85, -0.32]
})
```

### 2. 存储股票价格数据

```python
# 价格数据 DataFrame
price_df = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-02'],
    'stock_code': ['000001', '000001'],
    'close_price': [10.5, 10.8],
    'return': [0.05, 0.03]
})
```

### 3. 合并数据进行分析

```python
# 将新闻情绪和股票收益率合并
merged_df = pd.merge(news_df, price_df, on=['date', 'stock_code'])
```

## 📝 本章练习

本章包含 8 个练习，帮助你掌握 DataFrame 的基础操作：

1. **练习1**：创建 DataFrame
2. **练习2**：查看数据形状和信息
3. **练习3**：选择单列
4. **练习4**：选择多列
5. **练习5**：选择行
6. **练习6**：选择特定单元格
7. **练习7**：添加新列
8. **练习8**：综合练习 - 处理股票数据

## 🚀 开始练习

```bash
# 测试单个练习
python test.py 2.4.1

# 测试整个章节
python test.py 2.4
```

加油！掌握 DataFrame 是数据分析的第一步！
