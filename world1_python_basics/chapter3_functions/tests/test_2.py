"""
练习 2 测试：创建股票字典
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_2 import create_stock
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 2: 创建股票字典\n")

    try:
        # 测试默认参数
        stock1 = create_stock('AAPL', 'Apple Inc.', 150.25)
        runner.test(
            "code 正确",
            stock1['code'] == 'AAPL',
            f"code 应该是 'AAPL'，实际是 {stock1.get('code')}"
        )
        runner.test(
            "name 正确",
            stock1['name'] == 'Apple Inc.',
            f"name 应该是 'Apple Inc.'，实际是 {stock1.get('name')}"
        )
        runner.test(
            "price 正确",
            stock1['price'] == 150.25,
            f"price 应该是 150.25，实际是 {stock1.get('price')}"
        )
        runner.test(
            "默认 shares 正确",
            stock1['shares'] == 0,
            f"默认 shares 应该是 0，实际是 {stock1.get('shares')}"
        )

        # 测试传递 shares
        stock2 = create_stock('GOOGL', 'Google', 2800.50, 20)
        runner.test(
            "传递的 shares 正确",
            stock2['shares'] == 20,
            f"shares 应该是 20，实际是 {stock2.get('shares')}"
        )
    except Exception as e:
        runner.test("create_stock 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
