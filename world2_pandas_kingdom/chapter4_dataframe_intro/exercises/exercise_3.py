"""
练习 3：选择单列

任务：从 DataFrame 中选择指定的列
要求：返回指定列名的数据（Series）
"""

import pandas as pd


def select_column(df, column_name):
    """
    选择 DataFrame 中的单列

    参数:
        df (DataFrame): 输入的 DataFrame
        column_name (str): 要选择的列名

    返回:
        Series: 指定列的数据

    示例:
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        >>> result = select_column(df, 'A')
        >>> list(result)
        [1, 2, 3]
    """
    # 在这里写你的代码
    # 提示：使用 df[column_name]
    pass
