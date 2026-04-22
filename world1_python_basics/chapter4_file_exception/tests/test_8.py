"""
测试练习 8：安全转换价格（异常处理）
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.exercise_8 import safe_convert_price
from tests.test_base import TestRunner


def main():
    runner = TestRunner()

    try:
        # 测试正常转换
        result1 = safe_convert_price('150.25')
        runner.test(
            "正常字符串应该转换成功",
            result1 == 150.25,
            f"应该返回 150.25，实际返回 {result1}"
        )

        # 测试无效字符串
        result2 = safe_convert_price('invalid')
        runner.test(
            "无效字符串应该返回 0.0",
            result2 == 0.0,
            f"实际返回 {result2}"
        )

        # 测试空字符串
        result3 = safe_convert_price('')
        runner.test(
            "空字符串应该返回 0.0",
            result3 == 0.0,
            f"实际返回 {result3}"
        )
    except Exception as e:
        runner.test("函数执行", False, str(e))

    runner.summary()


if __name__ == '__main__':
    main()
