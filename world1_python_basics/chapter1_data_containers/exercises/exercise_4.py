"""
练习 4：更新字典中的价格

任务：更新字典中 price 键的值
"""

def update_price(company_dict, new_price):
    """
    更新字典中的价格
    参数:
        company_dict - 公司信息字典
        new_price - 新的价格
    返回: 更新后的字典
    """
    # 在这里写你的代码
    company_dict["price"] = new_price
    return company_dict
