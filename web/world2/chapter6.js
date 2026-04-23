const exercises = {
    1: { title: "练习 1：计算平均值", description: `<h2>练习 1：计算平均值</h2><p>计算指定列的平均值。</p><div class="code-block">def calculate_mean(df, column_name):
    # 使用 df[column_name].mean()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.1</code></p></div>` },
    2: { title: "练习 2：计算最大最小值", description: `<h2>练习 2：计算最大最小值</h2><p>返回 (最大值, 最小值)。</p><div class="code-block">def calculate_max_min(df, column_name):
    # 使用 max() 和 min()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.2</code></p></div>` },
    3: { title: "练习 3：分组统计", description: `<h2>练习 3：分组统计</h2><p>按指定列分组，计算平均值。</p><div class="code-block">def group_by_mean(df, group_column, value_column):
    # 使用 df.groupby()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.3</code></p></div>` },
    4: { title: "练习 4：多指标统计", description: `<h2>练习 4：多指标统计</h2><p>计算 mean, max, min。</p><div class="code-block">def group_by_multiple_stats(df, group_column, value_column):
    # 使用 .agg(['mean', 'max', 'min'])
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.4</code></p></div>` },
    5: { title: "练习 5：计数统计", description: `<h2>练习 5：计数统计</h2><p>统计每个值出现的次数。</p><div class="code-block">def count_by_group(df, column_name):
    # 使用 value_counts()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.5</code></p></div>` },
    6: { title: "练习 6：多列分组", description: `<h2>练习 6：多列分组</h2><p>按多列分组统计。</p><div class="code-block">def group_by_multiple_columns(df, group_columns, value_column):
    # 使用 df.groupby(group_columns)
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.6</code></p></div>` },
    7: { title: "练习 7：数据透视表", description: `<h2>练习 7：数据透视表</h2><p>创建数据透视表。</p><div class="code-block">def create_pivot_table(df, index_column, columns_column, values_column):
    # 使用 pd.pivot_table()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.7</code></p></div>` },
    8: { title: "练习 8：综合练习", description: `<h2>练习 8：新闻情绪分析</h2><p>分析每只股票的情绪统计。</p><div class="code-block">def analyze_sentiment_by_stock(df):
    # 返回包含平均情绪、新闻数量、总阅读量的 DataFrame
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 2.6.8</code></p></div>` }
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
