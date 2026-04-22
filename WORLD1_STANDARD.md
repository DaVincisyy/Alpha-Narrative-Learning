# World 1 开发标准文档

> 本文档总结了 World 1 的所有开发标准和要求，作为后续 World 2-5 开发的参考模板

## 📁 目录结构标准

```
world1_python_basics/
├── chapter1_data_containers/        (8 个练习)
│   ├── lesson.md                   # 课程讲解
│   ├── exercises/                  # 练习代码目录
│   │   ├── exercise_1.py          # 练习 1
│   │   ├── exercise_2.py          # 练习 2
│   │   └── ...
│   └── tests/                      # 测试代码目录
│       ├── test_base.py           # 共享测试基类
│       ├── test_1.py              # 练习 1 的测试
│       ├── test_2.py              # 练习 2 的测试
│       └── ...
├── chapter2_loops_conditions/       (8 个练习)
├── chapter3_functions/              (15 个练习)
├── chapter4_file_exception/         (11 个练习)
└── chapter5_oop/                    (10 个练习)
```

## 🎯 核心原则

### 1. 一个练习一个文件
- ✅ 每个练习独立成文件
- ✅ 文件命名：`exercise_N.py`
- ✅ 互不干扰，专注单一任务
- ❌ 不要把所有练习放在一个 `practice.py` 里

### 2. 一个练习一个测试
- ✅ 每个测试独立成文件
- ✅ 文件命名：`test_N.py`
- ✅ 从 `exercises.exercise_N` 导入
- ❌ 不要把所有测试放在一个 `test_practice.py` 里

### 3. 统一的测试命令
- ✅ 使用 `python test.py W.C.E` 格式
- ✅ 例如：`python test.py 1.1.1`（world1, chapter1, exercise1）
- ✅ 支持测试单个练习、整个章节、整个 world

## 📝 练习文件格式

### 基本结构

```python
"""
练习 N：练习标题

任务描述：清晰说明要做什么
要求：列出具体要求
"""

def function_name(param1, param2):
    """
    函数说明
    
    参数:
        param1 (type): 参数说明
        param2 (type): 参数说明
    
    返回:
        type: 返回值说明
    
    例子:
        >>> function_name(input1, input2)
        expected_output
    """
    # 在这里写你的代码
    pass
```

### 关键要素

1. **文档字符串**
   - 清晰的任务描述
   - 参数说明
   - 返回值说明
   - 示例（输入输出）

2. **提示注释**
   - 给出思路提示
   - 不直接给答案

3. **初始代码**
   - 函数签名完整
   - 包含 `pass` 占位符

## 🧪 测试文件格式

### 基本结构

```python
"""
练习 N 测试：测试标题
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from exercises.exercise_N import function_name
from tests.test_base import TestRunner


def run_test():
    """运行测试"""
    runner = TestRunner()

    print("测试练习 N: 标题\n")

    try:
        # 测试用例 1
        result = function_name(input1)
        runner.test(
            "测试描述",
            result == expected_output,
            f"期望 {expected_output}，实际 {result}"
        )

        # 测试用例 2
        result2 = function_name(input2)
        runner.test(
            "测试描述 2",
            result2 == expected_output2,
            f"期望 {expected_output2}，实际 {result2}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
```

### 测试原则

1. **多个测试用例**
   - 基础功能测试
   - 边界情况测试
   - 错误处理测试

2. **清晰的错误信息**
   - 说明期望值
   - 说明实际值
   - 给出修改建议

3. **异常处理**
   - 捕获所有异常
   - 显示友好的错误信息

## 🎨 题目设计原则（World 2-5 适用）

### LeetCode 风格

1. **明确的输入输出**
   ```python
   """
   输入: [1, 2, 3, 4, 5], 3
   输出: [4, 5]
   
   解释: 返回所有大于 3 的数字
   """
   ```

2. **避免副作用**
   - ✅ 返回值（容易测试）
   - ❌ 打印输出（难测试）
   - ❌ 修改全局变量（难测试）
   - ❌ 文件操作（需要临时文件）

3. **纯函数优先**
   ```python
   # ✅ 好：纯函数
   def filter_numbers(numbers, threshold):
       return [n for n in numbers if n > threshold]
   
   # ❌ 不好：有副作用
   def print_numbers(numbers):
       for n in numbers:
           print(n)
   ```

4. **提供示例**
   - 至少 2-3 个输入输出示例
   - 包含边界情况
   - 说明特殊情况

## 🔧 测试系统要求

### test.py 功能

1. **支持三级测试**
   - `python test.py 1.1.1` - 单个练习
   - `python test.py 1.1` - 整个章节
   - `python test.py 1` - 整个 world

2. **列出所有内容**
   - `python test.py --list`
   - 显示所有 world/chapter/exercise

