"""
练习 4：选择多列

任务：从 DataFrame 中选择多个列
要求：返回包含指定列的新 DataFrame
"""

import pandas as pd


def select_columns(df, column_names):
    """
    选择 DataFrame 中的多列

    参数:
        df (DataFrame): 输入的 DataFrame
        column_names (list): 要选择的列名列表

    返回:
        DataFrame: 包含指定列的新 DataFrame

    示例:
        >>> df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        >>> result = select_columns(df, ['A', 'C'])
        >>> list(result.columns)
        ['A', 'C']
    """
    # 在这里写你的代码
    # 提示：使用 df[column_names]，注意是双层方括号
    pass
