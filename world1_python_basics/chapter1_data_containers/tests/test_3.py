"""
练习 3 测试：获取第 3 个元素
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_3 import get_third_element
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 3: 获取第 3 个元素\n")

    try:
        test_list = [10, 20, 30, 40, 50]
        result = get_third_element(test_list)
        runner.test(
            "正确获取第 3 个元素（索引 2）",
            result == 30,
            f"期望 30，实际是 {result}。提示：索引从 0 开始！"
        )

        test_list2 = ["a", "b", "c", "d"]
        result2 = get_third_element(test_list2)
        runner.test(
            "对字符串列表也能正确工作",
            result2 == "c",
            f"期望 'c'，实际是 {result2}"
        )
    except Exception as e:
        runner.test("get_third_element 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
