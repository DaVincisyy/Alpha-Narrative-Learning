"""
练习 4 测试：选择多列
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_4 import select_columns
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 4: 选择多列\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003'],
            '价格': [10.5, 20.3, 15.8],
            '涨跌幅': [0.05, -0.02, 0.03],
            '成交量': [1000, 2000, 1500]
        })

        # 测试选择两列
        result1 = select_columns(df, ['股票代码', '价格'])
        runner.test(
            "选择股票代码和价格列",
            list(result1.columns) == ['股票代码', '价格'],
            f"期望列名 ['股票代码', '价格']，实际 {list(result1.columns)}"
        )

        # 测试返回类型
        runner.test(
            "返回 DataFrame 类型",
            isinstance(result1, pd.DataFrame),
            f"期望返回 DataFrame，实际返回 {type(result1)}"
        )

        # 测试数据正确性
        runner.test(
            "数据正确",
            result1.shape == (3, 2),
            f"期望形状 (3, 2)，实际 {result1.shape}"
        )

        # 测试选择三列
        result2 = select_columns(df, ['股票代码', '涨跌幅', '成交量'])
        runner.test(
            "选择三列",
            list(result2.columns) == ['股票代码', '涨跌幅', '成交量'],
            f"期望列名 ['股票代码', '涨跌幅', '成交量']，实际 {list(result2.columns)}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
