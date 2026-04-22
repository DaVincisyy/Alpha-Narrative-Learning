"""
练习 2 测试：创建公司信息字典
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_2 import create_company_dict
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 2: 创建公司信息字典\n")

    try:
        result = create_company_dict()
        runner.test(
            "返回类型是字典",
            isinstance(result, dict),
            f"期望返回 dict，实际返回 {type(result)}"
        )
        runner.test(
            "包含 'name' 键",
            "name" in result,
            "字典中没有 'name' 键"
        )
        runner.test(
            "name 的值是 'Apple Inc.'",
            result.get("name") == "Apple Inc.",
            f"期望 'Apple Inc.'，实际是 {result.get('name')}"
        )
        runner.test(
            "包含 'ticker' 键且值为 'AAPL'",
            result.get("ticker") == "AAPL",
            f"期望 'AAPL'，实际是 {result.get('ticker')}"
        )
        runner.test(
            "包含 'price' 键且值为 150.25",
            result.get("price") == 150.25,
            f"期望 150.25，实际是 {result.get('price')}"
        )
        runner.test(
            "包含 'industry' 键且值为 'Technology'",
            result.get("industry") == "Technology",
            f"期望 'Technology'，实际是 {result.get('industry')}"
        )
    except Exception as e:
        runner.test("create_company_dict 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
