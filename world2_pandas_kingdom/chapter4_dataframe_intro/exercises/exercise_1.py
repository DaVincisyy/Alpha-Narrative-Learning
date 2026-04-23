"""
练习 1：创建 DataFrame

任务：从字典创建一个 DataFrame
要求：
1. 创建包含股票代码、价格、涨跌幅的 DataFrame
2. 返回创建的 DataFrame
"""

import pandas as pd


def create_stock_dataframe():
    """
    创建股票数据 DataFrame

    返回:
        DataFrame: 包含以下列的 DataFrame
            - 股票代码: ['000001', '000002', '000003']
            - 价格: [10.5, 20.3, 15.8]
            - 涨跌幅: [0.05, -0.02, 0.03]

    示例:
        >>> df = create_stock_dataframe()
        >>> df.shape
        (3, 3)
        >>> list(df.columns)
        ['股票代码', '价格', '涨跌幅']
    """
    # 在这里写你的代码
    # 提示：使用 pd.DataFrame() 和字典
    pass
