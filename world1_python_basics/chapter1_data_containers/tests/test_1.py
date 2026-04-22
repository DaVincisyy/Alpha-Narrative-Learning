"""
练习 1 测试：创建股票列表
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import create_stock_list
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 1: 创建股票列表\n")

    try:
        result = create_stock_list()
        runner.test(
            "返回类型是列表",
            isinstance(result, list),
            f"期望返回 list，实际返回 {type(result)}"
        )
        runner.test(
            "列表包含 5 个元素",
            len(result) == 5,
            f"期望 5 个元素，实际有 {len(result)} 个"
        )
        expected = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
        runner.test(
            "列表内容正确",
            result == expected,
            f"期望 {expected}，实际是 {result}"
        )
    except Exception as e:
        runner.test("create_stock_list 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
