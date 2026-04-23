"""
练习 4 测试：范围筛选
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_4 import filter_by_price_range
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 4: 范围筛选\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003', '000004', '000005'],
            '价格': [10.5, 20.3, 15.8, 8.2, 25.0]
        })

        # 测试范围 [12, 22]
        result1 = filter_by_price_range(df, 12, 22)
        expected1 = ['000002', '000003']
        runner.test(
            "筛选价格在 [12, 22] 范围",
            list(result1['股票代码']) == expected1,
            f"期望 {expected1}，实际 {list(result1['股票代码'])}"
        )

        # 测试范围 [10, 20]
        result2 = filter_by_price_range(df, 10, 20)
        expected2 = ['000001', '000003']
        runner.test(
            "筛选价格在 [10, 20] 范围",
            list(result2['股票代码']) == expected2,
            f"期望 {expected2}，实际 {list(result2['股票代码'])}"
        )

        # 测试范围 [30, 40]（无结果）
        result3 = filter_by_price_range(df, 30, 40)
        runner.test(
            "筛选价格在 [30, 40] 范围（无结果）",
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
