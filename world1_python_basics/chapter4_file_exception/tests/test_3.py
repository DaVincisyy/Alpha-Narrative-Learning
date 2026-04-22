"""
测试练习 3：写入 CSV 文件
"""

import os
import sys
import csv
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_3 import write_stocks_csv
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        temp_file = f.name

    try:
        stocks = [
            {'code': 'AAPL', 'name': 'Apple Inc.', 'price': 150.25},
            {'code': 'GOOGL', 'name': 'Alphabet Inc.', 'price': 2800.50}
        ]
        write_stocks_csv(stocks, temp_file)

        with open(temp_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        runner.test(
            "应该有 2 行数据",
            len(rows) == 2,
            f"实际 {len(rows)} 行"
        )
        runner.test(
            "第一行 code 应该是 'AAPL'",
            rows[0]['code'] == 'AAPL'
        )
        runner.test(
            "第一行 name 应该是 'Apple Inc.'",
            rows[0]['name'] == 'Apple Inc.'
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
