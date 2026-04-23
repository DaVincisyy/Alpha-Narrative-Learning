"""练习 7 测试"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd
from exercises.exercise_7 import create_pivot_table

def run_test():
    runner = TestRunner()
    print("测试练习 7: 数据透视表\n")
    try:
        df = pd.DataFrame({'日期': ['2024-01-01', '2024-01-01'], '股票代码': ['A', 'B'], '价格': [10, 20]})
        result = create_pivot_table(df, '日期', '股票代码', '价格')
        runner.test("透视表正确", result.loc['2024-01-01', 'A'] == 10.0, "期望 10.0")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)
