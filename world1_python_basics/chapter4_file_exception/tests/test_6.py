"""
测试练习 6：读取 JSON 文件
"""

import os
import sys
import json
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_6 import load_portfolio_json
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', encoding='utf-8') as f:
        temp_file = f.name
        json.dump({'name': 'Test', 'value': 100}, f)

    try:
        data = load_portfolio_json(temp_file)

        runner.test(
            "应该返回字典",
            isinstance(data, dict),
            f"实际返回 {type(data)}"
        )
        runner.test(
            "name 字段应该正确",
            data['name'] == 'Test'
        )
        runner.test(
            "value 字段应该正确",
            data['value'] == 100
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
