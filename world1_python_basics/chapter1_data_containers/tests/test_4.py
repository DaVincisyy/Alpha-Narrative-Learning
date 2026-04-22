"""
练习 4 测试：更新价格
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_4 import update_price
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 4: 更新价格\n")

    try:
        test_dict = {"name": "Apple", "price": 150.0}
        result = update_price(test_dict, 155.5)
        runner.test(
            "返回类型是字典",
            isinstance(result, dict),
            f"期望返回 dict，实际返回 {type(result)}"
        )
        runner.test(
            "价格已更新",
            result["price"] == 155.5,
            f"期望价格为 155.5，实际是 {result.get('price')}"
        )
        runner.test(
            "其他键值不变",
            result["name"] == "Apple",
            "更新价格时不应该改变其他键值"
        )
    except Exception as e:
        runner.test("update_price 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
