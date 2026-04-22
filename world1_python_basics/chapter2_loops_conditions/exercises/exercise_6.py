"""
练习 6：在字典列表中查找指定股票的价格
"""


def find_stock_price(companies, ticker):
    """
    在字典列表中查找指定股票的价格

    参数：
        companies (list): 公司信息字典列表，每个字典包含 "ticker" 和 "price"
        ticker (str): 要查找的股票代码

    返回：
        float: 股票价格，如果找不到返回 None

    例子：
        >>> companies = [
        ...     {"ticker": "AAPL", "price": 150.25},
        ...     {"ticker": "GOOGL", "price": 2800.50}
        ... ]
        >>> price = find_stock_price(companies, "GOOGL")
        >>> print(price)
        2800.5
    """
    # 在这里写你的代码
    # 提示：循环遍历，用 if 判断 ticker 是否匹配
    pass
