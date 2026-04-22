# 第 2 章：循环与条件判断

## 🎯 本章目标

学习如何遍历数据（循环）和根据条件做决策（if 判断）。

---

## 📖 为什么需要循环和条件？

想象你管理 100 只股票：
- 需要检查**每一只**股票的价格（循环）
- 找出价格**大于 100** 的股票（条件判断）
- 对**高价股**和**低价股**做不同处理（if-else）

手动一个个检查？太慢了！让代码自动完成！

---

## 1️⃣ for 循环 - 遍历数据

### 什么是 for 循环？

for 循环就像**流水线**，让每个元素依次经过处理。

### 基础语法

```python
# 遍历列表
stocks = ["AAPL", "GOOGL", "MSFT"]

for stock in stocks:
    print(stock)

# 输出：
# AAPL
# GOOGL
# MSFT
```

### 💡 理解循环的执行过程

```python
numbers = [1, 2, 3]

for num in numbers:
    print(f"当前数字是: {num}")

# 执行过程：
# 第 1 次循环：num = 1，打印 "当前数字是: 1"
# 第 2 次循环：num = 2，打印 "当前数字是: 2"
# 第 3 次循环：num = 3，打印 "当前数字是: 3"
# 循环结束
```

### 遍历字典

```python
company = {
    "name": "Apple",
    "ticker": "AAPL",
    "price": 150.25
}

# 遍历键
for key in company:
    print(key)  # name, ticker, price

# 遍历值
for value in company.values():
    print(value)  # Apple, AAPL, 150.25

# 同时遍历键和值
for key, value in company.items():
    print(f"{key}: {value}")
    # name: Apple
    # ticker: AAPL
    # price: 150.25
```

### range() 函数 - 生成数字序列

```python
# 生成 0 到 4 的数字
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 生成 1 到 5 的数字
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# 步长为 2
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### 实战例子：计算总价值

```python
prices = [150.25, 2800.50, 380.00]
total = 0

for price in prices:
    total = total + price  # 或者写成 total += price

print(f"总价值: {total}")  # 3330.75
```

---

## 2️⃣ if 条件判断 - 做决策

### 什么是条件判断？

if 就像**红绿灯**，根据条件决定走哪条路。

### 基础语法

```python
price = 150.25

if price > 100:
    print("这是高价股")

# 输出：这是高价股
```

### if-else：两个选择

```python
price = 50.0

if price > 100:
    print("高价股")
else:
    print("低价股")

# 输出：低价股
```

### if-elif-else：多个选择

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 输出：良好
```

### 比较运算符

```python
# == 等于
5 == 5  # True
5 == 3  # False

# != 不等于
5 != 3  # True

# > 大于
5 > 3  # True

# < 小于
3 < 5  # True

# >= 大于等于
5 >= 5  # True

# <= 小于等于
3 <= 5  # True
```

### 逻辑运算符

```python
# and：两个条件都要满足
price = 150
volume = 1000000

if price > 100 and volume > 500000:
    print("高价且高成交量")

# or：满足任意一个条件
if price > 200 or volume > 2000000:
    print("高价或高成交量")

# not：取反
if not price < 50:
    print("价格不低于 50")
```

---

## 3️⃣ 循环 + 条件：强大组合

### 筛选数据

```python
prices = [45.0, 150.25, 30.5, 200.0, 80.0]
high_prices = []

for price in prices:
    if price > 100:
        high_prices.append(price)

print(high_prices)  # [150.25, 200.0]
```

### 计数

```python
stocks = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
count = 0

for stock in stocks:
    if len(stock) == 4:  # 股票代码长度为 4
        count += 1

print(f"4 个字母的股票有 {count} 个")  # 4 个
```

### 查找

```python
companies = [
    {"ticker": "AAPL", "price": 150.25},
    {"ticker": "GOOGL", "price": 2800.50},
    {"ticker": "MSFT", "price": 380.00}
]

# 查找 GOOGL 的价格
for company in companies:
    if company["ticker"] == "GOOGL":
        print(f"GOOGL 的价格是: {company['price']}")
        break  # 找到后退出循环
```

---

## 4️⃣ 列表推导式 - 简洁写法

### 什么是列表推导式？

一行代码完成循环 + 筛选 + 创建新列表。

### 基础语法

```python
# 传统写法
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)

# 列表推导式（一行搞定）
squares = [num ** 2 for num in numbers]
print(squares)  # [1, 4, 9, 16, 25]
```

### 带条件的列表推导式

```python
# 筛选出大于 100 的价格
prices = [45.0, 150.25, 30.5, 200.0, 80.0]
high_prices = [price for price in prices if price > 100]
print(high_prices)  # [150.25, 200.0]
```

---

## 🎮 实战例子：股票筛选器

```python
# 股票数据
portfolio = [
    {"ticker": "AAPL", "price": 150.25, "shares": 100},
    {"ticker": "GOOGL", "price": 2800.50, "shares": 10},
    {"ticker": "MSFT", "price": 380.00, "shares": 50},
    {"ticker": "TSLA", "price": 250.00, "shares": 20}
]

# 任务 1：计算总资产
total_value = 0
for stock in portfolio:
    value = stock["price"] * stock["shares"]
    total_value += value

print(f"总资产: ${total_value:.2f}")

# 任务 2：找出价值超过 10000 的持仓
high_value_stocks = []
for stock in portfolio:
    value = stock["price"] * stock["shares"]
    if value > 10000:
        high_value_stocks.append(stock["ticker"])

print(f"高价值持仓: {high_value_stocks}")

# 任务 3：给所有股票打标签
for stock in portfolio:
    price = stock["price"]
    if price > 1000:
        stock["category"] = "高价股"
    elif price > 100:
        stock["category"] = "中价股"
    else:
        stock["category"] = "低价股"

# 打印结果
for stock in portfolio:
    print(f"{stock['ticker']}: {stock['category']}")
```

---

## ✍️ 练习题

打开 `practice.py` 完成练习：

1. **练习 1**：遍历列表并打印每个元素
2. **练习 2**：计算列表中所有数字的总和
3. **练习 3**：筛选出大于某个值的数字
4. **练习 4**：判断价格等级（高/中/低）
5. **练习 5**：统计满足条件的元素数量
6. **练习 6**：查找字典列表中的特定项
7. **练习 7**：使用列表推导式

完成后运行测试：
```bash
python test_practice.py
```

---

## 🔑 关键要点

1. **for 循环**：`for item in items:` 遍历每个元素
2. **if 判断**：`if 条件:` 根据条件执行代码
3. **比较运算符**：`>`, `<`, `==`, `!=`, `>=`, `<=`
4. **逻辑运算符**：`and`, `or`, `not`
5. **循环 + 条件**：强大的数据处理组合
6. **列表推导式**：简洁的一行写法

---

## 📚 下一章预告

学会了循环和条件后，下一章我们将学习**函数**：如何把重复的代码封装起来，让代码更简洁、更易维护。

继续加油！🚀
