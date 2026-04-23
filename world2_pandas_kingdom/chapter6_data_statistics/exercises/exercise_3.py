"""练习 3：分组统计"""
import pandas as pd

def group_by_mean(df, group_column, value_column):
    """按指定列分组，计算另一列的平均值

    参数:
        df (DataFrame): 输入的 DataFrame
        group_column (str): 分组列名
        value_column (str): 要计算平均值的列名

    返回:
        Series: 分组后的平均值

    示例:
        >>> df = pd.DataFrame({
        ...     '股票代码': ['A', 'A', 'B', 'B'],
        ...     '价格': [10, 20, 15, 25]
        ... })
        >>> result = group_by_mean(df, '股票代码', '价格')
        >>> result['A']
        15.0
    """
    pass
