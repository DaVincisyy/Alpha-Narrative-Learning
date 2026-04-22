"""
练习 6：类方法和静态方法

任务：实现类方法和静态方法
"""

class StockValidator:
    """
    股票验证器类

    类属性:
        valid_markets: 有效市场列表 ['NASDAQ', 'NYSE', 'AMEX']

    方法:
        __init__(code, market): 初始化
        is_valid_code(code): 静态方法
                             检查代码是否有效（1-5个大写字母）
        is_valid_market(market): 类方法
                                 检查市场是否在 valid_markets 中
        validate(): 实例方法
                    返回 True 如果代码和市场都有效

    示例:
        print(StockValidator.is_valid_code('AAPL'))  # True
        print(StockValidator.is_valid_code('apple')) # False

        validator = StockValidator('AAPL', 'NASDAQ')
        print(validator.validate())  # True
    """
    valid_markets = ['NASDAQ', 'NYSE', 'AMEX']

    pass
