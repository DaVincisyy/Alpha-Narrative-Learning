"""
测试练习 5：统计大于阈值的价格数量
"""

import sys
from pathlib import Path

# 添加 exercises 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from exercise_5 import count_high_prices
from test_base import TestRunner


def run_tests():
    runner = TestRunner()
    print("测试练习 5: 计数\n")

    try:
        result = count_high_prices([50, 150, 200, 80], 100)
        runner.test("正确计数", result == 2, f"期望 2，实际 {result}")
    except Exception as e:
        runner.test("count_high_prices 运行成功", False, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
