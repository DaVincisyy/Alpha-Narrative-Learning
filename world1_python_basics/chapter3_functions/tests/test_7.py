"""
练习 7 测试：计算投资组合总价值
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_7 import calculate_portfolio_value
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 7: 计算投资组合总价值\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 150, 'shares': 100},
            {'code': 'GOOGL', 'price': 2800, 'shares': 20}
        ]

        total = calculate_portfolio_value(stocks)
        expected = 150 * 100 + 2800 * 20
        runner.test(
            "总价值计算正确",
            total == expected,
            f"总价值应该是 {expected}，实际是 {total}"
        )
    except Exception as e:
        runner.test("calculate_portfolio_value 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
