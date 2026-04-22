"""
练习 6 测试：类方法和静态方法
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_6 import StockValidator
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 6: 类方法和静态方法\n")

    try:
        # 测试静态方法
        runner.test(
            "is_valid_code() 静态方法正确（有效代码）",
            StockValidator.is_valid_code('AAPL') == True,
            "'AAPL' 应该是有效代码"
        )
        runner.test(
            "is_valid_code() 静态方法正确（小写）",
            StockValidator.is_valid_code('apple') == False,
            "'apple' 不应该是有效代码"
        )
        runner.test(
            "is_valid_code() 静态方法正确（太长）",
            StockValidator.is_valid_code('TOOLONG') == False,
            "'TOOLONG' 太长"
        )
        runner.test(
            "is_valid_code() 静态方法正确（空字符串）",
            StockValidator.is_valid_code('') == False,
            "空字符串不应该有效"
        )

        # 测试类方法
        runner.test(
            "is_valid_market() 类方法正确（NASDAQ）",
            StockValidator.is_valid_market('NASDAQ') == True,
            "'NASDAQ' 应该有效"
        )
        runner.test(
            "is_valid_market() 类方法正确（NYSE）",
            StockValidator.is_valid_market('NYSE') == True,
            "'NYSE' 应该有效"
        )
        runner.test(
            "is_valid_market() 类方法正确（无效市场）",
            StockValidator.is_valid_market('INVALID') == False,
            "'INVALID' 不应该有效"
        )

        # 测试实例方法
        validator1 = StockValidator('AAPL', 'NASDAQ')
        runner.test(
            "validate() 实例方法正确（都有效）",
            validator1.validate() == True,
            "AAPL + NASDAQ 应该有效"
        )

        validator2 = StockValidator('invalid', 'NASDAQ')
        runner.test(
            "validate() 实例方法正确（代码无效）",
            validator2.validate() == False,
            "invalid + NASDAQ 不应该有效"
        )

        validator3 = StockValidator('AAPL', 'INVALID')
        runner.test(
            "validate() 实例方法正确（市场无效）",
            validator3.validate() == False,
            "AAPL + INVALID 不应该有效"
        )

    except Exception as e:
        runner.test("StockValidator 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
