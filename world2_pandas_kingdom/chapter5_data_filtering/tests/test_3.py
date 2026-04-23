"""
练习 3 测试：多条件筛选（OR）
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_3 import filter_by_price_or_change
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 3: 多条件筛选（OR）\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003', '000004'],
            '价格': [10.5, 20.3, 15.8, 8.2],
            '涨跌幅': [0.05, -0.02, 0.01, 0.06]
        })

        # 测试：价格 > 18 或 涨跌幅 > 0.04
        result1 = filter_by_price_or_change(df, 18, 0.04)
        expected1 = ['000001', '000002', '000004']
        runner.test(
            "筛选价格 > 18 或涨跌幅 > 0.04",
            list(result1['股票代码']) == expected1,
            f"期望 {expected1}，实际 {list(result1['股票代码'])}"
        )

        # 测试：价格 > 15 或 涨跌幅 > 0.02
        result2 = filter_by_price_or_change(df, 15, 0.02)
        expected2 = ['000001', '000002', '000003', '000004']
        runner.test(
            "筛选价格 > 15 或涨跌幅 > 0.02",
            list(result2['股票代码']) == expected2,
            f"期望 {expected2}，实际 {list(result2['股票代码'])}"
        )

        # 测试：价格 > 25 或 涨跌幅 > 0.1（少量结果）
        result3 = filter_by_price_or_change(df, 25, 0.1)
        runner.test(
            "筛选价格 > 25 或涨跌幅 > 0.1（无结果）",
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
