"""
练习 6 测试：列表筛选（isin）
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_6 import filter_by_stock_list
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 6: 列表筛选（isin）\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003', '000004', '000005'],
            '价格': [10.5, 20.3, 15.8, 8.2, 25.0]
        })

        # 测试筛选两个股票
        result1 = filter_by_stock_list(df, ['000001', '000003'])
        expected1 = ['000001', '000003']
        runner.test(
            "筛选 ['000001', '000003']",
            list(result1['股票代码']) == expected1,
            f"期望 {expected1}，实际 {list(result1['股票代码'])}"
        )

        # 测试筛选三个股票
        result2 = filter_by_stock_list(df, ['000002', '000004', '000005'])
        expected2 = ['000002', '000004', '000005']
        runner.test(
            "筛选 ['000002', '000004', '000005']",
            list(result2['股票代码']) == expected2,
            f"期望 {expected2}，实际 {list(result2['股票代码'])}"
        )

        # 测试筛选不存在的股票
        result3 = filter_by_stock_list(df, ['999999'])
        runner.test(
            "筛选不存在的股票（无结果）",
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
