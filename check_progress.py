"""
学习进度追踪器

运行这个文件查看你的学习进度。
"""

import os
import sys


def check_file_exists(path):
    """检查文件是否存在"""
    return os.path.exists(path)


def check_chapter_completion(chapter_path):
    """检查章节是否完成（通过检查 practice.py 是否有内容）"""
    practice_file = os.path.join(chapter_path, "practice.py")
    if not os.path.exists(practice_file):
        return False

    # 简单检查：如果文件中没有 "pass" 关键字，说明可能已完成
    try:
        with open(practice_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # 如果所有函数都实现了，应该没有单独的 pass 语句
            return content.count('pass') < 3  # 允许少量 pass
    except:
        return False


def main():
    print("=" * 60)
    print("📊 学习进度追踪")
    print("=" * 60)
    print()

    base_path = os.path.dirname(os.path.abspath(__file__))

    # 世界 1
    print("🌱 世界 1：Python 基础村")
    chapters = [
        ("chapter1_data_containers", "第 1 章：数据容器"),
        ("chapter2_loops_conditions", "第 2 章：循环与条件"),
        ("chapter3_functions", "第 3 章：函数")
    ]

    world1_completed = 0
    for folder, name in chapters:
        path = os.path.join(base_path, "world1_python_basics", folder)
        if check_chapter_completion(path):
            print(f"  ✅ {name}")
            world1_completed += 1
        else:
            print(f"  ⬜ {name}")

    # 作业 1
    assignment1_path = os.path.join(base_path, "assignments", "assignment1_stock_manager", "solution.py")
    if check_file_exists(assignment1_path):
        try:
            with open(assignment1_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.count('pass') < 2:
                    print(f"  ✅ 作业 1：股票管理器")
                    world1_completed += 1
                else:
                    print(f"  ⬜ 作业 1：股票管理器")
        except:
            print(f"  ⬜ 作业 1：股票管理器")
    else:
        print(f"  ⬜ 作业 1：股票管理器")

    print(f"  进度: {world1_completed}/4")
    print()

    # 世界 2
    print("📊 世界 2：Pandas 数据王国")
    chapters = [
        ("chapter4_dataframe_intro", "第 4 章：DataFrame 入门"),
        ("chapter5_data_filtering", "第 5 章：数据筛选"),
        ("chapter6_data_statistics", "第 6 章：数据统计")
    ]

    world2_completed = 0
    for folder, name in chapters:
        path = os.path.join(base_path, "world2_pandas_kingdom", folder)
        if check_chapter_completion(path):
            print(f"  ✅ {name}")
            world2_completed += 1
        else:
            print(f"  ⬜ {name}")

    print(f"  进度: {world2_completed}/3")
    print()

    # 总进度
    total_chapters = 14  # 5 个世界的所有章节
    completed_estimate = world1_completed + world2_completed

    print("=" * 60)
    print(f"总体进度: {completed_estimate}/{total_chapters} 章节")

    progress_percent = (completed_estimate / total_chapters) * 100
    progress_bar = "█" * int(progress_percent / 5) + "░" * (20 - int(progress_percent / 5))
    print(f"[{progress_bar}] {progress_percent:.1f}%")
    print("=" * 60)
    print()

    # 建议
    if world1_completed == 0:
        print("💡 建议：从世界 1 第 1 章开始学习")
        print("   cd world1_python_basics/chapter1_data_containers")
    elif world1_completed < 4:
        print("💡 建议：继续完成世界 1 的剩余内容")
    elif world2_completed == 0:
        print("💡 建议：开始学习世界 2（Pandas）")
        print("   cd world2_pandas_kingdom/chapter4_dataframe_intro")
    else:
        print("🎉 你正在稳步前进！继续加油！")

    print()


if __name__ == "__main__":
    main()
