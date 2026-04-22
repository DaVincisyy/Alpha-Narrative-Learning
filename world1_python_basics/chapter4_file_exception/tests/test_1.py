"""
测试练习 1：写入文本文件
"""

import os
import sys
import tempfile

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_1 import write_stock_codes
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_file = f.name

    try:
        codes = ['AAPL', 'GOOGL', 'MSFT']
        write_stock_codes(codes, temp_file)

        with open(temp_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        runner.test(
            "应该写入 3 行",
            len(lines) == 3,
            f"实际 {len(lines)} 行"
        )
        runner.test(
            "第一行应该是 'AAPL'",
            lines[0].strip() == 'AAPL',
            f"实际是 '{lines[0].strip()}'"
        )
        runner.test(
            "第二行应该是 'GOOGL'",
            lines[1].strip() == 'GOOGL',
            f"实际是 '{lines[1].strip()}'"
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
