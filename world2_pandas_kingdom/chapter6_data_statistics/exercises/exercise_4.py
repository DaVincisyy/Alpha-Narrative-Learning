"""练习 4：多指标统计"""
import pandas as pd

def group_by_multiple_stats(df, group_column, value_column):
    """按指定列分组，计算多个统计指标

    参数:
        df (DataFrame): 输入的 DataFrame
        group_column (str): 分组列名
        value_column (str): 要统计的列名

    返回:
        DataFrame: 包含 mean, max, min 的统计结果

    示例:
        >>> df = pd.DataFrame({
        ...     '股票代码': ['A', 'A', 'B'],
        ...     '价格': [10, 20, 15]
        ... })
        >>> result = group_by_multiple_stats(df, '股票代码', '价格')
        >>> result.loc['A', 'mean']
        15.0
    """
    pass
