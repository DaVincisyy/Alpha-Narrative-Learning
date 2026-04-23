"""
练习 5：选择行

任务：使用 iloc 选择指定位置的行
要求：返回指定索引位置的行数据
"""

import pandas as pd


def select_row_by_position(df, position):
    """
    通过位置索引选择行

    参数:
        df (DataFrame): 输入的 DataFrame
        position (int): 行的位置索引（从 0 开始）

    返回:
        Series: 指定位置的行数据

    示例:
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        >>> result = select_row_by_position(df, 0)
        >>> result['A']
        1
    """
    # 在这里写你的代码
    # 提示：使用 df.iloc[position]
    pass
