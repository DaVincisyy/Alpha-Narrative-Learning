"""
练习 5 测试：选择行
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_5 import select_row_by_position
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 5: 选择行\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003'],
            '价格': [10.5, 20.3, 15.8],
            '涨跌幅': [0.05, -0.02, 0.03]
        })

        # 测试选择第一行
        result1 = select_row_by_position(df, 0)
        runner.test(
            "选择第一行",
            result1['股票代码'] == '000001' and result1['价格'] == 10.5,
            f"期望股票代码='000001', 价格=10.5，实际股票代码='{result1['股票代码']}', 价格={result1['价格']}"
        )

        # 测试选择第二行
        result2 = select_row_by_position(df, 1)
        runner.test(
            "选择第二行",
            result2['股票代码'] == '000002' and result2['价格'] == 20.3,
            f"期望股票代码='000002', 价格=20.3，实际股票代码='{result2['股票代码']}', 价格={result2['价格']}"
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
