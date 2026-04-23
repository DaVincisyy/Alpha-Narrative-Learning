"""练习 1-8 测试文件"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd

# Test 1
from exercises.exercise_1 import calculate_mean
def test_1():
    runner = TestRunner()
    print("测试练习 1: 计算平均值\n")
    try:
        df = pd.DataFrame({'价格': [10, 20, 30]})
        result = calculate_mean(df, '价格')
        runner.test("计算平均值", result == 20.0, f"期望 20.0，实际 {result}")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    sys.exit(0 if test_1() else 1)
