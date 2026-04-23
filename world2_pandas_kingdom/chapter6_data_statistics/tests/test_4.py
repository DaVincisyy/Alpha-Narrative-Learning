"""练习 4-8 测试"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
import pandas as pd

# Test 4
from exercises.exercise_4 import group_by_multiple_stats
def test_4():
    runner = TestRunner()
    print("测试练习 4: 多指标统计\n")
    try:
        df = pd.DataFrame({'股票代码': ['A', 'A', 'B'], '价格': [10, 20, 15]})
        result = group_by_multiple_stats(df, '股票代码', '价格')
        runner.test("A组平均值", result.loc['A', 'mean'] == 15.0, f"期望 15.0")
        runner.test("A组最大值", result.loc['A', 'max'] == 20, f"期望 20")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

# Test 5
from exercises.exercise_5 import count_by_group
def test_5():
    runner = TestRunner()
    print("测试练习 5: 计数统计\n")
    try:
        df = pd.DataFrame({'股票代码': ['A', 'A', 'B', 'C', 'A']})
        result = count_by_group(df, '股票代码')
        runner.test("A出现3次", result['A'] == 3, f"期望 3，实际 {result['A']}")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

# Test 6
from exercises.exercise_6 import group_by_multiple_columns
def test_6():
    runner = TestRunner()
    print("测试练习 6: 多列分组\n")
    try:
        df = pd.DataFrame({'日期': ['2024-01-01', '2024-01-01', '2024-01-02'], '股票代码': ['A', 'B', 'A'], '价格': [10, 20, 15]})
        result = group_by_multiple_columns(df, ['日期', '股票代码'], '价格')
        runner.test("分组正确", result[('2024-01-01', 'A')] == 10.0, f"期望 10.0")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

# Test 7
from exercises.exercise_7 import create_pivot_table
def test_7():
    runner = TestRunner()
    print("测试练习 7: 数据透视表\n")
    try:
        df = pd.DataFrame({'日期': ['2024-01-01', '2024-01-01'], '股票代码': ['A', 'B'], '价格': [10, 20]})
        result = create_pivot_table(df, '日期', '股票代码', '价格')
        runner.test("透视表正确", result.loc['2024-01-01', 'A'] == 10.0, f"期望 10.0")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

# Test 8
from exercises.exercise_8 import analyze_sentiment_by_stock
def test_8():
    runner = TestRunner()
    print("测试练习 8: 综合练习\n")
    try:
        df = pd.DataFrame({'股票代码': ['A', 'A', 'B'], '情绪分数': [0.8, 0.6, 0.9], '阅读量': [1000, 2000, 1500]})
        result = analyze_sentiment_by_stock(df)
        runner.test("A平均情绪", result.loc['A', '平均情绪'] == 0.7, f"期望 0.7")
        runner.test("A新闻数量", result.loc['A', '新闻数量'] == 2, f"期望 2")
    except Exception as e:
        runner.test("函数执行", False, str(e))
    return runner.summary()

if __name__ == "__main__":
    test_num = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    tests = {4: test_4, 5: test_5, 6: test_6, 7: test_7, 8: test_8}
    sys.exit(0 if tests[test_num]() else 1)
