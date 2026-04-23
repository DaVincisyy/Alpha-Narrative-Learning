// 练习数据
const exercises = {
    1: {
        title: "练习 1：创建 DataFrame",
        description: `
            <h2>练习 1：创建 DataFrame</h2>
            <p>从字典创建一个包含股票数据的 DataFrame。</p>

            <h3>任务</h3>
            <p>创建包含以下数据的 DataFrame：</p>
            <ul>
                <li>股票代码: ['000001', '000002', '000003']</li>
                <li>价格: [10.5, 20.3, 15.8]</li>
                <li>涨跌幅: [0.05, -0.02, 0.03]</li>
            </ul>

            <h3>代码示例</h3>
            <div class="code-block">import pandas as pd

def create_stock_dataframe():
    # 在这里写你的代码
    # 提示：使用 pd.DataFrame() 和字典
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.1</code></p>
                <p>测试将验证：DataFrame 的形状、列名和数据是否正确</p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>1. 使用字典创建 DataFrame，键是列名，值是列表</p>
                <p>2. 使用 pd.DataFrame(data) 创建</p>
                <p>3. 返回创建的 DataFrame</p>
            </div>
        `
    },
    2: {
        title: "练习 2：查看 DataFrame 信息",
        description: `
            <h2>练习 2：查看 DataFrame 信息</h2>
            <p>获取 DataFrame 的基本信息：行数和列数。</p>

            <h3>任务</h3>
            <p>编写函数返回 DataFrame 的形状 (行数, 列数)。</p>

            <h3>代码示例</h3>
            <div class="code-block">def get_dataframe_shape(df):
    # 在这里写你的代码
    # 提示：使用 df.shape 属性
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.2</code></p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>df.shape 返回一个元组 (行数, 列数)</p>
            </div>
        `
    },
    3: {
        title: "练习 3：选择单列",
        description: `
            <h2>练习 3：选择单列</h2>
            <p>从 DataFrame 中选择指定的列。</p>

            <h3>任务</h3>
            <p>返回指定列名的数据（Series）。</p>

            <h3>代码示例</h3>
            <div class="code-block">def select_column(df, column_name):
    # 在这里写你的代码
    # 提示：使用 df[column_name]
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.3</code></p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>使用方括号 [] 选择列，返回的是 Series 对象</p>
            </div>
        `
    },
    4: {
        title: "练习 4：选择多列",
        description: `
            <h2>练习 4：选择多列</h2>
            <p>从 DataFrame 中选择多个列。</p>

            <h3>任务</h3>
            <p>返回包含指定列的新 DataFrame。</p>

            <h3>代码示例</h3>
            <div class="code-block">def select_columns(df, column_names):
    # 在这里写你的代码
    # 提示：使用 df[column_names]，注意双层方括号
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.4</code></p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>使用双层方括号 df[[col1, col2]] 选择多列</p>
            </div>
        `
    },
    5: {
        title: "练习 5：选择行",
        description: `
            <h2>练习 5：选择行</h2>
            <p>使用 iloc 选择指定位置的行。</p>

            <h3>任务</h3>
            <p>返回指定索引位置的行数据。</p>

            <h3>代码示例</h3>
            <div class="code-block">def select_row_by_position(df, position):
    # 在这里写你的代码
    # 提示：使用 df.iloc[position]
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.5</code></p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>iloc 用于基于位置的索引，从 0 开始</p>
            </div>
        `
    },
    6: {
        title: "练习 6：选择特定单元格",
        description: `
            <h2>练习 6：选择特定单元格</h2>
            <p>使用 loc 选择特定行和列的值。</p>

            <h3>任务</h3>
            <p>返回指定行索引和列名的单元格值。</p>

            <h3>代码示例</h3>
            <div class="code-block">def get_cell_value(df, row_index, column_name):
    # 在这里写你的代码
    # 提示：使用 df.loc[row_index, column_name]
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.6</code></p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>loc 用于基于标签的索引</p>
            </div>
        `
    },
    7: {
        title: "练习 7：添加新列",
        description: `
            <h2>练习 7：添加新列</h2>
            <p>向 DataFrame 添加新列。</p>

            <h3>任务</h3>
            <p>添加总价值列（价格 * 成交量）。</p>

            <h3>代码示例</h3>
            <div class="code-block">def add_total_value_column(df):
    # 在这里写你的代码
    # 提示：df['总价值'] = df['价格'] * df['成交量']
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.7</code></p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>直接对列进行运算，Pandas 会自动逐行计算</p>
            </div>
        `
    },
    8: {
        title: "练习 8：综合练习",
        description: `
            <h2>练习 8：综合练习 - 处理股票数据</h2>
            <p>综合运用 DataFrame 操作处理股票数据。</p>

            <h3>任务</h3>
            <p>1. 创建包含股票代码、开盘价、收盘价的 DataFrame</p>
            <p>2. 添加涨跌幅列（(收盘价 - 开盘价) / 开盘价）</p>
            <p>3. 返回涨跌幅大于 0 的股票代码列表</p>

            <h3>代码示例</h3>
            <div class="code-block">def analyze_stock_data(stock_codes, open_prices, close_prices):
    # 在这里写你的代码
    # 步骤：
    # 1. 创建 DataFrame
    # 2. 计算涨跌幅列
    # 3. 筛选涨跌幅 > 0 的行
    # 4. 返回股票代码列表
    pass</div>

            <div class="test-info">
                <h4>💻 在 VSCode 中测试</h4>
                <p>运行命令：<code>python test.py 2.4.8</code></p>
            </div>

            <div class="hint-box">
                <h4>💡 提示</h4>
                <p>1. 使用字典创建 DataFrame</p>
                <p>2. 添加新列进行计算</p>
                <p>3. 使用布尔索引筛选</p>
                <p>4. 使用 list() 转换为列表</p>
            </div>
        `
    }
};

// 初始化页面
let currentExercise = 1;

function init() {
    renderExerciseList();
    showExercise(1);
}

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

    // 更新侧边栏激活状态
    const items = document.querySelectorAll('.exercise-item');
    items.forEach((item, index) => {
        item.classList.toggle('active', index + 1 === num);
    });

    // 显示练习内容
    const contentArea = document.getElementById('contentArea');
    contentArea.innerHTML = `
        <div class="lesson-content active">
            ${exercises[num].description}
        </div>
    `;

    // 更新进度条
    updateProgress();
}

function updateProgress() {
    const progress = (currentExercise / 8) * 100;
    document.getElementById('progressBar').style.width = progress + '%';
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', init);
