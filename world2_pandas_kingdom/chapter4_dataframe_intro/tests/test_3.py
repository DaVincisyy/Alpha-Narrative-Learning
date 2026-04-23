"""
练习 3 测试：选择单列
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_3 import select_column
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 3: 选择单列\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003'],
            '价格': [10.5, 20.3, 15.8],
            '涨跌幅': [0.05, -0.02, 0.03]
        })

        # 测试选择股票代码列
        result1 = select_column(df, '股票代码')
        runner.test(
            "选择股票代码列",
            list(result1) == ['000001', '000002', '000003'],
            f"期望 ['000001', '000002', '000003']，实际 {list(result1)}"
        )

        # 测试选择价格列
        result2 = select_column(df, '价格')
        runner.test(
            "选择价格列",
            list(result2) == [10.5, 20.3, 15.8],
            f"期望 [10.5, 20.3, 15.8]，实际 {list(result2)}"
        )

        # 测试返回类型
        runner.test(
            "返回 Series 类型",
            isinstance(result1, pd.Series),
            f"期望返回 Series，实际返回 {type(result1)}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
