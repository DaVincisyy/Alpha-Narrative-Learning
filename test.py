#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新的测试运行器
支持格式: python test.py 1.1.3 (world.chapter.exercise)
"""

import sys
import os
from pathlib import Path

# 设置Windows控制台编码
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


def find_worlds():
    """查找所有 world 目录"""
    worlds = []
    for item in sorted(Path('.').iterdir()):
        if item.is_dir() and item.name.startswith('world'):
            worlds.append(item)
    return worlds


def find_chapters(world_path):
    """查找指定 world 的所有章节"""
    chapters = []
    for item in sorted(world_path.iterdir()):
        if item.is_dir() and item.name.startswith('chapter'):
            chapters.append(item)
    return chapters


def find_exercises(chapter_path):
    """查找章节的所有练习测试文件"""
    tests_dir = chapter_path / 'tests'
    if not tests_dir.exists():
        return []

    exercises = []
    for item in sorted(tests_dir.iterdir()):
        if item.name.startswith('test_') and item.name.endswith('.py') and item.name != 'test_base.py':
            exercises.append(item)
    return exercises


def run_exercise_test(test_file):
    """运行单个练习测试"""
    original_dir = os.getcwd()
    os.chdir(test_file.parent.parent)

    try:
        # 运行测试文件
        exit_code = os.system(f'python "{test_file.relative_to(test_file.parent.parent)}"')
        return exit_code == 0
    finally:
        os.chdir(original_dir)


def run_chapter_tests(chapter_path):
    """运行章节所有测试"""
    exercises = find_exercises(chapter_path)
    if not exercises:
        print(f"❌ 没有找到测试文件: {chapter_path}")
        return False

    print(f"\n{'='*60}")
    print(f"测试章节: {chapter_path.name}")
    print(f"共 {len(exercises)} 个练习")
    print(f"{'='*60}\n")

    passed = 0
    for ex in exercises:
        if run_exercise_test(ex):
            passed += 1
        print()

    print(f"\n总结: {passed}/{len(exercises)} 个练习通过")
    return passed == len(exercises)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Python学习平台测试运行器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python test.py 1.1.3          # 测试 world1 chapter1 练习3
  python test.py 1.1            # 测试 world1 chapter1 所有练习
  python test.py 1              # 测试 world1 所有章节
  python test.py --list         # 列出所有内容
        """
    )

    parser.add_argument("target", nargs="?", help="测试目标 (格式: world.chapter.exercise)")
    parser.add_argument("--list", "-l", action="store_true", help="列出所有内容")

    args = parser.parse_args()

    worlds = find_worlds()

    if args.list:
        print("\n可用内容:")
        for i, world in enumerate(worlds, 1):
            chapters = find_chapters(world)
            print(f"\n{i}. {world.name} ({len(chapters)} 个章节)")
            for j, chapter in enumerate(chapters, 1):
                exercises = find_exercises(chapter)
                print(f"   {i}.{j}. {chapter.name} ({len(exercises)} 个练习)")
        print()
        return

    if not args.target:
        print("请指定测试目标")
        print("\n示例:")
        print("  python test.py 1.1.3    # 测试 world1 chapter1 练习3")
        print("  python test.py 1.1      # 测试 world1 chapter1")
        print("  python test.py 1        # 测试 world1")
        print("  python test.py --list   # 列出所有内容")
        return

    # 解析目标
    parts = args.target.split('.')

    try:
        world_num = int(parts[0])
        if world_num < 1 or world_num > len(worlds):
            print(f"❌ World 编号无效: {world_num}")
            print(f"可用 world: 1-{len(worlds)}")
            return

        world = worlds[world_num - 1]
        chapters = find_chapters(world)

        if len(parts) == 1:
            # 测试整个 world
            print(f"\n🚀 测试 {world.name} 所有章节...\n")
            for chapter in chapters:
                run_chapter_tests(chapter)
            return

        chapter_num = int(parts[1])
        if chapter_num < 1 or chapter_num > len(chapters):
            print(f"❌ Chapter 编号无效: {chapter_num}")
            print(f"可用 chapter: 1-{len(chapters)}")
            return

        chapter = chapters[chapter_num - 1]
        exercises = find_exercises(chapter)

        if len(parts) == 2:
            # 测试整个 chapter
            run_chapter_tests(chapter)
            return

        exercise_num = int(parts[2])
        if exercise_num < 1 or exercise_num > len(exercises):
            print(f"❌ 练习编号无效: {exercise_num}")
            print(f"可用练习: 1-{len(exercises)}")
            return

        # 测试单个练习
        exercise = exercises[exercise_num - 1]
        print(f"\n{'='*60}")
        print(f"测试: {world.name} / {chapter.name} / 练习 {exercise_num}")
        print(f"{'='*60}\n")
        run_exercise_test(exercise)

    except ValueError:
        print(f"❌ 无效的格式: {args.target}")
        print("使用格式: world.chapter.exercise (如 1.1.3)")
    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
