"""
练习 12 测试：使用关键字参数创建股票
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_12 import create_stock_flexible
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 12: 使用关键字参数创建股票\n")

    try:
        stock1 = create_stock_flexible(code='AAPL', name='Apple', price=150.25)
        runner.test(
            "code 正确",
            stock1['code'] == 'AAPL',
            f"code 应该是 'AAPL'，实际是 {stock1.get('code')}"
        )
        runner.test(
            "name 正确",
            stock1['name'] == 'Apple',
            f"name 应该是 'Apple'，实际是 {stock1.get('name')}"
        )
        runner.test(
            "price 正确",
            stock1['price'] == 150.25,
            f"price 应该是 150.25，实际是 {stock1.get('price')}"
        )

        stock2 = create_stock_flexible(code='GOOGL', price=2800, sector='Tech', market='NASDAQ')
        runner.test(
            "包含所有键",
            len(stock2) == 4,
            f"应该包含 4 个键，实际有 {len(stock2)} 个"
        )
        runner.test(
            "额外参数正确",
            stock2['sector'] == 'Tech',
            f"sector 应该是 'Tech'，实际是 {stock2.get('sector')}"
        )
    except Exception as e:
        runner.test("create_stock_flexible 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
