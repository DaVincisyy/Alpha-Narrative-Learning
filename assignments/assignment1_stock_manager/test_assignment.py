"""
作业 1 测试：股票数据管理器

运行这个文件来测试你的作业完成情况。
"""

import sys
from solution import *


class TestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.total_score = 0
        self.max_score = 100

    def test(self, name, condition, points, error_msg=""):
        if condition:
            self.passed += 1
            self.total_score += points
            print(f"✅ {name} (+{points} 分)")
        else:
            self.failed += 1
            print(f"❌ {name} (0 分)")
            if error_msg:
                print(f"   错误: {error_msg}")

    def summary(self):
        total = self.passed + self.failed
        print("\n" + "=" * 60)
        print(f"测试结果: {self.passed}/{total} 通过")
        print(f"得分: {self.total_score}/{self.max_score}")
        print("=" * 60)

        if self.total_score >= 90:
            grade = "优秀 🌟"
        elif self.total_score >= 80:
            grade = "良好 👍"
        elif self.total_score >= 60:
            grade = "及格 ✓"
        else:
            grade = "需要改进 📚"

        print(f"\n评级: {grade}")

        if self.failed == 0:
            print("\n🎉 完美！所有测试都通过了！")
            print("你已经完成了世界 1 的学习。")
            print("\n下一步：进入世界 2 学习 Pandas")
            print("cd ../../world2_pandas_kingdom/chapter4_dataframe_intro")
        else:
            print("\n💡 提示：检查失败的测试，修改代码后重新运行。")

        return self.failed == 0


def run_tests():
    runner = TestRunner()
    print("=" * 60)
    print("作业 1：股票数据管理器 - 自动测试")
    print("=" * 60)
    print()

    # 测试功能 1: add_stock
    print("【功能 1】添加股票 (20 分)")
    try:
        portfolio = []
        portfolio = add_stock(portfolio, "AAPL", 150.25, 100)

        runner.test(
            "返回类型是列表",
            isinstance(portfolio, list),
            5,
            f"期望 list，实际 {type(portfolio)}"
        )

        runner.test(
            "列表包含 1 个元素",
            len(portfolio) == 1,
            5,
            f"期望 1 个元素，实际 {len(portfolio)} 个"
        )

        if len(portfolio) > 0:
            stock = portfolio[0]
            runner.test(
                "股票字典包含正确的键",
                "ticker" in stock and "price" in stock and "shares" in stock,
                5,
                f"字典应包含 ticker, price, shares，实际包含 {list(stock.keys())}"
            )

            runner.test(
                "股票信息正确",
                stock["ticker"] == "AAPL" and stock["price"] == 150.25 and stock["shares"] == 100,
                5,
                f"期望 AAPL/150.25/100，实际 {stock.get('ticker')}/{stock.get('price')}/{stock.get('shares')}"
            )
    except Exception as e:
        runner.test("add_stock 运行成功", False, 20, str(e))

    print()

    # 测试功能 2: calculate_total_value
    print("【功能 2】计算总价值 (20 分)")
    try:
        portfolio = [
            {"ticker": "AAPL", "price": 150, "shares": 10},
            {"ticker": "GOOGL", "price": 2800, "shares": 5}
        ]
        result = calculate_total_value(portfolio)

        runner.test(
            "正确计算总价值",
            result == 15500.0,
            15,
            f"期望 15500.0，实际 {result}"
        )

        empty_portfolio = []
        result2 = calculate_total_value(empty_portfolio)
        runner.test(
            "空列表返回 0",
            result2 == 0,
            5,
            f"期望 0，实际 {result2}"
        )
    except Exception as e:
        runner.test("calculate_total_value 运行成功", False, 20, str(e))

    print()

    # 测试功能 3: find_most_expensive
    print("【功能 3】查找最贵股票 (20 分)")
    try:
        portfolio = [
            {"ticker": "AAPL", "price": 150},
            {"ticker": "GOOGL", "price": 2800},
            {"ticker": "MSFT", "price": 380}
        ]
        result = find_most_expensive(portfolio)

        runner.test(
            "找到最贵的股票",
            result is not None and result["ticker"] == "GOOGL",
            15,
            f"期望 GOOGL，实际 {result.get('ticker') if result else None}"
        )

        empty_portfolio = []
        result2 = find_most_expensive(empty_portfolio)
        runner.test(
            "空列表返回 None",
            result2 is None,
            5,
            f"期望 None，实际 {result2}"
        )
    except Exception as e:
        runner.test("find_most_expensive 运行成功", False, 20, str(e))

    print()

    # 测试功能 4: filter_high_value_stocks
    print("【功能 4】筛选高价值股票 (20 分)")
    try:
        portfolio = [
            {"ticker": "AAPL", "price": 150, "shares": 100},   # 15000
            {"ticker": "GOOGL", "price": 2800, "shares": 5},   # 14000
            {"ticker": "MSFT", "price": 100, "shares": 50}     # 5000
        ]
        result = filter_high_value_stocks(portfolio, 10000)

        runner.test(
            "返回类型是列表",
            isinstance(result, list),
            5,
            f"期望 list，实际 {type(result)}"
        )

        runner.test(
            "筛选出正确数量的股票",
            len(result) == 2,
            10,
            f"期望 2 只股票，实际 {len(result)} 只"
        )

        tickers = [s["ticker"] for s in result]
        runner.test(
            "筛选出正确的股票",
            "AAPL" in tickers and "GOOGL" in tickers,
            5,
            f"期望包含 AAPL 和 GOOGL，实际 {tickers}"
        )
    except Exception as e:
        runner.test("filter_high_value_stocks 运行成功", False, 20, str(e))

    print()

    # 测试功能 5: generate_report
    print("【功能 5】生成投资报告 (20 分)")
    try:
        portfolio = [
            {"ticker": "AAPL", "price": 150, "shares": 10},
            {"ticker": "GOOGL", "price": 2800, "shares": 5}
        ]
        result = generate_report(portfolio)

        runner.test(
            "返回类型是字典",
            isinstance(result, dict),
            5,
            f"期望 dict，实际 {type(result)}"
        )

        runner.test(
            "包含 total_value 且正确",
            result.get("total_value") == 15500.0,
            5,
            f"期望 15500.0，实际 {result.get('total_value')}"
        )

        runner.test(
            "包含 stock_count 且正确",
            result.get("stock_count") == 2,
            3,
            f"期望 2，实际 {result.get('stock_count')}"
        )

        expected_avg = (150 + 2800) / 2
        runner.test(
            "包含 average_price 且正确",
            abs(result.get("average_price", 0) - expected_avg) < 0.01,
            4,
            f"期望 {expected_avg}，实际 {result.get('average_price')}"
        )

        runner.test(
            "包含 most_expensive_ticker 且正确",
            result.get("most_expensive_ticker") == "GOOGL",
            3,
            f"期望 GOOGL，实际 {result.get('most_expensive_ticker')}"
        )
    except Exception as e:
        runner.test("generate_report 运行成功", False, 20, str(e))

    return runner.summary()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
