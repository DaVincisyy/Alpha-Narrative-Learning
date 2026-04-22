# World 2-5 开发模板

> 基于 World 1 标准，为后续 World 开发提供快速参考

## 📋 开发检查清单

开始开发新 World 前，确保：

- [ ] 阅读 `WORLD1_STANDARD.md`
- [ ] 了解目录结构要求
- [ ] 准备好 `test_base.py`（可复制 World 1 的）
- [ ] 确定章节数量和练习数量
- [ ] 设计好题目（LeetCode 风格）

## 🎯 题目设计原则（重要！）

### ✅ 好的题目设计

```python
"""
练习 N：过滤大于阈值的数字

任务：返回列表中所有大于阈值的数字

输入输出示例：
    输入: [10, 50, 30, 80, 20], 40
    输出: [50, 80]
    
    输入: [1, 2, 3], 5
    输出: []
    
    输入: [100, 200], 50
    输出: [100, 200]
"""

def filter_numbers(numbers, threshold):
    """
    过滤大于阈值的数字
    
    参数:
        numbers (list): 数字列表
        threshold (int): 阈值
    
    返回:
        list: 大于阈值的数字列表
    """
    # 在这里写你的代码
    pass
```

**为什么好？**
- ✅ 有明确的输入输出
- ✅ 有多个示例（包含边界情况）
- ✅ 纯函数，容易测试
- ✅ 任务清晰

### ❌ 避免的题目设计

```python
# ❌ 不好：只打印，没有返回值
def print_numbers(numbers):
    for n in numbers:
        print(n)

# ❌ 不好：需要文件操作
def save_to_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

# ❌ 不好：没有输入输出示例
def process_data(data):
    """处理数据"""
    pass
```

## 📁 快速创建结构

### 1. 创建目录

```bash
cd world2_pandas_kingdom
mkdir -p chapter1_name/exercises
mkdir -p chapter1_name/tests
```

### 2. 复制 test_base.py

```bash
cp ../world1_python_basics/chapter1_data_containers/tests/test_base.py chapter1_name/tests/
```

### 3. 创建练习文件

使用模板（见下方）

### 4. 创建测试文件

使用模板（见下方）

## 📝 练习文件模板

```python
"""
练习 N：[标题]

任务：[清晰的任务描述]

输入输出示例：
    输入: [示例输入1]
    输出: [示例输出1]
    解释: [可选的解释]
    
    输入: [示例输入2]
    输出: [示例输出2]
    
    输入: [边界情况]
    输出: [边界输出]
"""


def function_name(param1, param2):
    """
    [函数说明]
    
    参数:
        param1 (type): [说明]
        param2 (type): [说明]
    
    返回:
        type: [说明]
    """
    # 在这里写你的代码
    pass
```

## 🧪 测试文件模板

```python
"""
练习 N 测试：[标题]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_N import function_name
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()
    print("测试练习 N: [标题]\n")

    try:
        # 测试用例 1：基础功能
        result = function_name(input1, input2)
        runner.test(
            "基础功能测试",
            result == expected1,
            f"期望 {expected1}，实际 {result}"
        )

        # 测试用例 2：边界情况
        result2 = function_name(edge_input1, edge_input2)
        runner.test(
            "边界情况测试",
            result2 == expected2,
            f"期望 {expected2}，实际 {result2}"
        )

        # 测试用例 3：特殊情况
        result3 = function_name(special_input1, special_input2)
        runner.test(
            "特殊情况测试",
            result3 == expected3,
            f"期望 {expected3}，实际 {result3}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
```

## 📚 lesson.md 模板

```markdown
# Chapter N - [章节标题]

## 🎯 学习目标

- 目标 1
- 目标 2
- 目标 3

## 📖 知识点

### 1. [知识点1]

[详细讲解]

```python
# 示例代码
```

### 2. [知识点2]

[详细讲解]

## 💡 练习说明

本章共 X 个练习：

1. **练习 1**：[简短描述]
2. **练习 2**：[简短描述]
...

## 🚀 开始练习

```bash
# 测试单个练习
python test.py W.C.1

