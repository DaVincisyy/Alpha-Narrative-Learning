"""
练习 8 测试：综合练习 - 处理股票数据
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_8 import analyze_stock_data
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 8: 综合练习 - 处理股票数据\n")

    try:
        # 测试用例 1：部分上涨
        codes1 = ['000001', '000002', '000003']
        opens1 = [10.0, 20.0, 15.0]
        closes1 = [10.5, 19.5, 15.3]
        result1 = analyze_stock_data(codes1, opens1, closes1)
        expected1 = ['000001', '000003']
        runner.test(
            "识别上涨股票",
            result1 == expected1,
            f"期望 {expected1}，实际 {result1}"
        )

        # 测试用例 2：全部上涨
        codes2 = ['A', 'B', 'C']
        opens2 = [100, 200, 300]
        closes2 = [110, 220, 330]
        result2 = analyze_stock_data(codes2, opens2, closes2)
        expected2 = ['A', 'B', 'C']
        runner.test(
            "全部上涨情况",
            result2 == expected2,
            f"期望 {expected2}，实际 {result2}"
        )

        # 测试用例 3：全部下跌
        codes3 = ['X', 'Y', 'Z']
        opens3 = [100, 200, 300]
        closes3 = [90, 180, 270]
        result3 = analyze_stock_data(codes3, opens3, closes3)
        expected3 = []
        runner.test(
            "全部下跌情况",
            result3 == expected3,
            f"期望 {expected3}，实际 {result3}"
        )

        # 测试用例 4：包含持平
        codes4 = ['M', 'N', 'O', 'P']
        opens4 = [10, 20, 30, 40]
        closes4 = [11, 20, 29, 42]
        result4 = analyze_stock_data(codes4, opens4, closes4)
        expected4 = ['M', 'P']
        runner.test(
            "包含持平情况",
            result4 == expected4,
            f"期望 {expected4}，实际 {result4}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
