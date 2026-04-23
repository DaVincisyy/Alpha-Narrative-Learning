# 第9章：项目核心代码解读

> 现在我们来理解 quant-NPL 项目的核心代码是如何工作的。

## 🌱 项目架构

quant-NPL 项目的核心流程：

1. **数据采集**：爬取新闻数据
2. **文本处理**：清理和分词
3. **情绪分析**：计算情绪分数
4. **因子构建**：将情绪转化为交易信号
5. **回测分析**：评估策略效果

## 🔍 核心代码解析

### 1. 新闻处理模块

```python
class NewsProcessor:
    def process_news(self, raw_news):
        # 清理标题
        clean_title = self.clean_text(raw_news['title'])
        # 分词
        words = jieba.lcut(clean_title)
        # 计算情绪
        sentiment = self.calculate_sentiment(words)
        return sentiment
```

### 2. 因子构建模块

```python
def build_sentiment_factor(news_df, price_df):
    # 按日期和股票聚合情绪
    daily_sentiment = news_df.groupby(['date', 'stock_code'])['sentiment'].mean()
    # 合并价格数据
    factor_df = pd.merge(daily_sentiment, price_df, on=['date', 'stock_code'])
    return factor_df
```

## 🎯 理解项目逻辑

通过本章练习，你将能够：
- 读懂项目代码
- 理解数据流转
- 修改和扩展功能

## 📝 本章练习

8个练习帮助你理解项目核心。

```bash
python test.py 3.9.1
```
