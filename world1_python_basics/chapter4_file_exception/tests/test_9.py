"""
测试练习 9：加载并验证 CSV 数据
"""

import os
import sys
import csv
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_9 import load_and_validate_stocks
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    # 创建包含有效和无效数据的 CSV
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='', encoding='utf-8') as f:
        temp_file = f.name
        writer = csv.DictWriter(f, fieldnames=['code', 'name', 'price'])
        writer.writeheader()
        writer.writerow({'code': 'AAPL', 'name': 'Apple', 'price': '150.25'})
        writer.writerow({'code': 'GOOGL', 'name': 'Google', 'price': 'invalid'})  # 无效价格
        writer.writerow({'code': 'MSFT', 'name': 'Microsoft', 'price': '300.50'})

    try:
        stocks = load_and_validate_stocks(temp_file)

        runner.test(
            "应该返回列表",
            isinstance(stocks, list)
        )
        runner.test(
            "应该有 2 条有效数据",
            len(stocks) == 2,
            f"实际 {len(stocks)} 条"
        )
        runner.test(
            "第一条数据应该是 AAPL",
            stocks[0]['code'] == 'AAPL'
        )
        runner.test(
            "price 应该是 float 类型",
            isinstance(stocks[0]['price'], float)
        )
        runner.test(
            "AAPL 的价格应该是 150.25",
            stocks[0]['price'] == 150.25
        )

        # 测试文件不存在
        result = load_and_validate_stocks('non_existent.csv')
        runner.test(
            "文件不存在时应该返回空列表",
            result == []
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
