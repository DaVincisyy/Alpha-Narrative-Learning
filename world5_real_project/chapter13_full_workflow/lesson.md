# 第13章：完整流程实战

> 运行完整的 quant-NPL 项目。

## 🌱 项目完整流程

从数据到策略的完整流程：

1. **数据准备**：加载新闻和价格数据
2. **文本处理**：清理和分词
3. **情绪分析**：计算情绪分数
4. **因子构建**：生成交易信号
5. **回测分析**：评估策略表现

## 🔍 实战步骤

### 1. 运行主程序

```bash
cd C:\syy\claude project\quant-NPL
python main.py
```

### 2. 查看结果

```python
# 查看因子统计
print(factor_df.describe())

# 查看回测结果
print(f"年化收益: {annual_return:.2%}")
print(f"夏普比率: {sharpe_ratio:.2f}")
```

### 3. 修改参数

```python
# 调整情绪阈值
SENTIMENT_THRESHOLD = 0.7

# 调整持仓周期
HOLDING_PERIOD = 5
```

## 🎯 实战任务

通过本章练习，你将：
- 运行完整项目
- 理解每个模块
- 调试和优化代码

## 📝 本章练习

8个练习帮助你掌握完整流程。

```bash
python test.py 5.13.1
```
