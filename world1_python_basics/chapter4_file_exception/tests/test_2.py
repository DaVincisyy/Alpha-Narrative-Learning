"""
测试练习 2：读取文本文件
"""

import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_2 import read_stock_codes
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
        temp_file = f.name
        f.write('AAPL\n')
        f.write('GOOGL\n')
        f.write('MSFT\n')

    try:
        codes = read_stock_codes(temp_file)

        runner.test(
            "应该返回列表",
            isinstance(codes, list),
            f"实际返回 {type(codes)}"
        )
        runner.test(
            "应该有 3 个元素",
            len(codes) == 3,
            f"实际 {len(codes)} 个"
        )
        runner.test(
            "第一个元素应该是 'AAPL'",
            codes[0] == 'AAPL',
            f"实际是 '{codes[0]}'"
        )
        runner.test(
            "第三个元素应该是 'MSFT'",
            codes[2] == 'MSFT',
            f"实际是 '{codes[2]}'"
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
