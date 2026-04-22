"""
练习 9：组合模式 - 嵌套投资组合

任务：实现支持嵌套的投资组合
"""

class NestedPortfolio:
    """
    支持嵌套的投资组合

    属性:
        name: 组合名称
        items: 项目列表（可以是 Stock 或 NestedPortfolio）

    方法:
        __init__(name): 初始化
        add_item(item): 添加项目（Stock 或 NestedPortfolio）
        get_total_value(): 递归计算总价值
                           - 如果是 Stock，返回 get_value()
                           - 如果是 NestedPortfolio，递归调用 get_total_value()

    示例:
        tech_portfolio = NestedPortfolio("科技股")
        tech_portfolio.add_item(Stock('AAPL', 'Apple', 150, 100))
        tech_portfolio.add_item(Stock('GOOGL', 'Google', 2800, 20))

        main_portfolio = NestedPortfolio("主组合")
        main_portfolio.add_item(tech_portfolio)
        main_portfolio.add_item(Stock('TSLA', 'Tesla', 200, 50))

        print(main_portfolio.get_total_value())
    """
    pass
