"""练习 7：数据透视表"""
import pandas as pd

def create_pivot_table(df, index_column, columns_column, values_column):
    """创建数据透视表

    参数:
        df (DataFrame): 输入的 DataFrame
        index_column (str): 行索引列名
        columns_column (str): 列索引列名
        values_column (str): 值列名

    返回:
        DataFrame: 透视表

    示例:
        >>> df = pd.DataFrame({
        ...     '日期': ['2024-01-01', '2024-01-01', '2024-01-02'],
        ...     '股票代码': ['A', 'B', 'A'],
        ...     '价格': [10, 20, 15]
        ... })
        >>> result = create_pivot_table(df, '日期', '股票代码', '价格')
        >>> result.loc['2024-01-01', 'A']
        10.0
    """
    pass
