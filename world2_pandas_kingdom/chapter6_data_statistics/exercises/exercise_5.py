"""练习 5：计数统计"""
import pandas as pd

def count_by_group(df, column_name):
    """统计每个值出现的次数

    参数:
        df (DataFrame): 输入的 DataFrame
        column_name (str): 要统计的列名

    返回:
        Series: 每个值的出现次数

    示例:
        >>> df = pd.DataFrame({'股票代码': ['A', 'A', 'B', 'C', 'A']})
        >>> result = count_by_group(df, '股票代码')
        >>> result['A']
        3
    """
    pass
