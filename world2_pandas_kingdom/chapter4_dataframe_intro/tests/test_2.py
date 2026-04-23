"""
练习 2 测试：查看 DataFrame 信息
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_2 import get_dataframe_shape
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 2: 查看 DataFrame 信息\n")

    try:
        # 测试用例 1：3x2 DataFrame
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result1 = get_dataframe_shape(df1)
        runner.test(
            "测试 3x2 DataFrame",
            result1 == (3, 2),
            f"期望 (3, 2)，实际 {result1}"
        )

        # 测试用例 2：5x4 DataFrame
        df2 = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [6, 7, 8, 9, 10],
            'C': [11, 12, 13, 14, 15],
            'D': [16, 17, 18, 19, 20]
        })
        result2 = get_dataframe_shape(df2)
        runner.test(
            "测试 5x4 DataFrame",
            result2 == (5, 4),
            f"期望 (5, 4)，实际 {result2}"
        )

        # 测试用例 3：1x1 DataFrame
        df3 = pd.DataFrame({'X': [100]})
        result3 = get_dataframe_shape(df3)
        runner.test(
            "测试 1x1 DataFrame",
            result3 == (1, 1),
            f"期望 (1, 1)，实际 {result3}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
