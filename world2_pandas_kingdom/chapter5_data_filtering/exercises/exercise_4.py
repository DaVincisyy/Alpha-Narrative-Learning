"""
练习 4：范围筛选

任务：筛选在指定范围内的数据
要求：返回价格在 [min_price, max_price] 范围内的股票
"""

import pandas as pd


def filter_by_price_range(df, min_price, max_price):
    """
    筛选价格在指定范围内的股票

    参数:
        df (DataFrame): 包含 '价格' 列的 DataFrame
        min_price (float): 最小价格
        max_price (float): 最大价格

    返回:
        DataFrame: 价格在范围内的行

    示例:
        >>> df = pd.DataFrame({
        ...     '股票代码': ['A', 'B', 'C', 'D'],
        ...     '价格': [10, 20, 15, 25]
        ... })
        >>> result = filter_by_price_range(df, 12, 22)
        >>> list(result['股票代码'])
        ['B', 'C']
    """
    # 在这里写你的代码
    # 提示：使用 df['价格'].between(min_price, max_price)
    # 或者 (df['价格'] >= min_price) & (df['价格'] <= max_price)
    pass
