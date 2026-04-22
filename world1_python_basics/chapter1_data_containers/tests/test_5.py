"""
练习 5 测试：创建元组
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_5 import create_company_tuple
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 5: 创建元组\n")

    try:
        result = create_company_tuple()
        runner.test(
            "返回类型是元组",
            isinstance(result, tuple),
            f"期望返回 tuple，实际返回 {type(result)}"
        )
        runner.test(
            "元组包含 3 个元素",
            len(result) == 3,
            f"期望 3 个元素，实际有 {len(result)} 个"
        )
        expected = ("Apple", 1976, "California")
        runner.test(
            "元组内容正确",
            result == expected,
            f"期望 {expected}，实际是 {result}"
        )
    except Exception as e:
        runner.test("create_company_tuple 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
