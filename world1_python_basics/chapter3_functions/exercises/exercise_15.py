"""
练习 15：计算加权平均价格

任务：计算加权平均价格（按持有数量加权）
参数：
    stocks: 股票列表，每个元素是字典，包含 'price' 和 'shares'

返回：
    加权平均价格（浮点数）
    如果总持有数量为 0，返回 0

公式：
    加权平均 = Σ(price * shares) / Σ(shares)

示例：
    stocks = [
        {'code': 'AAPL', 'price': 100, 'shares': 10},
        {'code': 'GOOGL', 'price': 200, 'shares': 5}
    ]
    calculate_weighted_average(stocks)
    # 返回: 133.33...
    # 计算: (100*10 + 200*5) / (10+5) = 2000/15 = 133.33
"""

def calculate_weighted_average(stocks):
    """
    计算加权平均价格（按持有数量加权）

    参数:
        stocks: 股票列表，每个元素是字典，包含 'price' 和 'shares'

    返回:
        加权平均价格（浮点数）
        如果总持有数量为 0，返回 0

    公式:
        加权平均 = Σ(price * shares) / Σ(shares)

    示例:
        stocks = [
            {'code': 'AAPL', 'price': 100, 'shares': 10},
            {'code': 'GOOGL', 'price': 200, 'shares': 5}
        ]
        calculate_weighted_average(stocks)
        # 返回: 133.33...
        # 计算: (100*10 + 200*5) / (10+5) = 2000/15 = 133.33
    """
    pass
