"""
测试练习 11：追加写入日志
"""

import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_11 import append_to_log
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        temp_file = f.name

    try:
        append_to_log('First message', temp_file)
        append_to_log('Second message', temp_file)

        with open(temp_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        runner.test(
            "应该有 2 行",
            len(lines) == 2,
            f"实际 {len(lines)} 行"
        )
        runner.test(
            "第一行应该包含 'First message'",
            'First message' in lines[0]
        )
        runner.test(
            "第二行应该包含 'Second message'",
            'Second message' in lines[1]
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
