"""
练习 14：使用 Lambda 筛选

任务：使用自定义条件筛选股票
参数：
    stocks: 股票列表
    condition: 筛选条件函数（lambda 或普通函数）

返回：
    满足条件的股票列表

示例：
    stocks = [
        {'code': 'AAPL', 'price': 150},
        {'code': 'GOOGL', 'price': 2800},
        {'code': 'MSFT', 'price': 300}
    ]

    # 筛选价格大于 200 的股票
    filter_stocks_by_condition(stocks, lambda s: s['price'] > 200)
    # 返回: [{'code': 'GOOGL', 'price': 2800}, {'code': 'MSFT', 'price': 300}]

    # 筛选代码以 'A' 开头的股票
    filter_stocks_by_condition(stocks, lambda s: s['code'].startswith('A'))
    # 返回: [{'code': 'AAPL', 'price': 150}]
"""

def filter_stocks_by_condition(stocks, condition):
    """
    使用自定义条件筛选股票

    参数:
        stocks: 股票列表
        condition: 筛选条件函数（lambda 或普通函数）

    返回:
        满足条件的股票列表

    示例:
        stocks = [
            {'code': 'AAPL', 'price': 150},
            {'code': 'GOOGL', 'price': 2800},
            {'code': 'MSFT', 'price': 300}
        ]

        # 筛选价格大于 200 的股票
        filter_stocks_by_condition(stocks, lambda s: s['price'] > 200)
        # 返回: [{'code': 'GOOGL', 'price': 2800}, {'code': 'MSFT', 'price': 300}]

        # 筛选代码以 'A' 开头的股票
        filter_stocks_by_condition(stocks, lambda s: s['code'].startswith('A'))
        # 返回: [{'code': 'AAPL', 'price': 150}]
    """
    pass
