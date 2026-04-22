"""
练习 11 测试：使用可变参数计算总和
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_11 import sum_prices
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 11: 使用可变参数计算总和\n")

    try:
        result1 = sum_prices(100, 200, 300)
        runner.test(
            "多个参数计算正确",
            result1 == 600,
            f"应该返回 600，实际返回 {result1}"
        )

        result2 = sum_prices(50.5, 75.25)
        runner.test(
            "浮点数计算正确",
            abs(result2 - 125.75) < 0.01,
            f"应该返回 125.75，实际返回 {result2}"
        )

        result3 = sum_prices(100)
        runner.test(
            "单个参数计算正确",
            result3 == 100,
            f"应该返回 100，实际返回 {result3}"
        )
    except Exception as e:
        runner.test("sum_prices 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
