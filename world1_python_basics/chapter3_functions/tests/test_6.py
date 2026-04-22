"""
练习 6 测试：获取股票代码列表
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_6 import get_stock_codes
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 6: 获取股票代码列表\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 150},
            {'code': 'GOOGL', 'price': 2800},
            {'code': 'MSFT', 'price': 300}
        ]

        codes = get_stock_codes(stocks)
        runner.test(
            "提取代码正确",
            codes == ['AAPL', 'GOOGL', 'MSFT'],
            f"代码列表应该是 ['AAPL', 'GOOGL', 'MSFT']，实际是 {codes}"
        )
    except Exception as e:
        runner.test("get_stock_codes 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
