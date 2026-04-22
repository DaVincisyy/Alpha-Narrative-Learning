"""
练习 2 测试：添加买入和卖出方法
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_2 import TradableStock
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 2: 添加买入和卖出方法\n")

    try:
        stock = TradableStock('AAPL', 'Apple', 150.25, 100)

        # 测试买入
        stock.buy(50)
        runner.test(
            "buy() 方法正确",
            stock.shares == 150,
            f"买入后应该有 150 股，实际 {stock.shares} 股"
        )

        # 测试卖出成功
        result = stock.sell(30)
        runner.test(
            "sell() 方法正确（成功情况）",
            stock.shares == 120 and result == True,
            f"卖出后应该有 120 股且返回 True，实际 {stock.shares} 股，返回 {result}"
        )

        # 测试卖出失败
        result = stock.sell(200)
        runner.test(
            "sell() 方法正确（失败情况）",
            stock.shares == 120 and result == False,
            f"卖出失败时持有数量不应改变且返回 False，实际 {stock.shares} 股，返回 {result}"
        )

    except Exception as e:
        runner.test("TradableStock 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
