"""
练习 10：批量处理文件
"""

def process_multiple_files(filenames):
    """
    批量读取多个文本文件，返回所有内容

    参数:
        filenames: 文件名列表

    返回:
        字典，键是文件名，值是文件内容
        如果文件不存在，值为 None

    示例:
        result = process_multiple_files(['a.txt', 'b.txt', 'not_exist.txt'])
        # 返回: {'a.txt': '内容A', 'b.txt': '内容B', 'not_exist.txt': None}

    提示:
        - 对每个文件使用 try-except
        - 不要因为一个文件失败而停止处理其他文件
    """
    pass
