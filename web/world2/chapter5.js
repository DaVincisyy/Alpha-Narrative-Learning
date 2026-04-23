const exercises = {
    1: { title: "练习 1：简单条件筛选", description: `<h2>练习 1：简单条件筛选</h2><p>筛选价格大于指定阈值的股票。</p><div class="code-block">def filter_by_price(df, threshold):
    # 使用 df[df['价格'] > threshold]
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.1</code></p></div>` },
    2: { title: "练习 2：多条件筛选（AND）", description: `<h2>练习 2：多条件筛选（AND）</h2><p>筛选价格大于阈值且涨跌幅为正的股票。</p><div class="code-block">def filter_by_price_and_change(df, price_threshold):
    # 使用 & 连接条件
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.2</code></p></div>` },
    3: { title: "练习 3：多条件筛选（OR）", description: `<h2>练习 3：多条件筛选（OR）</h2><p>筛选满足任一条件的股票。</p><div class="code-block">def filter_by_price_or_change(df, price_threshold, change_threshold):
    # 使用 | 连接条件
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.3</code></p></div>` },
    4: { title: "练习 4：范围筛选", description: `<h2>练习 4：范围筛选</h2><p>筛选价格在指定范围内的股票。</p><div class="code-block">def filter_by_price_range(df, min_price, max_price):
    # 使用 df['价格'].between()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.4</code></p></div>` },
    5: { title: "练习 5：字符串筛选", description: `<h2>练习 5：字符串筛选</h2><p>筛选标题中包含关键词的新闻。</p><div class="code-block">def filter_by_keyword(df, keyword):
    # 使用 df['标题'].str.contains()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.5</code></p></div>` },
    6: { title: "练习 6：列表筛选（isin）", description: `<h2>练习 6：列表筛选</h2><p>筛选股票代码在列表中的行。</p><div class="code-block">def filter_by_stock_list(df, stock_codes):
    # 使用 df['股票代码'].isin()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.6</code></p></div>` },
    7: { title: "练习 7：复杂条件组合", description: `<h2>练习 7：复杂条件组合</h2><p>使用多个条件筛选股票。</p><div class="code-block">def filter_complex_conditions(df):
    # 组合多个条件
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.7</code></p></div>` },
    8: { title: "练习 8：综合练习", description: `<h2>练习 8：筛选高质量新闻</h2><p>筛选情绪分数>0.7、阅读量>5000、标题包含关键词的新闻。</p><div class="code-block">def filter_quality_news(df):
    # 综合运用多种筛选条件
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.5.8</code></p></div>` }
};
let currentExercise = 1;
function init() { renderExerciseList(); showExercise(1); }
function renderExerciseList() {
    const list = document.getElementById('exerciseList');
    list.innerHTML = '';
    for (let i = 1; i <= 8; i++) {
        const li = document.createElement('li');
        li.className = 'exercise-item';
        li.textContent = exercises[i].title;
        li.onclick = () => showExercise(i);
        list.appendChild(li);
    }
}
function showExercise(num) {
    currentExercise = num;
    const items = document.querySelectorAll('.exercise-item');
    items.forEach((item, index) => { item.classList.toggle('active', index + 1 === num); });
    document.getElementById('contentArea').innerHTML = `<div class="lesson-content active">${exercises[num].description}</div>`;
    document.getElementById('progressBar').style.width = (num / 8) * 100 + '%';
}
document.addEventListener('DOMContentLoaded', init);
