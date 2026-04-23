const exercises = {
    1: { title: "练习 1：字符串清理", description: `<h2>练习 1：字符串清理</h2><p>去除字符串首尾空格。</p><div class="code-block">def clean_string(text):
    # 使用 text.strip()
    pass</div><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.1</code></p></div>` },
    2: { title: "练习 2：大小写转换", description: `<h2>练习 2：大小写转换</h2><p>将文本转换为小写。</p><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.2</code></p></div>` },
    3: { title: "练习 3：字符串分割", description: `<h2>练习 3：字符串分割</h2><p>按空格分割字符串。</p><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.3</code></p></div>` },
    4: { title: "练习 4：中文分词", description: `<h2>练习 4：中文分词</h2><p>使用 jieba 分词。</p><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.4</code></p></div>` },
    5: { title: "练习 5：停用词过滤", description: `<h2>练习 5：停用词过滤</h2><p>过滤停用词。</p><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.5</code></p></div>` },
    6: { title: "练习 6：特殊符号去除", description: `<h2>练习 6：特殊符号去除</h2><p>使用正则表达式去除特殊符号。</p><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.6</code></p></div>` },
    7: { title: "练习 7：词频统计", description: `<h2>练习 7：词频统计</h2><p>统计词频并返回前N个高频词。</p><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.7</code></p></div>` },
    8: { title: "练习 8：综合练习", description: `<h2>练习 8：新闻标题处理</h2><p>清理、分词、过滤停用词。</p><div class="test-info"><h4>💻 在 VSCode 中测试</h4><p>运行命令：<code>python test.py 4.11.8</code></p></div>` }
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
