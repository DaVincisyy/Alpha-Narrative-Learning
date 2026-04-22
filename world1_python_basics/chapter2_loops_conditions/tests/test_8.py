"""
测试练习 8：计算投资组合总价值
"""

import sys
from pathlib import Path

# 添加 exercises 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from exercise_8 import calculate_portfolio_value
from test_base import TestRunner


def run_tests():
    runner = TestRunner()
    print("测试练习 8: 计算组合价值\n")

    try:
        portfolio = [
            {"price": 150, "shares": 10},
            {"price": 200, "shares": 5}
        ]
        result = calculate_portfolio_value(portfolio)
        runner.test("正确计算总价值", result == 2500.0, f"期望 2500.0，实际 {result}")
    except Exception as e:
        runner.test("calculate_portfolio_value 运行成功", False, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
