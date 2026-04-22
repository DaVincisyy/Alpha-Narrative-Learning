"""
测试练习 5：写入 JSON 文件
"""

import os
import sys
import json
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_5 import save_portfolio_json
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        temp_file = f.name

    try:
        portfolio = {
            'name': 'My Portfolio',
            'stocks': [{'code': 'AAPL', 'shares': 100}],
            'total_value': 15025.0
        }
        save_portfolio_json(portfolio, temp_file)

        with open(temp_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        runner.test(
            "name 字段应该正确",
            data['name'] == 'My Portfolio'
        )
        runner.test(
            "stocks 列表长度应该正确",
            len(data['stocks']) == 1
        )
        runner.test(
            "total_value 应该正确",
            data['total_value'] == 15025.0
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
