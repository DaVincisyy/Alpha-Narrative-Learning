"""
练习 7 测试：添加新列
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_7 import add_total_value_column
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 7: 添加新列\n")

    try:
        # 测试用例 1
        df1 = pd.DataFrame({
            '股票代码': ['000001', '000002'],
            '价格': [10.0, 20.0],
            '成交量': [100, 200]
        })
        result1 = add_total_value_column(df1)

        # 测试是否添加了新列
        runner.test(
            "添加了总价值列",
            '总价值' in result1.columns,
            f"期望包含 '总价值' 列，实际列名 {list(result1.columns)}"
        )

        # 测试计算是否正确
        expected_values = [1000.0, 4000.0]
        runner.test(
            "总价值计算正确",
            list(result1['总价值']) == expected_values,
            f"期望 {expected_values}，实际 {list(result1['总价值'])}"
        )

        # 测试用例 2：不同的数据
        df2 = pd.DataFrame({
            '价格': [15.5, 30.2, 25.0],
            '成交量': [1000, 500, 800]
        })
        result2 = add_total_value_column(df2)
        expected_values2 = [15500.0, 15100.0, 20000.0]
        runner.test(
            "不同数据计算正确",
            list(result2['总价值']) == expected_values2,
            f"期望 {expected_values2}，实际 {list(result2['总价值'])}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
