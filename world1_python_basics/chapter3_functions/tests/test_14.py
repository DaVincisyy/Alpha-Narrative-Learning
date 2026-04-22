"""
练习 14 测试：使用 Lambda 筛选
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_14 import filter_stocks_by_condition
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 14: 使用 Lambda 筛选\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 150},
            {'code': 'GOOGL', 'price': 2800},
            {'code': 'MSFT', 'price': 300}
        ]

        # 测试价格筛选
        result1 = filter_stocks_by_condition(stocks, lambda s: s['price'] > 200)
        runner.test(
            "价格筛选数量正确",
            len(result1) == 2,
            f"应该筛选出 2 只股票，实际 {len(result1)} 只"
        )
        codes1 = [s['code'] for s in result1]
        runner.test(
            "价格筛选结果正确",
            'GOOGL' in codes1 and 'MSFT' in codes1,
            f"应该包含 GOOGL 和 MSFT，实际是 {codes1}"
        )

        # 测试代码筛选
        result2 = filter_stocks_by_condition(stocks, lambda s: s['code'].startswith('A'))
        runner.test(
            "代码筛选数量正确",
            len(result2) == 1,
            f"应该筛选出 1 只股票，实际 {len(result2)} 只"
        )
        runner.test(
            "代码筛选结果正确",
            result2[0]['code'] == 'AAPL',
            f"应该筛选出 AAPL，实际是 {result2[0]['code'] if result2 else None}"
        )
    except Exception as e:
        runner.test("filter_stocks_by_condition 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
