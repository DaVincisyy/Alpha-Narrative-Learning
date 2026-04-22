"""
练习 10 测试：格式化股票信息
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_10 import format_stock_info
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 10: 格式化股票信息\n")

    try:
        stock = {'code': 'AAPL', 'name': 'Apple Inc.', 'price': 150.25}
        result = format_stock_info(stock)

        runner.test(
            "包含代码",
            'AAPL' in result,
            f"结果应该包含 'AAPL'，实际是 {result}"
        )
        runner.test(
            "包含名称",
            'Apple Inc.' in result,
            f"结果应该包含 'Apple Inc.'，实际是 {result}"
        )
        runner.test(
            "包含价格",
            '150.25' in result,
            f"结果应该包含 '150.25'，实际是 {result}"
        )
    except Exception as e:
        runner.test("format_stock_info 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
