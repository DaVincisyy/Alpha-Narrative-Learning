"""练习 2 测试"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd
from exercises.exercise_2 import calculate_max_min

def run_test():
    runner = TestRunner()
    print("测试练习 2: 计算最大值和最小值\n")
    try:
        df = pd.DataFrame({'价格': [10, 20, 30, 5]})
        result = calculate_max_min(df, '价格')
        runner.test("计算最大最小值", result == (30, 5), f"期望 (30, 5)，实际 {result}")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)
