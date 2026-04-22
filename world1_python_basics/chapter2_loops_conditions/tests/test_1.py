"""
测试练习 1：遍历并打印所有股票代码
"""

import sys
import io
from contextlib import redirect_stdout
from pathlib import Path

# 添加 exercises 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from exercise_1 import print_all_stocks
from test_base import TestRunner


def run_tests():
    runner = TestRunner()
    print("测试练习 1: 遍历打印\n")

    try:
        f = io.StringIO()
        with redirect_stdout(f):
            print_all_stocks(["AAPL", "GOOGL"])
        output = f.getvalue()
        runner.test("打印了所有股票", "AAPL" in output and "GOOGL" in output)
    except Exception as e:
        runner.test("print_all_stocks 运行成功", False, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
