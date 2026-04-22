"""
练习 10：上下文管理器

任务：实现股票交易的上下文管理器
"""

class StockTransaction:
    """
    股票交易上下文管理器

    用于确保交易的原子性（要么全部成功，要么全部回滚）

    属性:
        stock: 股票对象
        original_shares: 原始持有数量

    方法:
        __init__(stock): 初始化
        __enter__(): 进入上下文，保存原始持有数量
        __exit__(exc_type, exc_val, exc_tb): 退出上下文
                                              如果有异常，回滚到原始数量

    示例:
        stock = Stock('AAPL', 'Apple', 150, 100)

        with StockTransaction(stock):
            stock.shares += 50
            # 如果这里出错，shares 会回滚到 100

        print(stock.shares)  # 150（成功）或 100（失败）
    """
    pass
