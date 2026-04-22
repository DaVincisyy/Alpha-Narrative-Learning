# 第 4 章：文件操作与异常处理

## 🎯 本章目标

学习如何读写文件、处理不同格式的数据，以及优雅地处理程序错误。

---

## 📖 为什么需要文件操作？

在量化金融项目中，我们经常需要：
- 读取股票数据文件（CSV 格式）
- 保存分析结果（JSON 格式）
- 处理可能出现的错误（文件不存在、格式错误等）

---

## 1️⃣ 读写文本文件

### 基础文件操作

```python
# 写入文件
with open('stock_list.txt', 'w', encoding='utf-8') as f:
    f.write('AAPL\n')
    f.write('GOOGL\n')
    f.write('MSFT\n')

# 读取文件
with open('stock_list.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # 读取全部内容
    print(content)

# 按行读取
with open('stock_list.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # 返回列表，每行是一个元素
    for line in lines:
        print(line.strip())  # strip() 去掉换行符
```

### 为什么用 with？

`with` 语句会自动关闭文件，即使出错也能正确关闭：

```python
# ❌ 不推荐：需要手动关闭
f = open('data.txt', 'r')
content = f.read()
f.close()  # 如果前面出错，这行不会执行

# ✅ 推荐：自动关闭
with open('data.txt', 'r') as f:
    content = f.read()
# 文件自动关闭
```

---

## 2️⃣ CSV 文件处理

CSV（Comma-Separated Values）是存储表格数据的常用格式。

### 读取 CSV

```python
import csv

# 读取 CSV 文件
with open('stocks.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # 第一行是表头
    print(f"表头: {header}")
    
    for row in reader:
        code, name, price = row
        print(f"{code}: {name} - ${price}")
```

### 写入 CSV

```python
import csv

stocks = [
    ['AAPL', 'Apple Inc.', '150.25'],
    ['GOOGL', 'Alphabet Inc.', '2800.50'],
    ['MSFT', 'Microsoft Corp.', '300.75']
]

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Code', 'Name', 'Price'])  # 写表头
    writer.writerows(stocks)  # 写多行
```

### 使用字典读写 CSV

```python
import csv

# 读取为字典
with open('stocks.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Code']}: ${row['Price']}")

# 写入字典
stocks = [
    {'Code': 'AAPL', 'Name': 'Apple Inc.', 'Price': '150.25'},
    {'Code': 'GOOGL', 'Name': 'Alphabet Inc.', 'Price': '2800.50'}
]

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['Code', 'Name', 'Price']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(stocks)
```

---

## 3️⃣ JSON 文件处理

JSON（JavaScript Object Notation）是存储结构化数据的常用格式。

### JSON 基础

```python
import json

# Python 字典
stock_data = {
    'code': 'AAPL',
    'name': 'Apple Inc.',
    'price': 150.25,
    'shares': 100,
    'sector': 'Technology'
}

# 写入 JSON 文件
with open('stock.json', 'w', encoding='utf-8') as f:
    json.dump(stock_data, f, indent=4, ensure_ascii=False)

# 读取 JSON 文件
with open('stock.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data['name'])  # Apple Inc.
```

### JSON 字符串转换

```python
import json

# 字典转 JSON 字符串
stock = {'code': 'AAPL', 'price': 150.25}
json_str = json.dumps(stock)
print(json_str)  # '{"code": "AAPL", "price": 150.25}'

# JSON 字符串转字典
data = json.loads(json_str)
print(data['code'])  # AAPL
```

---

## 4️⃣ 异常处理

程序运行时可能遇到各种错误，我们需要优雅地处理它们。

### try-except 基础

```python
# ❌ 没有异常处理：程序会崩溃
price = int(input("输入价格: "))  # 如果输入 "abc" 会报错

# ✅ 有异常处理：程序继续运行
try:
    price = int(input("输入价格: "))
    print(f"价格是: {price}")
except ValueError:
    print("错误：请输入数字！")
```

### 常见异常类型

```python
# FileNotFoundError - 文件不存在
try:
    with open('not_exist.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在！")

# ValueError - 值错误
try:
    number = int("abc")
except ValueError:
    print("无法转换为数字！")

# KeyError - 键不存在
try:
    data = {'name': 'Apple'}
    print(data['price'])
except KeyError:
    print("键不存在！")

# ZeroDivisionError - 除以零
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零！")
```

### 捕获多个异常

```python
try:
    with open('stocks.csv', 'r') as f:
        price = float(f.readline())
        result = 100 / price
except FileNotFoundError:
    print("文件不存在")
except ValueError:
    print("数据格式错误")
except ZeroDivisionError:
    print("价格不能为零")
except Exception as e:
    print(f"其他错误: {e}")
```

### else 和 finally

```python
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在")
else:
    # 没有异常时执行
    print("文件读取成功")
finally:
    # 无论是否异常都执行
    print("操作完成")
```

---

## 5️⃣ 实战示例：股票数据处理

### 示例 1：读取并验证 CSV 数据

```python
import csv

def load_stock_data(filename):
    """读取股票数据，处理可能的错误"""
    stocks = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # 验证数据
                    stock = {
                        'code': row['Code'],
                        'name': row['Name'],
                        'price': float(row['Price'])
                    }
                    stocks.append(stock)
                except (KeyError, ValueError) as e:
                    print(f"跳过无效行: {row}, 错误: {e}")
                    continue
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return []
    
    return stocks

# 使用
stocks = load_stock_data('stocks.csv')
print(f"成功加载 {len(stocks)} 条数据")
```

### 示例 2：保存分析结果

```python
import json

def save_analysis_result(stocks, filename):
    """保存分析结果到 JSON 文件"""
    result = {
        'total_stocks': len(stocks),
        'average_price': sum(s['price'] for s in stocks) / len(stocks),
        'stocks': stocks
    }
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        print(f"结果已保存到 {filename}")
        return True
    except Exception as e:
        print(f"保存失败: {e}")
        return False

# 使用
stocks = [
    {'code': 'AAPL', 'name': 'Apple', 'price': 150.25},
    {'code': 'GOOGL', 'name': 'Google', 'price': 2800.50}
]
save_analysis_result(stocks, 'result.json')
```

---

## 📝 本章小结

### 核心概念

1. **文件操作**
   - 使用 `with open()` 读写文件
   - `'r'` 读取，`'w'` 写入，`'a'` 追加

2. **CSV 处理**
   - `csv.reader()` / `csv.writer()` - 列表方式
   - `csv.DictReader()` / `csv.DictWriter()` - 字典方式

3. **JSON 处理**
   - `json.load()` / `json.dump()` - 文件操作
   - `json.loads()` / `json.dumps()` - 字符串操作

4. **异常处理**
   - `try-except` 捕获异常
   - `else` 无异常时执行
   - `finally` 总是执行

### 最佳实践

- ✅ 总是使用 `with` 语句操作文件
- ✅ 指定 `encoding='utf-8'` 避免编码问题
- ✅ 捕获具体的异常类型，不要用空 `except`
- ✅ 在文件操作中添加异常处理
- ✅ 使用 `strip()` 去除多余的空白字符

---

## 🎯 下一步

完成 `practice.py` 中的练习题，然后运行 `python test_practice.py` 检查你的答案！
