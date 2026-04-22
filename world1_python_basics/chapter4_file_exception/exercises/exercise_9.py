"""
练习 9：加载并验证 CSV 数据
"""

def load_and_validate_stocks(filename):
    """
    加载 CSV 文件并验证数据，跳过无效行

    参数:
        filename: CSV 文件名

    返回:
        有效的股票列表，每个元素是字典
        字典包含 'code', 'name', 'price'（price 是 float 类型）

    要求:
        - 如果文件不存在，返回空列表
        - 跳过缺少必需字段的行
        - 跳过 price 无法转换为 float 的行
        - 不要让程序崩溃

    提示:
        - 外层 try-except 处理 FileNotFoundError
        - 内层 try-except 处理每行的 KeyError 和 ValueError
    """
    pass
