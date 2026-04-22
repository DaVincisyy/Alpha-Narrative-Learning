"""
练习 13：按价格排序

任务：按价格对股票列表排序
参数：
    stocks: 股票列表，每个元素是字典，包含 'price'
    reverse: 是否降序排序，默认 False（升序）

返回：
    排序后的新列表（不修改原列表）

示例：
    stocks = [
        {'code': 'AAPL', 'price': 150},
        {'code': 'GOOGL', 'price': 2800},
        {'code': 'MSFT', 'price': 300}
    ]
    sort_by_price(stocks)
    # 返回: [{'code': 'AAPL', 'price': 150}, {'code': 'MSFT', 'price': 300}, ...]

    sort_by_price(stocks, reverse=True)
    # 返回: [{'code': 'GOOGL', 'price': 2800}, {'code': 'MSFT', 'price': 300}, ...]
"""

def sort_by_price(stocks, reverse=False):
    """
    按价格对股票列表排序

    参数:
        stocks: 股票列表，每个元素是字典，包含 'price'
        reverse: 是否降序排序，默认 False（升序）

    返回:
        排序后的新列表（不修改原列表）

    示例:
        stocks = [
            {'code': 'AAPL', 'price': 150},
            {'code': 'GOOGL', 'price': 2800},
            {'code': 'MSFT', 'price': 300}
        ]
        sort_by_price(stocks)
        # 返回: [{'code': 'AAPL', 'price': 150}, {'code': 'MSFT', 'price': 300}, ...]

        sort_by_price(stocks, reverse=True)
        # 返回: [{'code': 'GOOGL', 'price': 2800}, {'code': 'MSFT', 'price': 300}, ...]
    """
    pass
