"""
练习 6 测试：选择特定单元格
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_6 import get_cell_value
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 6: 选择特定单元格\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003'],
            '价格': [10.5, 20.3, 15.8],
            '涨跌幅': [0.05, -0.02, 0.03]
        })

        # 测试获取第一行的股票代码
        result1 = get_cell_value(df, 0, '股票代码')
        runner.test(
            "获取第一行股票代码",
            result1 == '000001',
            f"期望 '000001'，实际 '{result1}'"
        )

        # 测试获取第二行的价格
        result2 = get_cell_value(df, 1, '价格')
        runner.test(
            "获取第二行价格",
            result2 == 20.3,
            f"期望 20.3，实际 {result2}"
        )

        # 测试获取第三行的涨跌幅
        result3 = get_cell_value(df, 2, '涨跌幅')
        runner.test(
            "获取第三行涨跌幅",
            result3 == 0.03,
            f"期望 0.03，实际 {result3}"
        )

        # 测试获取第一行的涨跌幅
        result4 = get_cell_value(df, 0, '涨跌幅')
        runner.test(
            "获取第一行涨跌幅",
            result4 == 0.05,
            f"期望 0.05，实际 {result4}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
