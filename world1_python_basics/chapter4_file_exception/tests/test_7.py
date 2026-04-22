"""
测试练习 7：安全读取文件（异常处理）
"""

import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_7 import safe_read_file
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    # 测试文件存在的情况
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
        temp_file = f.name
        f.write('Test content')

    try:
        content = safe_read_file(temp_file)
        runner.test(
            "文件存在时应该读取内容",
            content == 'Test content',
            f"实际读取: {content}"
        )

        # 测试文件不存在的情况
        result = safe_read_file('non_existent_file_12345.txt')
        runner.test(
            "文件不存在时应该返回 None",
            result is None,
            f"实际返回: {result}"
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    runner.summary()


if __name__ == '__main__':
    main()
