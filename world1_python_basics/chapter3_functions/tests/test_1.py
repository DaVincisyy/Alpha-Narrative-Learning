"""
练习 1 测试：计算股票总价值
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import calculate_stock_value
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 1: 计算股票总价值\n")

    try:
        result1 = calculate_stock_value(150.25, 100)
        runner.test(
            "基础计算正确",
            result1 == 15025.0,
            f"应该返回 15025.0，实际返回 {result1}"
        )

        result2 = calculate_stock_value(2800.50, 20)
        runner.test(
            "返回值类型正确",
            result2 == 56010.0,
            f"应该返回 56010.0，实际返回 {result2}"
        )
    except Exception as e:
        runner.test("calculate_stock_value 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
