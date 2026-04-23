"""
练习 1：简单条件筛选

任务：筛选满足条件的行
要求：返回价格大于指定阈值的所有行
"""

import pandas as pd


def filter_by_price(df, threshold):
    """
    筛选价格大于阈值的股票

    参数:
        df (DataFrame): 包含 '价格' 列的 DataFrame
        threshold (float): 价格阈值

    返回:
        DataFrame: 价格大于阈值的行

    示例:
        >>> df = pd.DataFrame({'股票代码': ['A', 'B', 'C'], '价格': [10, 20, 15]})
        >>> result = filter_by_price(df, 12)
        >>> list(result['股票代码'])
        ['B', 'C']
    """
    # 在这里写你的代码
    # 提示：使用 df[df['价格'] > threshold]
    pass
