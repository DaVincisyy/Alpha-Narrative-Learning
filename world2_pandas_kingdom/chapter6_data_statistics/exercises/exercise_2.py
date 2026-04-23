"""练习 2：计算最大值和最小值"""
import pandas as pd

def calculate_max_min(df, column_name):
    """计算指定列的最大值和最小值

    参数:
        df (DataFrame): 输入的 DataFrame
        column_name (str): 列名

    返回:
        tuple: (最大值, 最小值)

    示例:
        >>> df = pd.DataFrame({'价格': [10, 20, 30]})
        >>> calculate_max_min(df, '价格')
        (30, 10)
    """
    pass
