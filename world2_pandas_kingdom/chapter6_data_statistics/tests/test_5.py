"""练习 5 测试"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd
from exercises.exercise_5 import count_by_group

def run_test():
    runner = TestRunner()
    print("测试练习 5: 计数统计\n")
    try:
        df = pd.DataFrame({'股票代码': ['A', 'A', 'B', 'C', 'A']})
        result = count_by_group(df, '股票代码')
        runner.test("A出现3次", result['A'] == 3, f"期望 3")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)
