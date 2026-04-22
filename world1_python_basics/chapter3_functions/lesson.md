# 第 3 章：函数与模块

## 🎯 本章目标

学习如何定义和使用函数，理解参数、返回值、作用域等核心概念。

---

## 📖 为什么需要函数？

想象你需要多次计算股票的总价值：

```python
# ❌ 重复的代码
apple_value = 150.25 * 100
google_value = 2800.50 * 20
microsoft_value = 300.75 * 50
```

使用函数可以避免重复：

```python
# ✅ 使用函数
def calculate_value(price, shares):
    return price * shares

apple_value = calculate_value(150.25, 100)
google_value = calculate_value(2800.50, 20)
microsoft_value = calculate_value(300.75, 50)
```

---

## 1️⃣ 函数基础

### 定义和调用函数

```python
# 定义函数
def greet():
    """打招呼函数"""
    print("Hello, World!")

# 调用函数
greet()  # 输出: Hello, World!
```

### 带参数的函数

```python
def greet_user(name):
    """向指定用户打招呼"""
    print(f"Hello, {name}!")

greet_user("Alice")  # Hello, Alice!
greet_user("Bob")    # Hello, Bob!
```

### 带返回值的函数

```python
def calculate_value(price, shares):
    """计算股票总价值"""
    return price * shares

result = calculate_value(150.25, 100)
print(result)  # 15025.0
```

---

## 2️⃣ 参数类型

### 位置参数

```python
def create_stock(code, name, price):
    """创建股票字典"""
    return {
        'code': code,
        'name': name,
        'price': price
    }

# 必须按顺序传递参数
stock = create_stock('AAPL', 'Apple Inc.', 150.25)
```

### 关键字参数

```python
# 可以指定参数名，不需要按顺序
stock = create_stock(name='Apple Inc.', price=150.25, code='AAPL')
```

### 默认参数

```python
def create_stock(code, name, price, shares=0):
    """创建股票字典，shares 默认为 0"""
    return {
        'code': code,
        'name': name,
        'price': price,
        'shares': shares
    }

# 不传 shares，使用默认值 0
stock1 = create_stock('AAPL', 'Apple', 150.25)
print(stock1['shares'])  # 0

# 传递 shares
stock2 = create_stock('AAPL', 'Apple', 150.25, 100)
print(stock2['shares'])  # 100
```

### 可变参数 (*args)

```python
def calculate_total(*prices):
    """计算多个价格的总和"""
    return sum(prices)

total1 = calculate_total(100, 200, 300)  # 600
total2 = calculate_total(50, 75)         # 125
```

### 关键字可变参数 (**kwargs)

```python
def create_stock_info(**info):
    """创建股票信息字典"""
    return info

stock = create_stock_info(code='AAPL', name='Apple', price=150.25, sector='Tech')
print(stock)  # {'code': 'AAPL', 'name': 'Apple', 'price': 150.25, 'sector': 'Tech'}
```

---

## 3️⃣ 返回值

### 返回单个值

```python
def get_price(stock):
    """获取股票价格"""
    return stock['price']

stock = {'code': 'AAPL', 'price': 150.25}
price = get_price(stock)
print(price)  # 150.25
```

### 返回多个值

```python
def get_stock_info(stock):
    """获取股票代码和价格"""
    return stock['code'], stock['price']

# 返回的是元组
code, price = get_stock_info({'code': 'AAPL', 'price': 150.25})
print(code)   # AAPL
print(price)  # 150.25
```

### 返回 None

```python
def print_stock(stock):
    """打印股票信息，不返回值"""
    print(f"{stock['code']}: ${stock['price']}")
    # 没有 return 语句，默认返回 None

result = print_stock({'code': 'AAPL', 'price': 150.25})
print(result)  # None
```

---

## 4️⃣ 作用域

### 局部变量和全局变量

```python
# 全局变量
market = 'NASDAQ'

def display_market():
    """访问全局变量"""
    print(f"Market: {market}")

display_market()  # Market: NASDAQ

def change_market():
    """局部变量不影响全局变量"""
    market = 'NYSE'  # 这是局部变量
    print(f"Inside: {market}")

change_market()   # Inside: NYSE
print(market)     # NASDAQ（全局变量未改变）
```

### 使用 global 关键字

```python
market = 'NASDAQ'

def change_market_global():
    """修改全局变量"""
    global market
    market = 'NYSE'

change_market_global()
print(market)  # NYSE（全局变量被修改）
```

---

## 5️⃣ Lambda 函数

Lambda 函数是简短的匿名函数。

### 基础语法

```python
# 普通函数
def add(x, y):
    return x + y

# Lambda 函数
add_lambda = lambda x, y: x + y

print(add(3, 5))         # 8
print(add_lambda(3, 5))  # 8
```

### 实际应用

```python
stocks = [
    {'code': 'AAPL', 'price': 150.25},
    {'code': 'GOOGL', 'price': 2800.50},
    {'code': 'MSFT', 'price': 300.75}
]

# 按价格排序
sorted_stocks = sorted(stocks, key=lambda s: s['price'])
print([s['code'] for s in sorted_stocks])  # ['AAPL', 'MSFT', 'GOOGL']
```

