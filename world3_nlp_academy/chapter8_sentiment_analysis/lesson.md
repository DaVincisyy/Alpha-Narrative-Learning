# 第8章：情绪分析原理

> 学会了文本处理，现在我们要理解如何判断文本的情绪倾向。

## 🌱 什么是情绪分析？

情绪分析（Sentiment Analysis）是判断文本表达的情感倾向：
- 正面（积极）：业绩大涨、股价创新高
- 负面（消极）：业绩下滑、市场波动
- 中性：公司发布公告

## 🔍 情绪分析方法

### 1. 基于词典的方法

使用预定义的情绪词典：

```python
positive_words = ['大涨', '上涨', '增长', '成功', '突破']
negative_words = ['下跌', '下滑', '波动', '风险', '亏损']

def simple_sentiment(text):
    pos_count = sum(1 for w in positive_words if w in text)
    neg_count = sum(1 for w in negative_words if w in text)
    return pos_count - neg_count
```

### 2. 情绪分数计算

```python
def calculate_sentiment_score(text, pos_dict, neg_dict):
    """计算情绪分数 [-1, 1]"""
    words = jieba.lcut(text)
    pos_score = sum(pos_dict.get(w, 0) for w in words)
    neg_score = sum(neg_dict.get(w, 0) for w in words)
    total = pos_score + neg_score
    if total == 0:
        return 0
    return (pos_score - neg_score) / total
```

## 🎯 在 quant-NPL 项目中的应用

```python
# 分析新闻情绪
news_df['sentiment'] = news_df['title'].apply(calculate_sentiment_score)

# 按情绪分组
positive_news = news_df[news_df['sentiment'] > 0.5]
negative_news = news_df[news_df['sentiment'] < -0.5]
```

## 📝 本章练习

8个练习帮助你掌握情绪分析基础。

```bash
python test.py 3.8.1
```
