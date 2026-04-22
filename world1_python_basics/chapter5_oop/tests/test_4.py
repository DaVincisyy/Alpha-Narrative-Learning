"""
练习 4 测试：创建投资组合类
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import Stock
from exercises.exercise_4 import Portfolio
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 4: 创建投资组合类\n")

    try:
        portfolio = Portfolio("测试组合")

        # 测试添加股票
        stock1 = Stock('AAPL', 'Apple', 150.25, 100)
        stock2 = Stock('GOOGL', 'Google', 2800.50, 20)
        portfolio.add_stock(stock1)
        portfolio.add_stock(stock2)

        runner.test(
            "add_stock() 方法正确",
            len(portfolio) == 2,
            f"应该有 2 只股票，实际 {len(portfolio)} 只"
        )

        # 测试重复添加
        stock3 = Stock('AAPL', 'Apple', 150.25, 50)
        portfolio.add_stock(stock3)
        runner.test(
            "重复添加正确合并（数量）",
            len(portfolio) == 2,
            "重复添加应该合并，不增加数量"
        )
        runner.test(
            "重复添加正确合并（持有数）",
            portfolio.stocks['AAPL'].shares == 150,
            f"重复添加应该增加持有数量到 150，实际 {portfolio.stocks['AAPL'].shares}"
        )

        # 测试 __contains__
        runner.test(
            "__contains__() 方法正确（包含）",
            'AAPL' in portfolio,
            "'AAPL' 应该在组合中"
        )
        runner.test(
            "__contains__() 方法正确（不包含）",
            'TSLA' not in portfolio,
            "'TSLA' 不应该在组合中"
        )

        # 测试总价值
        total = portfolio.get_total_value()
        expected = 150.25 * 150 + 2800.50 * 20
        runner.test(
            "get_total_value() 方法正确",
            abs(total - expected) < 0.01,
            f"总价值应该是 {expected}，实际是 {total}"
        )

        # 测试移除
        portfolio.remove_stock('AAPL')
        runner.test(
            "remove_stock() 方法正确（数量）",
            len(portfolio) == 1,
            f"移除后应该只有 1 只股票，实际 {len(portfolio)} 只"
        )
        runner.test(
            "remove_stock() 方法正确（不包含）",
            'AAPL' not in portfolio,
            "'AAPL' 应该已被移除"
        )

    except Exception as e:
        runner.test("Portfolio 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
