"""
练习 6：列表筛选（isin）

任务：筛选在指定列表中的数据
要求：返回股票代码在给定列表中的所有行
"""

import pandas as pd


def filter_by_stock_list(df, stock_codes):
    """
    筛选股票代码在列表中的行

    参数:
        df (DataFrame): 包含 '股票代码' 列的 DataFrame
        stock_codes (list): 股票代码列表

    返回:
        DataFrame: 股票代码在列表中的行

    示例:
        >>> df = pd.DataFrame({
        ...     '股票代码': ['000001', '000002', '000003', '000004'],
        ...     '价格': [10, 20, 15, 25]
        ... })
        >>> result = filter_by_stock_list(df, ['000001', '000003'])
        >>> list(result['股票代码'])
        ['000001', '000003']
    """
    # 在这里写你的代码
    # 提示：使用 df['股票代码'].isin(stock_codes)
    pass
