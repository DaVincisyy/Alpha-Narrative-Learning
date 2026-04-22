"""
练习 6 测试：添加股票到列表
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_6 import add_stock_to_list
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 6: 添加股票到列表\n")

    try:
        test_list = ["AAPL", "GOOGL"]
        result = add_stock_to_list(test_list, "MSFT")
        runner.test(
            "返回类型是列表",
            isinstance(result, list),
            f"期望返回 list，实际返回 {type(result)}"
        )
        runner.test(
            "列表长度增加了 1",
            len(result) == 3,
            f"期望 3 个元素，实际有 {len(result)} 个"
        )
        runner.test(
            "新元素在列表末尾",
            result[-1] == "MSFT",
            f"期望最后一个元素是 'MSFT'，实际是 {result[-1]}"
        )
    except Exception as e:
        runner.test("add_stock_to_list 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
