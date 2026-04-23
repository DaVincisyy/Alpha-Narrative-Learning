"""
练习 8 测试：综合练习 - 筛选股票新闻
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_8 import filter_quality_news
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 8: 综合练习 - 筛选股票新闻\n")

    try:
        df = pd.DataFrame({
            '标题': [
                '公司业绩大涨',      # ✓ 0.85, 10000, 包含'业绩'
                '市场波动加剧',      # ✗ -0.3
                '增长超预期',        # ✓ 0.9, 8000, 包含'增长'
                '业绩下滑',          # ✗ -0.5
                '新产品发布',        # ✗ 不包含关键词
                '业绩稳定增长',      # ✓ 0.75, 12000, 包含'业绩'和'增长'
                '市场增长放缓'       # ✗ 阅读量不足
            ],
            '情绪分数': [0.85, -0.3, 0.9, -0.5, 0.8, 0.75, 0.8],
            '阅读量': [10000, 3000, 8000, 6000, 4000, 12000, 3000]
        })

        result = filter_quality_news(df)

        # 期望结果：情绪>0.7, 阅读量>5000, 包含'业绩'或'增长'
        expected_titles = ['公司业绩大涨', '增长超预期', '业绩稳定增长']

        runner.test(
            "筛选高质量正面新闻",
            list(result['标题']) == expected_titles,
            f"期望 {expected_titles}，实际 {list(result['标题'])}"
        )

        # 测试结果数量
        runner.test(
            "结果数量正确",
            len(result) == 3,
            f"期望 3 行，实际 {len(result)} 行"
        )

        # 测试所有情绪分数 > 0.7
        runner.test(
            "所有情绪分数 > 0.7",
            all(result['情绪分数'] > 0.7),
            "存在情绪分数 <= 0.7 的行"
        )

        # 测试所有阅读量 > 5000
        runner.test(
            "所有阅读量 > 5000",
            all(result['阅读量'] > 5000),
            "存在阅读量 <= 5000 的行"
        )

        # 测试所有标题包含关键词
        runner.test(
            "所有标题包含 '业绩' 或 '增长'",
            all(result['标题'].str.contains('业绩|增长')),
            "存在不包含关键词的标题"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
