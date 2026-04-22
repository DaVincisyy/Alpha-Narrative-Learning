# 第 5 章：面向对象编程（OOP）

## 🎯 本章目标

学习如何使用类和对象来组织代码，理解面向对象编程的核心概念。

---

## 📖 为什么需要面向对象？

想象你要管理一个投资组合，包含多只股票。每只股票都有：
- 属性：代码、名称、价格、持有数量
- 行为：计算总价值、更新价格、买入、卖出

如果用函数和字典，代码会很分散：

```python
# ❌ 分散的代码
stock = {'code': 'AAPL', 'price': 150.25, 'shares': 100}

def calculate_value(stock):
    return stock['price'] * stock['shares']

def buy_shares(stock, shares):
    stock['shares'] += shares
```

用类和对象，代码更清晰：

```python
# ✅ 组织良好的代码
class Stock:
    def __init__(self, code, price, shares):
        self.code = code
        self.price = price
        self.shares = shares
    
    def calculate_value(self):
        return self.price * self.shares
    
    def buy(self, shares):
        self.shares += shares

# 使用
apple = Stock('AAPL', 150.25, 100)
print(apple.calculate_value())  # 15025.0
apple.buy(50)
```

---

## 1️⃣ 类和对象基础

### 什么是类和对象？

- **类（Class）**：蓝图、模板
- **对象（Object）**：根据蓝图创建的实例

就像：
- 类 = 房屋设计图
- 对象 = 根据设计图建造的实际房子

### 创建第一个类

```python
class Stock:
    """股票类"""
    
    def __init__(self, code, name, price):
        """初始化方法（构造函数）"""
        self.code = code      # 实例属性
        self.name = name
        self.price = price
    
    def display(self):
        """显示股票信息"""
        print(f"{self.code}: {self.name} - ${self.price}")

# 创建对象
apple = Stock('AAPL', 'Apple Inc.', 150.25)
google = Stock('GOOGL', 'Alphabet Inc.', 2800.50)

# 使用对象
apple.display()   # AAPL: Apple Inc. - $150.25
google.display()  # GOOGL: Alphabet Inc. - $2800.50

# 访问属性
print(apple.code)   # AAPL
print(google.price) # 2800.50
```

### 关键概念

1. **`__init__` 方法**：初始化对象时自动调用
2. **`self` 参数**：代表对象本身，必须是第一个参数
3. **实例属性**：`self.code`、`self.name` 等
4. **实例方法**：类中定义的函数

---

## 2️⃣ 属性和方法

### 实例属性

```python
class Stock:
    def __init__(self, code, price, shares):
        self.code = code        # 公开属性
        self.price = price
        self.shares = shares
        self._cost = price      # 约定的"私有"属性（以 _ 开头）
    
    def get_cost(self):
        """获取成本价"""
        return self._cost

apple = Stock('AAPL', 150.25, 100)
print(apple.code)       # 可以直接访问
print(apple.get_cost()) # 通过方法访问私有属性
```

### 类属性

类属性被所有实例共享：

```python
class Stock:
    # 类属性
    market = 'NASDAQ'
    total_stocks = 0
    
    def __init__(self, code, price):
        self.code = code
        self.price = price
        Stock.total_stocks += 1  # 修改类属性

apple = Stock('AAPL', 150.25)
google = Stock('GOOGL', 2800.50)

print(Stock.market)        # NASDAQ
print(Stock.total_stocks)  # 2
print(apple.market)        # NASDAQ（也可以通过实例访问）
```

### 实例方法、类方法、静态方法

```python
class Stock:
    market = 'NASDAQ'
    
    def __init__(self, code, price):
        self.code = code
        self.price = price
    
    # 实例方法：操作实例数据
    def display(self):
        print(f"{self.code}: ${self.price}")
    
    # 类方法：操作类数据
    @classmethod
    def set_market(cls, market):
        cls.market = market
    
    # 静态方法：不需要访问实例或类数据
    @staticmethod
    def is_valid_code(code):
        return len(code) <= 5 and code.isupper()

# 使用
apple = Stock('AAPL', 150.25)
apple.display()                    # 实例方法
Stock.set_market('NYSE')           # 类方法
print(Stock.is_valid_code('AAPL')) # 静态方法：True
```

