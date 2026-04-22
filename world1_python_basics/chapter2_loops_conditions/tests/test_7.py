"""
测试练习 7：使用列表推导式计算平方
"""

import sys
from pathlib import Path

# 添加 exercises 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from exercise_7 import get_squares
from test_base import TestRunner


def run_tests():
    runner = TestRunner()
    print("测试练习 7: 列表推导式\n")

    try:
        result = get_squares([1, 2, 3, 4])
        runner.test("正确计算平方", result == [1, 4, 9, 16], f"期望 [1, 4, 9, 16]，实际 {result}")
    except Exception as e:
        runner.test("get_squares 运行成功", False, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
