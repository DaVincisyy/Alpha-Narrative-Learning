"""
练习 8：属性装饰器

任务：使用属性装饰器管理股票属性
"""

class ManagedStock:
    """
    使用属性装饰器管理股票

    属性:
        code: 股票代码（只读）
        _price: 私有价格属性
        price: 价格属性（使用 @property）
               getter: 返回 _price
               setter: 设置 _price，但必须 > 0

    方法:
        __init__(code, price): 初始化

    示例:
        stock = ManagedStock('AAPL', 150.25)
        print(stock.price)  # 150.25
        stock.price = 155.0 # 设置新价格
        stock.price = -10   # 应该抛出 ValueError
    """
    pass
