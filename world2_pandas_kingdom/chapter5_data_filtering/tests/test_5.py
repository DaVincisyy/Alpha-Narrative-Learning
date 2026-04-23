"""
练习 5 测试：字符串筛选
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_5 import filter_by_keyword
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 5: 字符串筛选\n")

    try:
        df = pd.DataFrame({
            '标题': ['公司业绩大涨', '市场波动加剧', '业绩超预期', '新产品发布', '业绩稳定增长'],
            '情绪': [0.8, -0.3, 0.9, 0.5, 0.7]
        })

        # 测试关键词 '业绩'
        result1 = filter_by_keyword(df, '业绩')
        expected1 = ['公司业绩大涨', '业绩超预期', '业绩稳定增长']
        runner.test(
            "筛选包含 '业绩' 的标题",
            list(result1['标题']) == expected1,
            f"期望 {expected1}，实际 {list(result1['标题'])}"
        )

        # 测试关键词 '市场'
        result2 = filter_by_keyword(df, '市场')
        expected2 = ['市场波动加剧']
        runner.test(
            "筛选包含 '市场' 的标题",
            list(result2['标题']) == expected2,
            f"期望 {expected2}，实际 {list(result2['标题'])}"
        )

        # 测试关键词 '下跌'（无结果）
        result3 = filter_by_keyword(df, '下跌')
        runner.test(
            "筛选包含 '下跌' 的标题（无结果）",
            len(result3) == 0,
            f"期望 0 行，实际 {len(result3)} 行"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
