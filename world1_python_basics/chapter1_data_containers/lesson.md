# 第 1 章：数据容器 - 列表、字典、元组

## 🎯 本章目标

学习 Python 中最基础的三种数据容器，理解它们的区别和使用场景。

---

## 📖 什么是数据容器？

想象你要管理一家公司的股票信息。你需要：
- 存储多个股票代码（比如：AAPL, GOOGL, MSFT）
- 记录每个公司的详细信息（名称、价格、行业）
- 保存不能修改的固定数据（比如公司成立日期）

这就需要**数据容器**！

---

## 1️⃣ 列表（List）- 有序的数据集合

### 什么是列表？

列表就像一个**购物清单**，可以存储多个项目，并且：
- ✅ 有顺序（第一个、第二个...）
- ✅ 可以修改（添加、删除、更改）
- ✅ 可以重复（可以有两个 "AAPL"）

### 基础语法

```python
# 创建列表 - 用方括号 []
stock_codes = ["AAPL", "GOOGL", "MSFT"]

# 访问元素 - 用索引（从 0 开始！）
first_stock = stock_codes[0]  # "AAPL"
second_stock = stock_codes[1]  # "GOOGL"

# 修改元素
stock_codes[0] = "TSLA"  # 把第一个改成 TSLA

# 添加元素
stock_codes.append("NVDA")  # 在末尾添加

# 删除元素
stock_codes.remove("GOOGL")  # 删除指定元素

# 获取长度
length = len(stock_codes)  # 有多少个元素
```

### 💡 重要概念：索引从 0 开始

```python
fruits = ["苹果", "香蕉", "橙子"]
#         索引0   索引1   索引2

print(fruits[0])  # 输出：苹果
print(fruits[2])  # 输出：橙子
```

### 常用操作

```python
numbers = [1, 2, 3, 4, 5]

# 切片 - 获取一部分
first_three = numbers[0:3]  # [1, 2, 3]
last_two = numbers[-2:]     # [4, 5]

# 检查元素是否存在
if 3 in numbers:
    print("3 在列表中")

# 排序
numbers.sort()  # 从小到大排序
numbers.reverse()  # 反转顺序
```

---

## 2️⃣ 字典（Dictionary）- 键值对存储

### 什么是字典？

字典就像一个**通讯录**，每个名字对应一个电话号码：
- ✅ 用"键"（key）查找"值"（value）
- ✅ 无序（不关心顺序）
- ✅ 键不能重复，但值可以重复

### 基础语法

```python
# 创建字典 - 用花括号 {}
company_info = {
    "name": "Apple Inc.",
    "ticker": "AAPL",
    "price": 150.25,
    "industry": "Technology"
}

# 访问值 - 用键
company_name = company_info["name"]  # "Apple Inc."
stock_price = company_info["price"]  # 150.25

# 修改值
company_info["price"] = 155.00

# 添加新键值对
company_info["country"] = "USA"

# 删除键值对
del company_info["industry"]

# 检查键是否存在
if "price" in company_info:
    print("价格信息存在")
```

### 常用操作

```python
student = {
    "name": "张三",
    "age": 20,
    "grade": 85
}

# 获取所有键
keys = student.keys()  # ["name", "age", "grade"]

# 获取所有值
values = student.values()  # ["张三", 20, 85]

# 获取所有键值对
items = student.items()  # [("name", "张三"), ("age", 20), ...]

# 安全获取值（如果键不存在，返回默认值）
score = student.get("score", 0)  # 如果没有 "score"，返回 0
```

---

## 3️⃣ 元组（Tuple）- 不可变的列表

### 什么是元组？

元组就像**身份证号码**，一旦创建就不能修改：
- ✅ 有顺序
- ❌ 不能修改（不能添加、删除、更改）
- ✅ 比列表更快、更安全

### 基础语法

```python
# 创建元组 - 用圆括号 ()
company_founded = ("Apple", 1976, "California")

# 访问元素 - 和列表一样
company_name = company_founded[0]  # "Apple"
year = company_founded[1]  # 1976

# ❌ 不能修改
# company_founded[1] = 1977  # 这会报错！

# 元组解包
name, year, location = company_founded
print(name)  # "Apple"
print(year)  # 1976
```

### 什么时候用元组？

```python
# 1. 函数返回多个值
def get_stock_info():
    return ("AAPL", 150.25, "Technology")

ticker, price, industry = get_stock_info()

# 2. 作为字典的键（列表不能做键）
stock_data = {
    ("AAPL", "2024-01-01"): 150.25,
    ("GOOGL", "2024-01-01"): 2800.50
}

# 3. 保护数据不被修改
COMPANY_CODES = ("AAPL", "GOOGL", "MSFT")  # 常量
```

---

## 📊 三种容器对比

| 特性 | 列表 List | 字典 Dict | 元组 Tuple |
|------|----------|-----------|-----------|
| 符号 | `[]` | `{}` | `()` |
| 有序 | ✅ | ❌ | ✅ |
| 可修改 | ✅ | ✅ | ❌ |
| 重复元素 | ✅ | 键不能重复 | ✅ |
| 访问方式 | 索引 | 键 | 索引 |
| 使用场景 | 多个相同类型数据 | 键值对关系 | 固定不变的数据 |

---

## 🎮 实战例子：管理股票数据

```python
# 列表：存储多个股票代码
portfolio = ["AAPL", "GOOGL", "MSFT", "TSLA"]

# 字典：存储单个公司的详细信息
apple_info = {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "price": 150.25,
    "shares": 100
}

# 元组：存储不变的历史数据
apple_ipo = ("AAPL", "1980-12-12", 22.0)

# 组合使用：列表 + 字典
companies = [
    {"ticker": "AAPL", "price": 150.25},
    {"ticker": "GOOGL", "price": 2800.50},
    {"ticker": "MSFT", "price": 380.00}
]

# 访问第一个公司的价格
first_company_price = companies[0]["price"]  # 150.25
```

---

## ✍️ 练习题

现在打开 `practice.py` 文件，完成以下练习：

1. **练习 1**：创建一个包含 5 个股票代码的列表
2. **练习 2**：创建一个字典存储公司信息（名称、代码、价格）
3. **练习 3**：从列表中获取第 3 个元素
4. **练习 4**：修改字典中的价格
5. **练习 5**：创建一个元组存储公司成立信息

完成后运行测试：
```bash
python test_practice.py
```

---

## 🔑 关键要点

1. **列表**：用 `[]`，可修改，有序
2. **字典**：用 `{}`，键值对，用键访问
3. **元组**：用 `()`，不可修改，有序
4. **索引从 0 开始**！
5. 选择合适的容器：
   - 需要顺序 → 列表或元组
   - 需要查找 → 字典
   - 不能修改 → 元组

---

## 📚 下一章预告

学会了数据容器后，下一章我们将学习如何**遍历**这些数据（循环）和**筛选**数据（条件判断）。

准备好了吗？让我们开始练习！🚀
