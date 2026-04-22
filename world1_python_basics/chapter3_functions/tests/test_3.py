"""
练习 3 测试：计算利润
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_3 import calculate_profit
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 3: 计算利润\n")

    try:
        # 测试盈利
        profit1 = calculate_profit(100, 120, 50)
        runner.test(
            "盈利计算正确",
            profit1 == 1000.0,
            f"盈利应该是 1000.0，实际是 {profit1}"
        )

        # 测试亏损
        profit2 = calculate_profit(100, 90, 50)
        runner.test(
            "亏损计算正确",
            profit2 == -500.0,
            f"亏损应该是 -500.0，实际是 {profit2}"
        )
    except Exception as e:
        runner.test("calculate_profit 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
