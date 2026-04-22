"""
练习 15 测试：计算加权平均价格
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_15 import calculate_weighted_average
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 15: 计算加权平均价格\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 100, 'shares': 10},
            {'code': 'GOOGL', 'price': 200, 'shares': 5}
        ]

        avg = calculate_weighted_average(stocks)
        expected = (100 * 10 + 200 * 5) / (10 + 5)
        runner.test(
            "加权平均计算正确",
            abs(avg - expected) < 0.01,
            f"加权平均应该是 {expected:.2f}，实际是 {avg:.2f}"
        )

        # 测试总持有数量为 0
        stocks_zero = [
            {'code': 'AAPL', 'price': 100, 'shares': 0},
            {'code': 'GOOGL', 'price': 200, 'shares': 0}
        ]
        avg_zero = calculate_weighted_average(stocks_zero)
        runner.test(
            "边界情况处理正确",
            avg_zero == 0,
            f"总持有数量为 0 时应该返回 0，实际返回 {avg_zero}"
        )
    except Exception as e:
        runner.test("calculate_weighted_average 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
