"""
练习 5：字符串筛选

任务：筛选包含特定关键词的行
要求：返回标题中包含指定关键词的新闻
"""

import pandas as pd


def filter_by_keyword(df, keyword):
    """
    筛选标题中包含关键词的新闻

    参数:
        df (DataFrame): 包含 '标题' 列的 DataFrame
        keyword (str): 要搜索的关键词

    返回:
        DataFrame: 标题包含关键词的行

    示例:
        >>> df = pd.DataFrame({
        ...     '标题': ['公司业绩大涨', '市场波动', '业绩超预期'],
        ...     '情绪': [0.8, -0.3, 0.9]
        ... })
        >>> result = filter_by_keyword(df, '业绩')
        >>> len(result)
        2
    """
    # 在这里写你的代码
    # 提示：使用 df['标题'].str.contains(keyword)
    pass
