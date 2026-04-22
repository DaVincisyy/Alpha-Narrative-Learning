"""
练习 7 测试：获取公司名称
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_7 import get_company_name
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 7: 获取公司名称\n")

    try:
        test_dict = {"name": "Google", "ticker": "GOOGL"}
        result = get_company_name(test_dict)
        runner.test(
            "正确获取 name 值",
            result == "Google",
            f"期望 'Google'，实际是 {result}"
        )
    except Exception as e:
        runner.test("get_company_name 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
