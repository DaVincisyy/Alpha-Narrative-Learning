"""
练习 8 测试：计算列表长度
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_8 import count_stocks
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 8: 计算列表长度\n")

    try:
        test_list = ["AAPL", "GOOGL", "MSFT"]
        result = count_stocks(test_list)
        runner.test(
            "正确计算列表长度",
            result == 3,
            f"期望 3，实际是 {result}"
        )

        empty_list = []
        result2 = count_stocks(empty_list)
        runner.test(
            "空列表返回 0",
            result2 == 0,
            f"期望 0，实际是 {result2}"
        )
    except Exception as e:
        runner.test("count_stocks 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
