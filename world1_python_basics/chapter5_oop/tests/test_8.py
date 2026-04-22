"""
练习 8 测试：属性装饰器
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_8 import ManagedStock
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 8: 属性装饰器\n")

    try:
        stock = ManagedStock('AAPL', 150.25)

        # 测试 getter
        runner.test(
            "price getter 正确",
            stock.price == 150.25,
            f"price 应该是 150.25，实际是 {stock.price}"
        )

        # 测试 setter
        stock.price = 155.0
        runner.test(
            "price setter 正确",
            stock.price == 155.0,
            f"设置后 price 应该是 155.0，实际是 {stock.price}"
        )

        # 测试验证
        try:
            stock.price = -10
            runner.test(
                "负数价格抛出 ValueError",
                False,
                "应该抛出 ValueError"
            )
        except ValueError:
            runner.test(
                "负数价格抛出 ValueError",
                True,
                ""
            )

    except Exception as e:
        runner.test("ManagedStock 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
