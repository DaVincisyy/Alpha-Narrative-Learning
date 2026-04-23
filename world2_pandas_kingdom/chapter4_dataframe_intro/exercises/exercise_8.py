"""
练习 8：综合练习 - 处理股票数据

任务：综合运用 DataFrame 操作处理股票数据
要求：
1. 创建包含股票代码、开盘价、收盘价的 DataFrame
2. 添加涨跌幅列（(收盘价 - 开盘价) / 开盘价）
3. 返回涨跌幅大于 0 的股票代码列表
"""

import pandas as pd


def analyze_stock_data(stock_codes, open_prices, close_prices):
    """
    分析股票数据，返回上涨的股票代码

    参数:
        stock_codes (list): 股票代码列表
        open_prices (list): 开盘价列表
        close_prices (list): 收盘价列表

    返回:
        list: 涨跌幅大于 0 的股票代码列表

    示例:
        >>> codes = ['000001', '000002', '000003']
        >>> opens = [10.0, 20.0, 15.0]
        >>> closes = [10.5, 19.5, 15.3]
        >>> analyze_stock_data(codes, opens, closes)
        ['000001', '000003']
    """
    # 在这里写你的代码
    # 步骤：
    # 1. 创建 DataFrame
    # 2. 计算涨跌幅列
    # 3. 筛选涨跌幅 > 0 的行
    # 4. 返回股票代码列表
    pass
