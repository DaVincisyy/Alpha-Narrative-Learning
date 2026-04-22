"""
练习 9 测试：计算平均价格
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_9 import calculate_average_price
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 9: 计算平均价格\n")

    try:
        stocks = [
            {'code': 'AAPL', 'price': 100},
            {'code': 'GOOGL', 'price': 200},
            {'code': 'MSFT', 'price': 300}
        ]

        avg = calculate_average_price(stocks)
        runner.test(
            "平均价格计算正确",
            avg == 200.0,
            f"平均价格应该是 200.0，实际是 {avg}"
        )

        # 测试空列表
        avg_empty = calculate_average_price([])
        runner.test(
            "空列表处理正确",
            avg_empty == 0,
            f"空列表应该返回 0，实际返回 {avg_empty}"
        )
    except Exception as e:
        runner.test("calculate_average_price 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
