"""练习 8：综合练习 - 新闻情绪分析"""
import pandas as pd

def analyze_sentiment_by_stock(df):
    """分析每只股票的情绪统计

    参数:
        df (DataFrame): 包含 '股票代码', '情绪分数', '阅读量' 列的 DataFrame

    返回:
        DataFrame: 包含以下列的统计结果
            - 平均情绪: 平均情绪分数
            - 新闻数量: 新闻条数
            - 总阅读量: 阅读量总和

    示例:
        >>> df = pd.DataFrame({
        ...     '股票代码': ['A', 'A', 'B'],
        ...     '情绪分数': [0.8, 0.6, 0.9],
        ...     '阅读量': [1000, 2000, 1500]
        ... })
        >>> result = analyze_sentiment_by_stock(df)
        >>> result.loc['A', '平均情绪']
        0.7
    """
    pass
