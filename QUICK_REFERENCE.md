# 快速参考

## 目录结构
```
world1_python_basics/
  chapter1_data_containers/        (8 个练习)
  chapter2_loops_conditions/       (8 个练习)
  chapter3_functions/              (15 个练习)
  chapter4_file_exception/         (11 个练习)
  chapter5_oop/                    (10 个练习)

每个章节结构：
chapter_name/
├── exercises/          # 你写代码的地方
│   ├── exercise_1.py  # 练习1
│   ├── exercise_2.py  # 练习2
│   └── ...
└── tests/             # 测试文件（不用改）
    ├── test_1.py
    ├── test_2.py
    └── ...
```

## 常用命令

```bash
# 查看所有练习
python test.py --list

# 测试单个练习
python test.py 1.1.1    # world1, chapter1, 练习1
python test.py 1.2.3    # world1, chapter2, 练习3
python test.py 1.3.5    # world1, chapter3, 练习5

# 测试整个章节
python test.py 1.1      # world1, chapter1 所有练习
python test.py 1.2      # world1, chapter2 所有练习

# 测试整个 world
python test.py 1        # world1 所有章节
```

## 工作流程

1. 打开 `exercises/exercise_N.py`
2. 写代码
3. 运行 `python test.py 1.X.N`
4. 看结果：✅ 通过 / ❌ 失败
5. 失败就改代码，重新测试
6. 通过就进入下一个练习

## 示例

```bash
# 1. 查看有什么
python test.py --list

# 2. 编辑练习1
code world1_python_basics/chapter1_data_containers/exercises/exercise_1.py

# 3. 测试练习1
python test.py 1.1.1

# 4. 通过后继续练习2
code world1_python_basics/chapter1_data_containers/exercises/exercise_2.py
python test.py 1.1.2
```

## World 1 练习总览

- **Chapter 1 - 数据容器** (8 个练习)
  - 列表、字典、元组基础操作
  
- **Chapter 2 - 循环与条件** (8 个练习)
  - for 循环、if-elif-else、列表推导式
  
- **Chapter 3 - 函数** (15 个练习)
  - 函数定义、参数、返回值、lambda 表达式
  
- **Chapter 4 - 文件与异常** (11 个练习)
  - 文件读写、CSV/JSON 处理、异常处理

- **Chapter 5 - 面向对象** (10 个练习)
  - 类定义、继承、多态、特殊方法

## 提示

- 每个练习都是独立的文件，互不干扰
- 测试失败会告诉你哪里错了
- 可以随时重新测试，没有限制
- 不用担心改坏其他练习的代码
- 所有练习文件都有详细的注释和示例

## 🌐 网页版

也可以在浏览器中学习：

```bash
# 打开网页版
start web/world1/chapter1.html
```

**💡 提示：**
- 网页版使用简单的字符串检查
- 想要真实的测试结果？在 VSCode 中运行：`python test.py 1.1.1`
- 推荐：网页看题目，VSCode 写代码和测试
