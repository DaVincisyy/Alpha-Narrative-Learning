"""
练习 3：多条件筛选（OR）

任务：筛选满足任一条件的行
要求：返回价格大于阈值或涨跌幅大于指定值的股票
"""

import pandas as pd


def filter_by_price_or_change(df, price_threshold, change_threshold):
    """
    筛选价格大于价格阈值或涨跌幅大于涨跌幅阈值的股票

    参数:
        df (DataFrame): 包含 '价格' 和 '涨跌幅' 列的 DataFrame
        price_threshold (float): 价格阈值
        change_threshold (float): 涨跌幅阈值

    返回:
        DataFrame: 满足条件的行

    示例:
        >>> df = pd.DataFrame({
        ...     '股票代码': ['A', 'B', 'C'],
        ...     '价格': [10, 20, 15],
        ...     '涨跌幅': [0.05, -0.02, 0.01]
        ... })
        >>> result = filter_by_price_or_change(df, 18, 0.04)
        >>> list(result['股票代码'])
        ['A', 'B']
    """
    # 在这里写你的代码
    # 提示：使用 | 连接条件，每个条件用括号括起来
    pass
