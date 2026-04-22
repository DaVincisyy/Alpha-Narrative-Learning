"""
练习 4 测试：计算收益率
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_4 import calculate_return_rate
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 4: 计算收益率\n")

    try:
        rate1 = calculate_return_rate(100, 120)
        runner.test(
            "正收益率计算正确",
            abs(rate1 - 20.0) < 0.01,
            f"收益率应该是 20.0，实际是 {rate1}"
        )

        rate2 = calculate_return_rate(100, 90)
        runner.test(
            "负收益率计算正确",
            abs(rate2 - (-10.0)) < 0.01,
            f"收益率应该是 -10.0，实际是 {rate2}"
        )
    except Exception as e:
        runner.test("calculate_return_rate 运行成功", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
