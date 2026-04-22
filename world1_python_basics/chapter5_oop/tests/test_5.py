"""
练习 5 测试：继承 - 创建资产基类
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_5 import Asset, StockAsset, BondAsset
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 5: 继承 - 创建资产基类\n")

    try:
        # 测试 Asset 基类
        asset = Asset('Test Asset', 10000)
        runner.test(
            "Asset name 属性正确",
            asset.name == 'Test Asset',
            f"期望 'Test Asset'，实际 '{asset.name}'"
        )
        runner.test(
            "Asset value 属性正确",
            asset.value == 10000,
            f"期望 10000，实际 {asset.value}"
        )
        runner.test(
            "Asset get_value() 方法正确",
            asset.get_value() == 10000,
            f"期望 10000，实际 {asset.get_value()}"
        )

        # 测试 StockAsset
        stock = StockAsset('Apple Inc.', 15025, 'AAPL', 100)
        runner.test(
            "StockAsset 继承自 Asset",
            isinstance(stock, Asset),
            "StockAsset 应该继承自 Asset"
        )
        runner.test(
            "StockAsset code 属性正确",
            stock.code == 'AAPL',
            f"期望 'AAPL'，实际 '{stock.code}'"
        )
        runner.test(
            "StockAsset shares 属性正确",
            stock.shares == 100,
            f"期望 100，实际 {stock.shares}"
        )

        # 测试 BondAsset
        bond = BondAsset('US Treasury', 10000, 0.02)
        runner.test(
            "BondAsset 继承自 Asset",
            isinstance(bond, Asset),
            "BondAsset 应该继承自 Asset"
        )
        runner.test(
            "BondAsset interest_rate 属性正确",
            bond.interest_rate == 0.02,
            f"期望 0.02，实际 {bond.interest_rate}"
        )

        interest = bond.get_annual_interest()
        runner.test(
            "get_annual_interest() 方法正确",
            interest == 200.0,
            f"年利息应该是 200.0，实际是 {interest}"
        )

    except Exception as e:
        runner.test("Asset 类实现", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
