"""
练习 7 测试：复杂条件组合
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_7 import filter_complex_conditions
from tests.test_base import TestRunner
import pandas as pd


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 7: 复杂条件组合\n")

    try:
        df = pd.DataFrame({
            '股票代码': ['000001', '000002', '000003', '000004', '000005'],
            '价格': [15.0, 25.0, 20.0, 35.0, 12.0],
            '涨跌幅': [0.05, 0.03, 0.02, 0.01, 0.04]
        })

        result = filter_complex_conditions(df)

        # 期望结果：价格在[10,30]，涨跌幅>0，股票代码!='000003'
        # 000001: 15, 0.05 ✓
        # 000002: 25, 0.03 ✓
        # 000003: 20, 0.02 ✗ (股票代码是000003)
        # 000004: 35, 0.01 ✗ (价格>30)
        # 000005: 12, 0.04 ✓
        expected = ['000001', '000002', '000005']

        runner.test(
            "复杂条件筛选",
            list(result['股票代码']) == expected,
            f"期望 {expected}，实际 {list(result['股票代码'])}"
        )

        # 测试结果数量
        runner.test(
            "结果数量正确",
            len(result) == 3,
            f"期望 3 行，实际 {len(result)} 行"
        )

        # 测试所有价格在范围内
        runner.test(
            "所有价格在 [10, 30] 范围",
            all((result['价格'] >= 10) & (result['价格'] <= 30)),
            "存在价格不在范围内的行"
        )

        # 测试所有涨跌幅为正
        runner.test(
            "所有涨跌幅 > 0",
            all(result['涨跌幅'] > 0),
            "存在涨跌幅 <= 0 的行"
        )

        # 测试不包含 000003
        runner.test(
            "不包含 000003",
            '000003' not in list(result['股票代码']),
            "结果中包含 000003"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
