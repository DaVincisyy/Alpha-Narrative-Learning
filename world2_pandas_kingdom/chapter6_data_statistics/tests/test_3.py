"""练习 3 测试"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd
from exercises.exercise_3 import group_by_mean

def run_test():
    runner = TestRunner()
    print("测试练习 3: 分组统计\n")
    try:
        df = pd.DataFrame({'股票代码': ['A', 'A', 'B', 'B'], '价格': [10, 20, 15, 25]})
        result = group_by_mean(df, '股票代码', '价格')
        runner.test("A组平均值", result['A'] == 15.0, f"期望 15.0，实际 {result['A']}")
        runner.test("B组平均值", result['B'] == 20.0, f"期望 20.0，实际 {result['B']}")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)
