"""
测试练习 10：批量处理文件
"""

import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_10 import process_multiple_files
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    # 创建两个临时文件
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f1:
        file1 = f1.name
        f1.write('Content A')

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f2:
        file2 = f2.name
        f2.write('Content B')

    try:
        filenames = [file1, file2, 'non_existent.txt']
        result = process_multiple_files(filenames)

        runner.test(
            "应该返回字典",
            isinstance(result, dict)
        )
        runner.test(
            "应该有 3 个键",
            len(result) == 3,
            f"实际 {len(result)} 个"
        )
        runner.test(
            "file1 的内容应该正确",
            result[file1] == 'Content A'
        )
        runner.test(
            "file2 的内容应该正确",
            result[file2] == 'Content B'
        )
        runner.test(
            "不存在的文件应该返回 None",
            result['non_existent.txt'] is None
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))
    finally:
        if os.path.exists(file1):
            os.remove(file1)
        if os.path.exists(file2):
            os.remove(file2)

    runner.summary()


if __name__ == '__main__':
    main()
