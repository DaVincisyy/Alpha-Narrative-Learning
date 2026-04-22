"""
测试练习 4：读取 CSV 文件
"""

import os
import sys
import csv
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_4 import read_stocks_csv
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='', encoding='utf-8') as f:
        temp_file = f.name
        writer = csv.DictWriter(f, fieldnames=['code', 'name', 'price'])
        writer.writeheader()
        writer.writerow({'code': 'AAPL', 'name': 'Apple', 'price': '150.25'})
        writer.writerow({'code': 'GOOGL', 'name': 'Google', 'price': '2800.50'})

    try:
        stocks = read_stocks_csv(temp_file)

        runner.test(
            "应该返回列表",
            isinstance(stocks, list),
            f"实际返回 {type(stocks)}"
        )
        runner.test(
            "应该有 2 条数据",
            len(stocks) == 2,
            f"实际 {len(stocks)} 条"
        )
        runner.test(
            "第一条数据的 code 应该是 'AAPL'",
            stocks[0]['code'] == 'AAPL'
        )
        runner.test(
            "第二条数据的 name 应该是 'Google'",
            stocks[1]['name'] == 'Google'
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
