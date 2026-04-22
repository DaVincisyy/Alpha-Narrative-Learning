"""
练习 3：实现魔法方法

任务：实现魔法方法支持比较和字符串表示
"""

class ComparableStock:
    """
    可比较的股票类

    实现魔法方法支持比较和字符串表示

    属性:
        code, name, price, shares

    方法:
        __init__(code, name, price, shares): 初始化
        __str__(): 返回格式化字符串 "AAPL: $150.25"
        __repr__(): 返回 "Stock('AAPL', 150.25, 100)"
        __eq__(other): 比较股票代码是否相同
        __lt__(other): 比较价格大小
        __len__(): 返回持有数量

    示例:
        apple = ComparableStock('AAPL', 'Apple', 150.25, 100)
        google = ComparableStock('GOOGL', 'Google', 2800.50, 20)

        print(apple)           # AAPL: $150.25
        print(apple < google)  # True（价格更低）
        print(len(apple))      # 100
    """
    pass
