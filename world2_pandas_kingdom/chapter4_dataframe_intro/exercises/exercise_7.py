"""
练习 7：添加新列

任务：向 DataFrame 添加新列
要求：根据现有列计算新列的值
"""

import pandas as pd


def add_total_value_column(df):
    """
    添加总价值列（价格 * 成交量）

    参数:
        df (DataFrame): 包含 '价格' 和 '成交量' 列的 DataFrame

    返回:
        DataFrame: 添加了 '总价值' 列的 DataFrame

    示例:
        >>> df = pd.DataFrame({'价格': [10, 20], '成交量': [100, 200]})
        >>> result = add_total_value_column(df)
        >>> list(result['总价值'])
        [1000, 4000]
    """
    # 在这里写你的代码
    # 提示：df['总价值'] = df['价格'] * df['成交量']
    # 注意：要返回修改后的 DataFrame
    pass
