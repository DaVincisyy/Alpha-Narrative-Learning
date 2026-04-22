"""
测试练习 4：根据价格分类
"""

import sys
from pathlib import Path

# 添加 exercises 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from exercise_4 import categorize_price
from test_base import TestRunner


def run_tests():
    runner = TestRunner()
    print("测试练习 4: 价格分类\n")

    try:
        runner.test("高价股", categorize_price(250) == "高价股")
        runner.test("中价股", categorize_price(150) == "中价股")
        runner.test("低价股", categorize_price(50) == "低价股")
    except Exception as e:
        runner.test("categorize_price 运行成功", False, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
