"""
练习 6：选择特定单元格

任务：使用 loc 选择特定行和列的值
要求：返回指定行索引和列名的单元格值
"""

import pandas as pd


def get_cell_value(df, row_index, column_name):
    """
    获取特定单元格的值

    参数:
        df (DataFrame): 输入的 DataFrame
        row_index (int): 行索引
        column_name (str): 列名

    返回:
        任意类型: 单元格的值

    示例:
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        >>> get_cell_value(df, 0, 'A')
        1
        >>> get_cell_value(df, 1, 'B')
        5
    """
    # 在这里写你的代码
    # 提示：使用 df.loc[row_index, column_name]
    pass
