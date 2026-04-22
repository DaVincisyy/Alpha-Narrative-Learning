"""
练习 10 测试：上下文管理器
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import Stock
from exercises.exercise_10 import StockTransaction
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 10: 上下文管理器\n")

    try:
        # 测试正常情况
        stock = Stock('AAPL', 'Apple', 150, 100)
        with StockTransaction(stock):
            stock.shares += 50
        runner.test(
            "正常情况下交易成功",
            stock.shares == 150,
            f"正常情况下应该是 150 股，实际 {stock.shares} 股"
        )

        # 测试异常回滚
        stock = Stock('AAPL', 'Apple', 150, 100)
        try:
            with StockTransaction(stock):
                stock.shares += 50
                raise ValueError("模拟错误")
        except ValueError:
            pass

        runner.test(
            "异常时正确回滚",
            stock.shares == 100,
            f"异常时应该回滚到 100 股，实际 {stock.shares} 股"
        )

    except Exception as e:
        runner.test("StockTransaction 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
