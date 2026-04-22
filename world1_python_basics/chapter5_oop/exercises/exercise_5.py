"""
练习 5：继承 - 创建资产基类

任务：使用继承创建资产类层次结构
"""

class Asset:
    """
    资产基类

    属性:
        name: 资产名称
        value: 资产价值

    方法:
        __init__(name, value): 初始化
        get_value(): 返回价值
        display(): 打印 "资产名称: $价值"
    """
    pass


class StockAsset(Asset):
    """
    股票资产类，继承自 Asset

    属性:
        name, value（继承自 Asset）
        code: 股票代码
        shares: 持有数量

    方法:
        __init__(name, value, code, shares): 初始化
        display(): 重写父类方法，打印 "AAPL - Apple: $15025 (100股)"

    示例:
        stock = StockAsset('Apple Inc.', 15025, 'AAPL', 100)
        stock.display()  # AAPL - Apple Inc.: $15025 (100股)
    """
    pass


class BondAsset(Asset):
    """
    债券资产类，继承自 Asset

    属性:
        name, value（继承自 Asset）
        interest_rate: 利率（浮点数，如 0.02 表示 2%）

    方法:
        __init__(name, value, interest_rate): 初始化
        get_annual_interest(): 返回年利息（value * interest_rate）

    示例:
        bond = BondAsset('US Treasury', 10000, 0.02)
        print(bond.get_annual_interest())  # 200.0
    """
    pass
