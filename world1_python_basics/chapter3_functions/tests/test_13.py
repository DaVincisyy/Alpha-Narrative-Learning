"""
练习 13 测试：按价格排序
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_13 import sort_by_price
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 13: 按价格排序\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 150},
            {'code': 'GOOGL', 'price': 2800},
            {'code': 'MSFT', 'price': 300}
        ]

        # 测试升序
        sorted_asc = sort_by_price(stocks)
        runner.test(
            "升序第一个正确",
            sorted_asc[0]['code'] == 'AAPL',
            f"升序第一个应该是 AAPL，实际是 {sorted_asc[0]['code']}"
        )
        runner.test(
            "升序最后一个正确",
            sorted_asc[-1]['code'] == 'GOOGL',
            f"升序最后一个应该是 GOOGL，实际是 {sorted_asc[-1]['code']}"
        )

        # 测试降序
        sorted_desc = sort_by_price(stocks, reverse=True)
        runner.test(
            "降序第一个正确",
            sorted_desc[0]['code'] == 'GOOGL',
            f"降序第一个应该是 GOOGL，实际是 {sorted_desc[0]['code']}"
        )
        runner.test(
            "降序最后一个正确",
            sorted_desc[-1]['code'] == 'AAPL',
            f"降序最后一个应该是 AAPL，实际是 {sorted_desc[-1]['code']}"
        )

        # 确保原列表未被修改
        runner.test(
            "原列表未被修改",
            stocks[0]['code'] == 'AAPL',
            f"原列表第一个应该仍是 AAPL，实际是 {stocks[0]['code']}"
        )
    except Exception as e:
        runner.test("sort_by_price 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
