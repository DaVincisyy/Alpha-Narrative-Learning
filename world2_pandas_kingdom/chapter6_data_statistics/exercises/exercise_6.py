"""练习 6：多列分组"""
import pandas as pd

def group_by_multiple_columns(df, group_columns, value_column):
    """按多列分组统计

    参数:
        df (DataFrame): 输入的 DataFrame
        group_columns (list): 分组列名列表
        value_column (str): 要统计的列名

    返回:
        Series: 分组后的平均值

    示例:
        >>> df = pd.DataFrame({
        ...     '日期': ['2024-01-01', '2024-01-01', '2024-01-02'],
        ...     '股票代码': ['A', 'B', 'A'],
        ...     '价格': [10, 20, 15]
        ... })
        >>> result = group_by_multiple_columns(df, ['日期', '股票代码'], '价格')
        >>> result[('2024-01-01', 'A')]
        10.0
    """
    pass
