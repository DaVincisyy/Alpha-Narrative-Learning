"""
测试练习 2：计算列表中所有数字的总和
"""

import sys
from pathlib import Path

# 添加 exercises 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from exercise_2 import calculate_total
from test_base import TestRunner


def run_tests():
    runner = TestRunner()
    print("测试练习 2: 计算总和\n")

    try:
        result = calculate_total([10, 20, 30])
        runner.test("正确计算总和", result == 60, f"期望 60，实际 {result}")
        result2 = calculate_total([1.5, 2.5, 3.0])
        runner.test("支持小数", result2 == 7.0, f"期望 7.0，实际 {result2}")
    except Exception as e:
        runner.test("calculate_total 运行成功", False, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
