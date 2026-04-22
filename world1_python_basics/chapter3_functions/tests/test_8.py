"""
练习 8 测试：查找最贵的股票
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_8 import find_most_expensive
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 8: 查找最贵的股票\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 150},
            {'code': 'GOOGL', 'price': 2800},
            {'code': 'MSFT', 'price': 300}
        ]

        most_expensive = find_most_expensive(stocks)
        runner.test(
            "找到最贵股票代码",
            most_expensive['code'] == 'GOOGL',
            f"应该找到 GOOGL，实际是 {most_expensive.get('code') if most_expensive else None}"
        )
        runner.test(
            "最贵股票价格正确",
            most_expensive['price'] == 2800,
            f"价格应该是 2800，实际是 {most_expensive.get('price') if most_expensive else None}"
        )

        # 测试空列表
        result = find_most_expensive([])
        runner.test(
            "空列表处理正确",
            result is None,
            f"空列表应该返回 None，实际返回 {result}"
        )
    except Exception as e:
        runner.test("find_most_expensive 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
