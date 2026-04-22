"""
练习 12：使用关键字参数创建股票

任务：使用关键字参数创建股票字典
参数：
    **kwargs: 任意关键字参数

返回：
    包含所有传入参数的字典

示例：
    create_stock_flexible(code='AAPL', name='Apple', price=150.25)
    # 返回: {'code': 'AAPL', 'name': 'Apple', 'price': 150.25}

    create_stock_flexible(code='GOOGL', price=2800, sector='Tech')
    # 返回: {'code': 'GOOGL', 'price': 2800, 'sector': 'Tech'}
"""

def create_stock_flexible(**kwargs):
    """
    使用关键字参数创建股票字典

    参数:
        **kwargs: 任意关键字参数

    返回:
        包含所有传入参数的字典

    示例:
        create_stock_flexible(code='AAPL', name='Apple', price=150.25)
        # 返回: {'code': 'AAPL', 'name': 'Apple', 'price': 150.25}

        create_stock_flexible(code='GOOGL', price=2800, sector='Tech')
        # 返回: {'code': 'GOOGL', 'price': 2800, 'sector': 'Tech'}
    """
    pass
