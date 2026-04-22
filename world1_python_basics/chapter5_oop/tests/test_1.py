"""
练习 1 测试：创建基础股票类
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import Stock
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 1: 创建基础股票类\n")

    try:
        apple = Stock('AAPL', 'Apple Inc.', 150.25, 100)

        runner.test(
            "Stock 有 code 属性",
            hasattr(apple, 'code'),
            "Stock 应该有 code 属性"
        )
        runner.test(
            "Stock 有 name 属性",
            hasattr(apple, 'name'),
            "Stock 应该有 name 属性"
        )
        runner.test(
            "Stock 有 price 属性",
            hasattr(apple, 'price'),
            "Stock 应该有 price 属性"
        )
        runner.test(
            "Stock 有 shares 属性",
            hasattr(apple, 'shares'),
            "Stock 应该有 shares 属性"
        )

        runner.test(
            "code 属性正确",
            apple.code == 'AAPL',
            f"期望 'AAPL'，实际 '{apple.code}'"
        )
        runner.test(
            "name 属性正确",
            apple.name == 'Apple Inc.',
            f"期望 'Apple Inc.'，实际 '{apple.name}'"
        )
        runner.test(
            "price 属性正确",
            apple.price == 150.25,
            f"期望 150.25，实际 {apple.price}"
        )
        runner.test(
            "shares 属性正确",
            apple.shares == 100,
            f"期望 100，实际 {apple.shares}"
        )

        value = apple.get_value()
        runner.test(
            "get_value() 方法正确",
            value == 15025.0,
            f"期望 15025.0，实际 {value}"
        )

    except Exception as e:
        runner.test("Stock 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
