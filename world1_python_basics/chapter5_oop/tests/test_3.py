"""
练习 3 测试：实现魔法方法
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_3 import ComparableStock
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 3: 实现魔法方法\n")

    try:
        apple = ComparableStock('AAPL', 'Apple', 150.25, 100)
        google = ComparableStock('GOOGL', 'Google', 2800.50, 20)
        apple2 = ComparableStock('AAPL', 'Apple Inc.', 155.00, 50)

        # 测试 __str__
        str_result = str(apple)
        runner.test(
            "__str__() 方法正确",
            'AAPL' in str_result and '150.25' in str_result,
            f"__str__() 格式不正确: {str_result}"
        )

        # 测试 __eq__
        runner.test(
            "__eq__() 方法正确（相同代码）",
            apple == apple2,
            "相同代码的股票应该相等"
        )
        runner.test(
            "__eq__() 方法正确（不同代码）",
            not (apple == google),
            "不同代码的股票不应该相等"
        )

        # 测试 __lt__
        runner.test(
            "__lt__() 方法正确（小于）",
            apple < google,
            "AAPL 价格应该小于 GOOGL"
        )
        runner.test(
            "__lt__() 方法正确（不小于）",
            not (google < apple),
            "GOOGL 价格不应该小于 AAPL"
        )

        # 测试 __len__
        runner.test(
            "__len__() 方法正确",
            len(apple) == 100,
            f"len() 应该返回 100，实际返回 {len(apple)}"
        )

    except Exception as e:
        runner.test("ComparableStock 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
