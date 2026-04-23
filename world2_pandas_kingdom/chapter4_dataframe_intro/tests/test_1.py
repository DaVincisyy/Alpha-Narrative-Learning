"""
练习 1 测试：创建 DataFrame
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import create_stock_dataframe
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 1: 创建 DataFrame\n")

    try:
        df = create_stock_dataframe()

        # 测试返回类型
        import pandas as pd
        runner.test(
            "返回 DataFrame 类型",
            isinstance(df, pd.DataFrame),
            f"期望返回 DataFrame，实际返回 {type(df)}"
        )

        # 测试形状
        runner.test(
            "DataFrame 形状正确",
            df.shape == (3, 3),
            f"期望形状 (3, 3)，实际 {df.shape}"
        )

        # 测试列名
        expected_columns = ['股票代码', '价格', '涨跌幅']
        runner.test(
            "列名正确",
            list(df.columns) == expected_columns,
            f"期望列名 {expected_columns}，实际 {list(df.columns)}"
        )

        # 测试股票代码列
        expected_codes = ['000001', '000002', '000003']
        runner.test(
            "股票代码列数据正确",
            list(df['股票代码']) == expected_codes,
            f"期望 {expected_codes}，实际 {list(df['股票代码'])}"
        )

        # 测试价格列
        expected_prices = [10.5, 20.3, 15.8]
        runner.test(
            "价格列数据正确",
            list(df['价格']) == expected_prices,
            f"期望 {expected_prices}，实际 {list(df['价格'])}"
        )

        # 测试涨跌幅列
        expected_changes = [0.05, -0.02, 0.03]
        runner.test(
            "涨跌幅列数据正确",
            list(df['涨跌幅']) == expected_changes,
            f"期望 {expected_changes}，实际 {list(df['涨跌幅'])}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
