"""
练习 5 测试：筛选高价股票
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_5 import filter_expensive_stocks
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 5: 筛选高价股票\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 150},
            {'code': 'GOOGL', 'price': 2800},
            {'code': 'MSFT', 'price': 300},
            {'code': 'TSLA', 'price': 200}
        ]

        result = filter_expensive_stocks(stocks, 200)
        runner.test(
            "筛选数量正确",
            len(result) == 2,
            f"应该筛选出 2 只股票，实际 {len(result)} 只"
        )

        codes = [s['code'] for s in result]
        runner.test(
            "筛选结果正确",
            'GOOGL' in codes and 'MSFT' in codes,
            f"应该包含 GOOGL 和 MSFT，实际是 {codes}"
        )
    except Exception as e:
        runner.test("filter_expensive_stocks 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
