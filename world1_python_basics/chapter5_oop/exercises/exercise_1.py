"""
练习 1：创建基础股票类

任务：实现一个基础的股票类
"""

class Stock:
    """
    股票类

    属性:
        code: 股票代码（字符串）
        name: 公司名称（字符串）
        price: 当前价格（浮点数）
        shares: 持有数量（整数）

    方法:
        __init__(code, name, price, shares): 初始化
        get_value(): 返回总价值（price * shares）
        display(): 打印股票信息，格式："AAPL: Apple Inc. - $150.25 x 100"

    示例:
        apple = Stock('AAPL', 'Apple Inc.', 150.25, 100)
        print(apple.get_value())  # 15025.0
        apple.display()           # AAPL: Apple Inc. - $150.25 x 100
    """
    pass