3. **清晰的输出**
   - ✅/❌ 标记
   - 详细的错误信息
   - 进度统计

### test_base.py 功能

```python
class TestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.tests = []
    
    def test(self, name, condition, error_msg=""):
        """运行单个测试"""
        pass
    
    def summary(self):
        """打印测试总结"""
        pass
```

## 📚 文档要求

### lesson.md 格式

1. **知识点讲解**
   - 从零开始
   - 配合代码示例
   - 解释底层原理

2. **练习说明**
   - 列出所有练习
   - 说明学习目标

3. **参考资料**
   - 相关链接
   - 扩展阅读

### README.md 内容

1. **项目介绍**
2. **快速开始**
3. **目录结构**
4. **使用方法**
5. **学习路径**

### QUICK_REFERENCE.md 内容

1. **常用命令**
2. **目录结构**
3. **工作流程**
4. **练习总览**

## 🌐 网页版要求

### 功能

1. **练习列表**
   - 显示所有练习
   - 点击切换

2. **代码编辑器**
   - 初始代码
   - 可编辑

3. **测试按钮**
   - 字符串检查（简单）
   - 提示：可以去 VSCode 做真实测试

4. **进度追踪**
   - 进度条
   - 完成标记

### 提示信息

```
💡 提示：
网页版使用简单的字符串检查。
想要真实的测试结果？
在 VSCode 中运行：python test.py 1.1.1
```

## 🚫 避免的问题

### 1. 文件组织
- ❌ 所有练习在一个文件
- ❌ 所有测试在一个文件
- ❌ 混乱的目录结构

### 2. 测试设计
- ❌ 只测试一个用例
- ❌ 错误信息不清晰
- ❌ 没有边界测试

### 3. 题目设计
- ❌ 没有输入输出示例
- ❌ 任务描述不清晰
- ❌ 依赖外部状态

### 4. 文档
- ❌ 文档过时
- ❌ 缺少使用说明
- ❌ 没有快速参考

## 📊 World 1 统计

- **总章节**: 5 章
- **总练习**: 52 个
  - Chapter 1: 8 个（数据容器）
  - Chapter 2: 8 个（循环与条件）
  - Chapter 3: 15 个（函数）
  - Chapter 4: 11 个（文件与异常）
  - Chapter 5: 10 个（面向对象）

## ✅ 检查清单

开发新 World 时，确保：

- [ ] 每个练习一个文件（exercise_N.py）
- [ ] 每个测试一个文件（test_N.py）
- [ ] 所有练习有清晰的文档字符串
- [ ] 所有练习有输入输出示例
- [ ] 测试覆盖多个用例
- [ ] 测试有清晰的错误信息
- [ ] 有 lesson.md 讲解
- [ ] 有 test_base.py 共享类
- [ ] 可以用 `python test.py W.C.E` 测试
- [ ] 网页版有提示信息
- [ ] 文档已更新

## 🎯 后续 World 改进方向

### World 2-5 的额外要求

1. **LeetCode 风格题目**
   - 明确的输入输出
   - 避免副作用
   - 纯函数优先

2. **更多示例**
   - 每题至少 3 个示例
   - 包含边界情况
   - 说明特殊情况

3. **难度递进**
   - 简单 → 中等 → 困难
   - 循序渐进

4. **实战导向**
   - 贴近真实场景
   - 可以直接应用

## 📝 模板文件

### exercise_template.py

```python
"""
练习 N：[标题]

任务：[清晰的任务描述]
要求：[具体要求]
"""


def function_name(param1, param2):
    """
    [函数说明]
    
    参数:
        param1 (type): [说明]
        param2 (type): [说明]
    
    返回:
        type: [说明]
    
    示例:
        输入: [示例输入]
        输出: [示例输出]
        
        输入: [示例输入2]
        输出: [示例输出2]
    """
    # 在这里写你的代码
    pass
```

### test_template.py

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
        # 测试用例
        result = function_name(input)
        runner.test(
            "测试描述",
            result == expected,
            f"期望 {expected}，实际 {result}"
        )

    except Exception as e:
        runner.test("函数执行", False, str(e))

    success = runner.summary()
    return success


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
```

## 🎓 总结

World 1 建立了一个清晰、可扩展的学习平台架构：

1. **清晰的结构** - 一个练习一个文件
2. **统一的测试** - 命令行 + 网页双模式
3. **完善的文档** - 从入门到精通
4. **易于扩展** - 模板化开发

后续 World 2-5 将在此基础上：
- 采用 LeetCode 风格题目
- 更多输入输出示例
- 更贴近实战场景

---

**版本**: 1.0  
**更新日期**: 2026-04-22  
**适用范围**: World 2-5 开发参考
