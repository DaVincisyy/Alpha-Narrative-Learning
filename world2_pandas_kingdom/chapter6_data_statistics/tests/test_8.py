"""练习 8 测试"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd
from exercises.exercise_8 import analyze_sentiment_by_stock

def run_test():
    runner = TestRunner()
    print("测试练习 8: 综合练习\n")
    try:
        df = pd.DataFrame({'股票代码': ['A', 'A', 'B'], '情绪分数': [0.8, 0.6, 0.9], '阅读量': [1000, 2000, 1500]})
        result = analyze_sentiment_by_stock(df)
        runner.test("A平均情绪", result.loc['A', '平均情绪'] == 0.7, "期望 0.7")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)