# 测试整个章节
python test.py W.C
```

## 📚 参考资料

- [相关链接]
```

## 🔄 开发流程

### 1. 规划阶段
- [ ] 确定章节主题
- [ ] 列出知识点
- [ ] 设计练习题目（LeetCode 风格）
- [ ] 准备示例数据

### 2. 创建阶段
- [ ] 创建目录结构
- [ ] 复制 test_base.py
- [ ] 编写 lesson.md
- [ ] 创建所有 exercise_N.py
- [ ] 创建所有 test_N.py

### 3. 测试阶段
- [ ] 运行 `python test.py W.C` 确保测试系统工作
- [ ] 检查所有测试用例
- [ ] 验证错误信息清晰

### 4. 完善阶段
- [ ] 检查文档字符串
- [ ] 确保输入输出示例完整
- [ ] 更新 README.md
- [ ] 更新 QUICK_REFERENCE.md

## 💡 题目设计技巧

### 1. 从简单到复杂

```python
# 练习 1：简单
def sum_list(numbers):
    """返回列表总和"""
    pass

# 练习 2：中等
def sum_even_numbers(numbers):
    """返回列表中偶数的总和"""
    pass

# 练习 3：复杂
def sum_by_condition(numbers, condition):
    """根据条件函数返回符合条件的数字总和"""
    pass
```

### 2. 提供多个示例

```python
"""
输入输出示例：
    输入: [1, 2, 3, 4, 5], 3
    输出: [4, 5]
    解释: 返回所有大于 3 的数字
    
    输入: [10, 20, 30], 50
    输出: []
    解释: 没有数字大于 50
    
    输入: [], 10
    输出: []
    解释: 空列表返回空列表
"""
```

### 3. 贴近实际场景

```python
# ✅ 好：实际场景
def filter_valid_emails(emails):
    """过滤出有效的邮箱地址"""
    pass

# ❌ 不好：抽象场景
def process_strings(strings):
    """处理字符串"""
    pass
```

## 📊 进度追踪

创建 `PROGRESS.md` 记录开发进度：

```markdown
# World 2 开发进度

## Chapter 1 - DataFrame 入门
- [x] lesson.md
- [x] exercise_1.py
- [x] test_1.py
- [ ] exercise_2.py
- [ ] test_2.py
...

## Chapter 2 - 数据筛选
- [ ] lesson.md
- [ ] 练习文件
- [ ] 测试文件
```

## 🎯 质量标准

每个练习必须满足：

- [ ] 有清晰的任务描述
- [ ] 有至少 3 个输入输出示例
- [ ] 有完整的文档字符串
- [ ] 测试有至少 3 个用例
- [ ] 测试有清晰的错误信息
- [ ] 可以用 `python test.py W.C.E` 测试
- [ ] 是纯函数（有输入输出，无副作用）

## 🚀 快速开始

```bash
# 1. 复制模板
cp WORLD_TEMPLATE.md world2_pandas_kingdom/

# 2. 创建第一个章节
cd world2_pandas_kingdom
mkdir -p chapter1_dataframe_intro/{exercises,tests}

# 3. 复制 test_base.py
cp ../world1_python_basics/chapter1_data_containers/tests/test_base.py chapter1_dataframe_intro/tests/

# 4. 开始创建练习
# 使用上面的模板创建 exercise_1.py 和 test_1.py

# 5. 测试
cd ..
python test.py 2.1.1
```

## 📝 注意事项

1. **保持一致性**
   - 所有 World 使用相同的结构
   - 所有练习使用相同的格式
   - 所有测试使用相同的风格

2. **文档完整性**
   - 每个练习都有详细说明
   - 每个示例都有解释
   - 每个测试都有清晰的错误信息

3. **测试覆盖**
   - 基础功能
   - 边界情况
   - 特殊情况

4. **用户体验**
   - 错误信息友好
   - 提示信息有帮助
   - 进度可追踪

---

**参考**: `WORLD1_STANDARD.md`  
**更新日期**: 2026-04-22
