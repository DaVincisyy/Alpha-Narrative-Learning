"""
练习 9 测试：组合模式 - 嵌套投资组合
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_1 import Stock
from exercises.exercise_9 import NestedPortfolio
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 9: 组合模式 - 嵌套投资组合\n")

    try:
        # 创建子组合
        tech_portfolio = NestedPortfolio("科技股")
        tech_portfolio.add_item(Stock('AAPL', 'Apple', 150, 100))
        tech_portfolio.add_item(Stock('GOOGL', 'Google', 2800, 20))

        tech_value = tech_portfolio.get_total_value()
        expected_tech = 150 * 100 + 2800 * 20
        runner.test(
            "单层组合计算正确",
            tech_value == expected_tech,
            f"科技股组合价值应该是 {expected_tech}，实际是 {tech_value}"
        )

        # 创建主组合
        main_portfolio = NestedPortfolio("主组合")
        main_portfolio.add_item(tech_portfolio)
        main_portfolio.add_item(Stock('TSLA', 'Tesla', 200, 50))

        main_value = main_portfolio.get_total_value()
        expected_main = expected_tech + 200 * 50
        runner.test(
            "嵌套组合计算正确",
            main_value == expected_main,
            f"主组合价值应该是 {expected_main}，实际是 {main_value}"
        )

    except Exception as e:
        runner.test("NestedPortfolio 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
