"""
测试练习 6：在字典列表中查找指定股票的价格
"""

import sys
from pathlib import Path

# 添加 exercises 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from exercise_6 import find_stock_price
from test_base import TestRunner


def run_tests():
    runner = TestRunner()
    print("测试练习 6: 查找价格\n")

    try:
        companies = [
            {"ticker": "AAPL", "price": 150.25},
            {"ticker": "GOOGL", "price": 2800.50}
        ]
        result = find_stock_price(companies, "GOOGL")
        runner.test("找到正确价格", result == 2800.50, f"期望 2800.50，实际 {result}")
        result2 = find_stock_price(companies, "TSLA")
        runner.test("找不到返回 None", result2 is None, f"期望 None，实际 {result2}")
    except Exception as e:
        runner.test("find_stock_price 运行成功", False, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
