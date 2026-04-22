"""
练习 4：创建投资组合类

任务：实现一个管理多个股票的投资组合类
"""

class Portfolio:
    """
    投资组合类

    属性:
        name: 组合名称（字符串）
        stocks: 股票字典 {code: Stock对象}

    方法:
        __init__(name): 初始化，stocks 为空字典
        add_stock(stock): 添加股票
                          如果代码已存在，增加持有数量
                          否则添加新股票
        remove_stock(code): 移除指定代码的股票
        get_total_value(): 返回所有股票的总价值
        get_stock_count(): 返回股票种类数量
        __len__(): 返回股票种类数量
        __contains__(code): 检查是否包含指定代码的股票

    示例:
        portfolio = Portfolio("我的组合")
        portfolio.add_stock(Stock('AAPL', 'Apple', 150.25, 100))
        portfolio.add_stock(Stock('GOOGL', 'Google', 2800.50, 20))

        print(len(portfolio))           # 2
        print('AAPL' in portfolio)      # True
        print(portfolio.get_total_value())  # 71035.0
    """
    pass
