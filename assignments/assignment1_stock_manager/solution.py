"""
作业 1：股票数据管理器

完成下面的函数，实现一个完整的股票投资组合管理系统。

数据结构说明：
- 投资组合（portfolio）：列表，包含多个股票字典
- 股票字典格式：{"ticker": "AAPL", "price": 150.25, "shares": 100}
"""


def add_stock(portfolio, ticker, price, shares):
    """
    功能 1：向投资组合添加股票

    参数：
        portfolio (list): 投资组合列表
        ticker (str): 股票代码
        price (float): 股票价格
        shares (int): 持有数量

    返回：
        list: 更新后的投资组合

    例子：
        >>> portfolio = []
        >>> portfolio = add_stock(portfolio, "AAPL", 150.25, 100)
        >>> print(portfolio)
        [{'ticker': 'AAPL', 'price': 150.25, 'shares': 100}]

    提示：
    1. 创建一个字典，包含 ticker, price, shares 三个键
    2. 将字典添加到 portfolio 列表中
    3. 返回更新后的 portfolio
    """
    # 在这里写你的代码
    pass


def calculate_total_value(portfolio):
    """
    功能 2：计算投资组合总价值

    总价值 = 每只股票的（价格 × 数量）之和

    参数：
        portfolio (list): 投资组合列表

    返回：
        float: 投资组合总价值

    例子：
        >>> portfolio = [
        ...     {"ticker": "AAPL", "price": 150, "shares": 10},
        ...     {"ticker": "GOOGL", "price": 2800, "shares": 5}
        ... ]
        >>> total = calculate_total_value(portfolio)
        >>> print(total)
        15500.0

    提示：
    1. 创建变量 total = 0
    2. 循环遍历 portfolio
    3. 每次循环：total += stock["price"] * stock["shares"]
    4. 返回 total
    """
    # 在这里写你的代码
    pass


def find_most_expensive(portfolio):
    """
    功能 3：找出价格最高的股票

    参数：
        portfolio (list): 投资组合列表

    返回：
        dict: 价格最高的股票字典，如果列表为空返回 None

    例子：
        >>> portfolio = [
        ...     {"ticker": "AAPL", "price": 150},
        ...     {"ticker": "GOOGL", "price": 2800},
        ...     {"ticker": "MSFT", "price": 380}
        ... ]
        >>> most_expensive = find_most_expensive(portfolio)
        >>> print(most_expensive["ticker"])
        GOOGL

    提示：
    1. 如果 portfolio 为空，返回 None
    2. 假设第一个股票是最贵的：max_stock = portfolio[0]
    3. 循环遍历剩余股票
    4. 如果发现更贵的，更新 max_stock
    5. 返回 max_stock
    """
    # 在这里写你的代码
    pass


def filter_high_value_stocks(portfolio, threshold):
    """
    功能 4：筛选出价值超过阈值的股票

    股票价值 = price * shares

    参数：
        portfolio (list): 投资组合列表
        threshold (float): 价值阈值

    返回：
        list: 价值超过阈值的股票列表

    例子：
        >>> portfolio = [
        ...     {"ticker": "AAPL", "price": 150, "shares": 100},  # 价值 15000
        ...     {"ticker": "GOOGL", "price": 2800, "shares": 5},  # 价值 14000
        ...     {"ticker": "MSFT", "price": 100, "shares": 50}    # 价值 5000
        ... ]
        >>> high_value = filter_high_value_stocks(portfolio, 10000)
        >>> print([s["ticker"] for s in high_value])
        ['AAPL', 'GOOGL']

    提示：
    1. 创建空列表 result = []
    2. 循环遍历 portfolio
    3. 计算每只股票的价值：value = stock["price"] * stock["shares"]
    4. 如果 value > threshold，添加到 result
    5. 返回 result
    """
    # 在这里写你的代码
    pass


def generate_report(portfolio):
    """
    功能 5：生成投资报告

    报告包含：
    - total_value: 总价值
    - stock_count: 股票数量
    - average_price: 平均价格
    - most_expensive_ticker: 最贵股票的代码

    参数：
        portfolio (list): 投资组合列表

    返回：
        dict: 包含统计信息的报告字典

    例子：
        >>> portfolio = [
        ...     {"ticker": "AAPL", "price": 150, "shares": 10},
        ...     {"ticker": "GOOGL", "price": 2800, "shares": 5}
        ... ]
        >>> report = generate_report(portfolio)
        >>> print(report["total_value"])
        15500.0
        >>> print(report["stock_count"])
        2

    提示：
    1. 使用前面写好的函数：calculate_total_value, find_most_expensive
    2. 计算平均价格：sum(所有价格) / 股票数量
    3. 创建字典包含所有统计信息
    """
    # 在这里写你的代码
    pass


# ============================================
# 🎉 完成所有函数后，运行测试：
# python test_assignment.py
# ============================================


# 可选：在这里测试你的代码
if __name__ == "__main__":
    # 创建测试数据
    my_portfolio = []
    my_portfolio = add_stock(my_portfolio, "AAPL", 150.25, 100)
    my_portfolio = add_stock(my_portfolio, "GOOGL", 2800.50, 10)
    my_portfolio = add_stock(my_portfolio, "MSFT", 380.00, 50)

    print("我的投资组合：")
    for stock in my_portfolio:
        print(f"  {stock['ticker']}: ${stock['price']} x {stock['shares']}")

    print(f"\n总价值: ${calculate_total_value(my_portfolio):.2f}")

    most_expensive = find_most_expensive(my_portfolio)
    if most_expensive:
        print(f"最贵的股票: {most_expensive['ticker']} (${most_expensive['price']})")

    high_value = filter_high_value_stocks(my_portfolio, 15000)
    print(f"\n价值超过 $15000 的股票:")
    for stock in high_value:
        value = stock['price'] * stock['shares']
        print(f"  {stock['ticker']}: ${value:.2f}")

    report = generate_report(my_portfolio)
    print(f"\n投资报告:")
    print(f"  股票数量: {report.get('stock_count', 'N/A')}")
    print(f"  总价值: ${report.get('total_value', 0):.2f}")
    print(f"  平均价格: ${report.get('average_price', 0):.2f}")
    print(f"  最贵股票: {report.get('most_expensive_ticker', 'N/A')}")
