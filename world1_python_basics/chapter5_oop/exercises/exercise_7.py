"""
练习 7：实现迭代器

任务：创建一个支持迭代的股票列表类
"""

class StockList:
    """
    股票列表类，支持迭代

    属性:
        stocks: 股票列表

    方法:
        __init__(): 初始化空列表
        add(stock): 添加股票
        __len__(): 返回股票数量
        __getitem__(index): 支持索引访问
        __iter__(): 返回迭代器

    示例:
        stock_list = StockList()
        stock_list.add(Stock('AAPL', 'Apple', 150.25, 100))
        stock_list.add(Stock('GOOGL', 'Google', 2800.50, 20))

        for stock in stock_list:
            print(stock.code)

        print(stock_list[0].code)  # AAPL
        print(len(stock_list))     # 2
    """
    pass
