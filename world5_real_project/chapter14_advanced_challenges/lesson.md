# 第14章：进阶挑战

> 扩展和改进 quant-NPL 项目。

## 🌱 进阶方向

掌握基础后，你可以：

1. **改进情绪分析**：使用更好的模型
2. **增加新因子**：结合技术指标
3. **优化策略**：改进选股和择时
4. **风险控制**：添加止损和仓位管理

## 🔍 挑战任务

### 挑战1：多因子策略

```python
# 结合多个因子
def multi_factor_strategy(sentiment, momentum, value):
    # 因子加权
    score = 0.4 * sentiment + 0.3 * momentum + 0.3 * value
    # 选股
    top_stocks = score.nlargest(20)
    return top_stocks
```

### 挑战2：动态调整

```python
# 根据市场状态调整策略
def adaptive_strategy(market_state):
    if market_state == 'bull':
        return aggressive_params
    else:
        return conservative_params
```

### 挑战3：实时监控

```python
# 实时获取新闻并分析
def real_time_monitor():
    while True:
        new_news = fetch_latest_news()
        sentiment = analyze_sentiment(new_news)
        if abs(sentiment) > threshold:
            send_alert(sentiment)
```

## 🎯 最终项目

完成你自己的量化策略：
- 选择感兴趣的因子
- 设计交易规则
- 回测验证效果
- 撰写分析报告

## 📝 本章练习

8个挑战练习等你完成。

```bash
python test.py 5.14.1
```

## 🎉 恭喜！

完成所有章节后，你已经掌握了：
- Python数据分析
- Pandas数据处理
- NLP文本分析
- 量化因子构建
- 策略回测验证

现在你可以独立运行和改进 quant-NPL 项目了！