---

## 6️⃣ map 和 filter

### map() - 对每个元素应用函数

```python
prices = [100, 200, 300, 400]

# 使用 map 计算每个价格的 10% 税
taxes = list(map(lambda p: p * 0.1, prices))
print(taxes)  # [10.0, 20.0, 30.0, 40.0]

# 等价的列表推导式
taxes = [p * 0.1 for p in prices]
```

### filter() - 筛选元素

```python
stocks = [
    {'code': 'AAPL', 'price': 150.25},
    {'code': 'GOOGL', 'price': 2800.50},
    {'code': 'MSFT', 'price': 300.75},
    {'code': 'TSLA', 'price': 200.00}
]

# 筛选价格大于 200 的股票
expensive = list(filter(lambda s: s['price'] > 200, stocks))
print([s['code'] for s in expensive])  # ['GOOGL', 'MSFT']

# 等价的列表推导式
expensive = [s for s in stocks if s['price'] > 200]
```

---

## 7️⃣ 文档字符串（Docstring）

```python
def calculate_portfolio_value(stocks):
    """
    计算投资组合的总价值
    
    参数:
        stocks: 股票列表，每个元素是字典，包含 'price' 和 'shares'
    
    返回:
        float: 投资组合总价值
    
    示例:
        >>> stocks = [{'price': 150, 'shares': 100}, {'price': 200, 'shares': 50}]
        >>> calculate_portfolio_value(stocks)
        25000.0
    """
    return sum(s['price'] * s['shares'] for s in stocks)

# 查看文档
print(calculate_portfolio_value.__doc__)
```

---

## 8️⃣ 实战示例：股票分析函数库

```python
def calculate_value(price, shares):
    """计算股票总价值"""
    return price * shares


def calculate_profit(buy_price, sell_price, shares):
    """计算利润"""
    return (sell_price - buy_price) * shares


def calculate_profit_rate(buy_price, sell_price):
    """计算收益率（百分比）"""
    return ((sell_price - buy_price) / buy_price) * 100


def filter_by_price(stocks, min_price, max_price):
    """筛选价格在指定范围内的股票"""
    return [s for s in stocks if min_price <= s['price'] <= max_price]


def get_top_stocks(stocks, n=5):
    """获取价格最高的 n 只股票"""
    sorted_stocks = sorted(stocks, key=lambda s: s['price'], reverse=True)
    return sorted_stocks[:n]


def calculate_average_price(stocks):
    """计算平均价格"""
    if not stocks:
        return 0
    return sum(s['price'] for s in stocks) / len(stocks)


def format_stock_info(stock):
    """格式化股票信息"""
    return f"{stock['code']}: {stock['name']} - ${stock['price']:.2f}"


# 使用示例
stocks = [
    {'code': 'AAPL', 'name': 'Apple', 'price': 150.25, 'shares': 100},
    {'code': 'GOOGL', 'name': 'Google', 'price': 2800.50, 'shares': 20},
    {'code': 'MSFT', 'name': 'Microsoft', 'price': 300.75, 'shares': 50},
    {'code': 'TSLA', 'name': 'Tesla', 'price': 200.00, 'shares': 30}
]

# 计算总价值
total = sum(calculate_value(s['price'], s['shares']) for s in stocks)
print(f"投资组合总价值: ${total:.2f}")

# 筛选价格在 100-500 之间的股票
mid_range = filter_by_price(stocks, 100, 500)
print(f"中等价格股票: {[s['code'] for s in mid_range]}")

# 获取价格最高的 2 只股票
top_2 = get_top_stocks(stocks, 2)
print(f"价格最高的股票: {[s['code'] for s in top_2]}")

# 计算平均价格
avg = calculate_average_price(stocks)
print(f"平均价格: ${avg:.2f}")

# 计算利润
profit = calculate_profit(150, 155, 100)
print(f"利润: ${profit:.2f}")

# 计算收益率
rate = calculate_profit_rate(150, 155)
print(f"收益率: {rate:.2f}%")
```

---

## 📝 本章小结

### 核心概念

1. **函数定义**
   - `def` 关键字
   - 参数和返回值
   - 文档字符串

2. **参数类型**
   - 位置参数、关键字参数
   - 默认参数
   - `*args` 和 `**kwargs`

3. **作用域**
   - 局部变量和全局变量
   - `global` 关键字

4. **高级特性**
   - Lambda 函数
   - `map()` 和 `filter()`
   - 列表推导式

### 最佳实践

- ✅ 函数名使用小写加下划线（snake_case）
- ✅ 每个函数只做一件事
- ✅ 添加文档字符串说明功能
- ✅ 使用有意义的参数名
- ✅ 避免修改全局变量
- ✅ 优先使用列表推导式而不是 map/filter

### 函数的优势

- 📦 **代码复用**：避免重复代码
- 🧩 **模块化**：将复杂问题分解
- 🔍 **易于测试**：独立测试每个函数
- 📖 **易于理解**：清晰的函数名表达意图

---

## 🎯 下一步

完成 `practice.py` 中的练习题，然后运行 `python test_practice.py` 检查你的答案！
