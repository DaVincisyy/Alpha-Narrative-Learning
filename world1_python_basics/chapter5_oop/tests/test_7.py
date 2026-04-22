"""
练习 7 测试：实现迭代器
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import Stock
from exercises.exercise_7 import StockList
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 7: 实现迭代器\n")

    try:
        stock_list = StockList()
        stock1 = Stock('AAPL', 'Apple', 150.25, 100)
        stock2 = Stock('GOOGL', 'Google', 2800.50, 20)

        stock_list.add(stock1)
        stock_list.add(stock2)

        # 测试 __len__
        runner.test(
            "__len__() 方法正确",
            len(stock_list) == 2,
            f"应该有 2 只股票，实际 {len(stock_list)} 只"
        )

        # 测试 __getitem__
        runner.test(
            "__getitem__() 方法正确（索引 0）",
            stock_list[0].code == 'AAPL',
            f"索引 0 应该是 AAPL，实际是 {stock_list[0].code}"
        )
        runner.test(
            "__getitem__() 方法正确（索引 1）",
            stock_list[1].code == 'GOOGL',
            f"索引 1 应该是 GOOGL，实际是 {stock_list[1].code}"
        )

        # 测试迭代
        codes = [stock.code for stock in stock_list]
        runner.test(
            "__iter__() 方法正确",
            codes == ['AAPL', 'GOOGL'],
            f"迭代结果不正确: {codes}"
        )

    except Exception as e:
        runner.test("StockList 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
