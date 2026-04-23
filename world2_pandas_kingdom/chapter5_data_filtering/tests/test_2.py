"""
练习 2 测试：多条件筛选（AND）
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_2 import filter_by_price_and_change
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 2: 多条件筛选（AND）\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003', '000004'],
            '价格': [10.5, 20.3, 15.8, 25.0],
            '涨跌幅': [0.05, -0.02, 0.03, 0.01]
        })

        # 测试阈值 12
        result1 = filter_by_price_and_change(df, 12)
        expected1 = ['000002', '000003', '000004']
        actual1 = list(result1['股票代码'])
        # 只有价格>12且涨跌幅>0的
        expected1_correct = ['000003', '000004']
        runner.test(
            "筛选价格 > 12 且涨跌幅 > 0",
            actual1 == expected1_correct,
            f"期望 {expected1_correct}，实际 {actual1}"
        )

        # 测试阈值 20
        result2 = filter_by_price_and_change(df, 20)
        expected2 = ['000004']
        runner.test(
            "筛选价格 > 20 且涨跌幅 > 0",
            list(result2['股票代码']) == expected2,
            f"期望 {expected2}，实际 {list(result2['股票代码'])}"
        )

        # 测试阈值 30（无结果）
        result3 = filter_by_price_and_change(df, 30)
        runner.test(
            "筛选价格 > 30 且涨跌幅 > 0（无结果）",
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