---

## 3️⃣ 继承

继承允许创建新类，复用现有类的代码。

### 基础继承

```python
class Asset:
    """资产基类"""
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def display(self):
        print(f"{self.name}: ${self.value}")

class Stock(Asset):
    """股票类，继承自 Asset"""
    def __init__(self, name, value, code, shares):
        super().__init__(name, value)  # 调用父类的 __init__
        self.code = code
        self.shares = shares
    
    def display(self):
        """重写父类方法"""
        print(f"{self.code} - {self.name}: ${self.value} ({self.shares} 股)")

class Bond(Asset):
    """债券类，继承自 Asset"""
    def __init__(self, name, value, interest_rate):
        super().__init__(name, value)
        self.interest_rate = interest_rate

# 使用
apple = Stock('Apple Inc.', 15025, 'AAPL', 100)
bond = Bond('US Treasury', 10000, 0.02)

apple.display()  # AAPL - Apple Inc.: $15025 (100 股)
bond.display()   # US Treasury: $10000
```

### 多态

不同的类可以有相同的方法名，但行为不同：

```python
class Portfolio:
    def __init__(self):
        self.assets = []
    
    def add_asset(self, asset):
        self.assets.append(asset)
    
    def display_all(self):
        for asset in self.assets:
            asset.display()  # 多态：不同类型的 asset 调用各自的 display

portfolio = Portfolio()
portfolio.add_asset(Stock('Apple', 15025, 'AAPL', 100))
portfolio.add_asset(Bond('Treasury', 10000, 0.02))
portfolio.display_all()
```

---

## 4️⃣ 魔法方法（特殊方法）

魔法方法以双下划线开头和结尾，让对象支持内置操作。

### 常用魔法方法

```python
class Stock:
    def __init__(self, code, price, shares):
        self.code = code
        self.price = price
        self.shares = shares
    
    def __str__(self):
        """print() 时调用"""
        return f"{self.code}: ${self.price} x {self.shares}"
    
    def __repr__(self):
        """交互式环境显示"""
        return f"Stock('{self.code}', {self.price}, {self.shares})"
    
    def __len__(self):
        """len() 时调用"""
        return self.shares
    
    def __eq__(self, other):
        """== 比较时调用"""
        return self.code == other.code
    
    def __lt__(self, other):
        """< 比较时调用"""
        return self.price < other.price
    
    def __add__(self, other):
        """+ 运算时调用"""
        if self.code == other.code:
            return Stock(self.code, self.price, self.shares + other.shares)
        raise ValueError("不能合并不同的股票")

# 使用
apple1 = Stock('AAPL', 150.25, 100)
apple2 = Stock('AAPL', 150.25, 50)
google = Stock('GOOGL', 2800.50, 20)

print(apple1)              # AAPL: $150.25 x 100
print(len(apple1))         # 100
print(apple1 == apple2)    # True（代码相同）
print(apple1 < google)     # True（价格更低）

combined = apple1 + apple2
print(combined)            # AAPL: $150.25 x 150
```

### 常用魔法方法列表

| 方法 | 说明 | 示例 |
|------|------|------|
| `__init__` | 初始化 | `Stock('AAPL', 150)` |
| `__str__` | 字符串表示 | `print(stock)` |
| `__repr__` | 开发者表示 | `stock` |
| `__len__` | 长度 | `len(stock)` |
| `__eq__` | 相等比较 | `stock1 == stock2` |
| `__lt__` | 小于比较 | `stock1 < stock2` |
| `__add__` | 加法 | `stock1 + stock2` |
| `__getitem__` | 索引访问 | `stock[0]` |
| `__contains__` | 成员测试 | `'AAPL' in stock` |

