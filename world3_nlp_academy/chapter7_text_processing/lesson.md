# 第7章：文本处理基础

> 欢迎来到 NLP 魔法学院！这一章我们将学习如何处理文本数据。

## 🌱 什么是文本处理？

### 为什么需要文本处理？

在 quant-NPL 项目中，我们处理的是新闻标题：

```python
# 原始新闻标题
"【重磅】公司业绩大涨50%！！！股价创新高"
"市场波动加剧，投资者需谨慎"
"   新产品发布成功   "
```

这些文本需要清理和标准化才能分析：
- 去除特殊符号
- 统一大小写
- 去除空格
- 分词

## 🔍 Python 字符串基础

### 1. 字符串操作

```python
text = "  Hello World  "

# 去除空格
text.strip()  # "Hello World"
text.lstrip()  # "Hello World  "
text.rstrip()  # "  Hello World"

# 大小写转换
text.lower()  # "  hello world  "
text.upper()  # "  HELLO WORLD  "

# 替换
text.replace("World", "Python")  # "  Hello Python  "

# 分割
text.split()  # ["Hello", "World"]
```

### 2. 字符串判断

```python
# 包含判断
"Hello" in text  # True
"Python" in text  # False

# 开头结尾判断
text.startswith("  Hello")  # True
text.endswith("World  ")  # True

# 字符类型判断
"123".isdigit()  # True
"abc".isalpha()  # True
```

## 💻 中文文本处理

### 1. 中文分词

中文不像英文有空格分隔，需要专门的分词工具：

```python
# 使用 jieba 分词
import jieba

text = "公司业绩大涨"
words = jieba.lcut(text)
print(words)  # ['公司', '业绩', '大涨']
```

### 2. 停用词过滤

停用词是没有实际意义的词（如"的"、"了"、"在"）：

```python
# 停用词列表
stopwords = ['的', '了', '在', '是', '我', '有', '和']

# 过滤停用词
text = "这是一个很好的产品"
words = jieba.lcut(text)
filtered = [w for w in words if w not in stopwords]
print(filtered)  # ['一个', '很好', '产品']
```

### 3. 特殊符号处理

```python
import re

# 去除标点符号
text = "【重磅】公司业绩大涨50%！！！"
clean_text = re.sub(r'[^\w\s]', '', text)
print(clean_text)  # "重磅公司业绩大涨50"

# 去除数字
text_no_num = re.sub(r'\d+', '', text)
print(text_no_num)  # "【重磅】公司业绩大涨%！！！"
```

## 🎯 在 quant-NPL 项目中的应用

### 场景1：清理新闻标题

```python
def clean_title(title):
    """清理新闻标题"""
    # 1. 去除空格
    title = title.strip()
    
    # 2. 去除特殊符号
    title = re.sub(r'[【】！？。，、；：""''（）《》]', '', title)
    
    # 3. 转小写（如果有英文）
    title = title.lower()
    
    return title

# 使用
raw_title = "【重磅】公司业绩大涨50%！！！"
clean = clean_title(raw_title)
print(clean)  # "重磅公司业绩大涨50%"
```

### 场景2：提取关键词

```python
def extract_keywords(title, stopwords):
    """提取关键词"""
    # 1. 分词
    words = jieba.lcut(title)
    
    # 2. 过滤停用词
    keywords = [w for w in words if w not in stopwords and len(w) > 1]
    
    return keywords

# 使用
title = "公司业绩大涨，股价创新高"
stopwords = ['的', '了', '在']
keywords = extract_keywords(title, stopwords)
print(keywords)  # ['公司', '业绩', '大涨', '股价', '创新高']
```

### 场景3：统计词频

```python
from collections import Counter

def count_word_frequency(titles):
    """统计词频"""
    all_words = []
    for title in titles:
        words = jieba.lcut(title)
        all_words.extend(words)
    
    # 统计词频
    word_counts = Counter(all_words)
    return word_counts.most_common(10)  # 返回前10个高频词

# 使用
titles = [
    "公司业绩大涨",
    "业绩超预期",
    "公司股价上涨"
]
top_words = count_word_frequency(titles)
print(top_words)  # [('公司', 2), ('业绩', 2), ...]
```

## ⚠️ 常见陷阱

### 陷阱1：编码问题

```python
# ❌ 可能出现编码错误
with open('news.txt', 'r') as f:
    text = f.read()

# ✅ 指定编码
with open('news.txt', 'r', encoding='utf-8') as f:
    text = f.read()
```

### 陷阱2：正则表达式贪婪匹配

```python
text = "【重磅】【独家】新闻"

# ❌ 贪婪匹配（匹配最长）
re.sub(r'【.*】', '', text)  # ""

# ✅ 非贪婪匹配
re.sub(r'【.*?】', '', text)  # "新闻"
```

### 陷阱3：分词后的空字符串

```python
# 分词可能产生空字符串
words = jieba.lcut("公司  业绩")
print(words)  # ['公司', '  ', '业绩']

# 过滤空字符串
words = [w for w in words if w.strip()]
print(words)  # ['公司', '业绩']
```

## 📝 本章练习

本章包含 8 个练习：

1. **练习1**：字符串清理
2. **练习2**：大小写转换
3. **练习3**：字符串分割
4. **练习4**：中文分词
5. **练习5**：停用词过滤
6. **练习6**：特殊符号去除
7. **练习7**：词频统计
8. **练习8**：综合练习 - 新闻标题处理

## 🚀 开始练习

```bash
python test.py 3.7.1
```

掌握文本处理，你就能为情绪分析做好准备！
