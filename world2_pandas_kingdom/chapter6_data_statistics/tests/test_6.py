"""练习 6 测试"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd
from exercises.exercise_6 import group_by_multiple_columns

def run_test():
    runner = TestRunner()
    print("测试练习 6: 多列分组\n")
    try:
        df = pd.DataFrame({'日期': ['2024-01-01', '2024-01-01'], '股票代码': ['A', 'B'], '价格': [10, 20]})
        result = group_by_multiple_columns(df, ['日期', '股票代码'], '价格')
        runner.test("分组正确", result[('2024-01-01', 'A')] == 10.0, "期望 10.0")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)
