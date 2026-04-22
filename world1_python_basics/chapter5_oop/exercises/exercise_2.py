"""
练习 2：添加买入和卖出方法

任务：在股票类的基础上添加交易功能
"""

class TradableStock:
    """
    可交易股票类

    在 Stock 的基础上添加交易功能

    属性:
        code, name, price, shares（同 Stock）

    方法:
        __init__(code, name, price, shares): 初始化
        get_value(): 返回总价值
        buy(shares): 买入指定数量的股票
        sell(shares): 卖出指定数量的股票
                      如果持有数量不足，返回 False
                      否则返回 True

    示例:
        stock = TradableStock('AAPL', 'Apple', 150.25, 100)
        stock.buy(50)
        print(stock.shares)  # 150
        stock.sell(30)
        print(stock.shares)  # 120
        stock.sell(200)      # 返回 False（数量不足）
    """
    pass