---

## 5️⃣ 实战示例：投资组合管理系统

### 完整示例

```python
class Stock:
    """股票类"""
    def __init__(self, code, name, price, shares):
        self.code = code
        self.name = name
        self.price = price
        self.shares = shares
    
    def get_value(self):
        """计算总价值"""
        return self.price * self.shares
    
    def update_price(self, new_price):
        """更新价格"""
        self.price = new_price
    
    def buy(self, shares):
        """买入"""
        self.shares += shares
    
    def sell(self, shares):
        """卖出"""
        if shares > self.shares:
            raise ValueError("持有数量不足")
        self.shares -= shares
    
    def __str__(self):
        return f"{self.code}: {self.name} - ${self.price} x {self.shares} = ${self.get_value():.2f}"


class Portfolio:
    """投资组合类"""
    def __init__(self, name):
        self.name = name
        self.stocks = {}  # {code: Stock}
    
    def add_stock(self, stock):
        """添加股票"""
        if stock.code in self.stocks:
            # 如果已存在，增加持有数量
            self.stocks[stock.code].shares += stock.shares
        else:
            self.stocks[stock.code] = stock
    
    def remove_stock(self, code):
        """移除股票"""
        if code in self.stocks:
            del self.stocks[code]
    
    def get_total_value(self):
        """计算总价值"""
        return sum(stock.get_value() for stock in self.stocks.values())
    
    def display(self):
        """显示投资组合"""
        print(f"\n{'='*60}")
        print(f"投资组合: {self.name}")
        print(f"{'='*60}")
        for stock in self.stocks.values():
            print(stock)
        print(f"{'='*60}")
        print(f"总价值: ${self.get_total_value():.2f}")
        print(f"{'='*60}\n")
    
    def __len__(self):
        """返回股票数量"""
        return len(self.stocks)
    
    def __contains__(self, code):
        """检查是否包含某只股票"""
        return code in self.stocks


# 使用示例
portfolio = Portfolio("我的投资组合")

# 添加股票
portfolio.add_stock(Stock('AAPL', 'Apple Inc.', 150.25, 100))
portfolio.add_stock(Stock('GOOGL', 'Alphabet Inc.', 2800.50, 20))
portfolio.add_stock(Stock('MSFT', 'Microsoft Corp.', 300.75, 50))

# 显示组合
portfolio.display()

# 更新价格
portfolio.stocks['AAPL'].update_price(155.00)

# 买入更多
portfolio.stocks['AAPL'].buy(50)

# 显示更新后的组合
portfolio.display()

# 检查是否包含某只股票
print('AAPL' in portfolio)  # True
print('TSLA' in portfolio)  # False
```

---

## 📝 本章小结

### 核心概念

1. **类和对象**
   - 类是模板，对象是实例
   - `__init__` 初始化对象
   - `self` 代表对象本身

2. **属性和方法**
   - 实例属性：每个对象独有
   - 类属性：所有对象共享
   - 实例方法、类方法、静态方法

3. **继承**
   - 子类继承父类的属性和方法
   - `super()` 调用父类方法
   - 方法重写（Override）

4. **魔法方法**
   - `__str__`、`__repr__`：字符串表示
   - `__len__`、`__eq__`：支持内置操作
   - `__add__`、`__lt__`：运算符重载

### 最佳实践

- ✅ 类名使用大驼峰命名（PascalCase）
- ✅ 方法名使用小写加下划线（snake_case）
- ✅ 私有属性以单下划线开头（`_attribute`）
- ✅ 使用 `super()` 调用父类方法
- ✅ 实现 `__str__` 方便调试

### OOP 的优势

- 📦 **封装**：数据和方法组织在一起
- 🔄 **复用**：通过继承复用代码
- 🎭 **多态**：不同对象可以有相同接口
- 🧩 **模块化**：代码更易维护和扩展

---

## 🎯 下一步

完成 `practice.py` 中的练习题，然后运行 `python test_practice.py` 检查你的答案！
