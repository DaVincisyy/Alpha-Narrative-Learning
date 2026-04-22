// 第4章：文件操作与异常处理 - 练习数据和测试逻辑

let currentExercise = 0;
const totalExercises = 8;

const exercises = {
    1: {
        title: "练习 1：写入文本文件",
        description: "将股票代码列表写入文本文件",
        initialCode: `def write_stock_codes(codes, filename):
    # 将股票代码列表写入文件，每行一个代码
    # 提示：使用 with open(filename, 'w') as f:
    pass`,
        test: function(code) {
            if (code.includes('pass') && !code.includes('with')) {
                return { success: false, message: "❌ 需要使用 with 语句打开文件" };
            }
            if (!code.includes('with') || !code.includes('open')) {
                return { success: false, message: "❌ 需要使用 with open() 打开文件" };
            }
            if (!code.includes("'w'") && !code.includes('"w"')) {
                return { success: false, message: "❌ 需要使用写入模式 'w'" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了使用 with 语句写入文件。\n\n关键概念：\n• with 语句自动管理资源\n• 'w' 模式会覆盖已存在的文件\n• 'a' 模式会追加到文件末尾\n• 文件对象会在 with 块结束时自动关闭\n\n💡 最佳实践：\n始终使用 with 语句操作文件，即使出现异常也能正确关闭文件，避免资源泄漏。"
            };
        }
    },
    2: {
        title: "练习 2：读取文本文件",
        description: "从文件读取股票代码",
        initialCode: `def read_stock_codes(filename):
    # 读取文件并返回股票代码列表
    # 提示：使用 readlines() 并去除换行符
    pass`,
        test: function(code) {
            if (!code.includes('with') || !code.includes('open')) {
                return { success: false, message: "❌ 需要使用 with open() 打开文件" };
            }
            if (!code.includes("'r'") && !code.includes('"r"') && !code.includes('open(filename)')) {
                return { success: false, message: "❌ 需要使用读取模式 'r'" };
            }
            if (!code.includes('return')) {
                return { success: false, message: "❌ 需要返回读取的数据" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了读取文件内容。\n\n常用方法：\n• read() - 读取全部内容\n• readlines() - 按行读取\n• readline() - 读取一行"
            };
        }
    },
    3: {
        title: "练习 3：写入 CSV 文件",
        description: "将股票数据写入 CSV 文件",
        initialCode: `import csv

def write_stocks_csv(stocks, filename):
    # stocks 是字典列表：[{'code': 'AAPL', 'name': 'Apple', 'price': 150}]
    # 提示：使用 csv.DictWriter
    pass`,
        test: function(code) {
            if (!code.includes('csv')) {
                return { success: false, message: "❌ 需要使用 csv 模块" };
            }
            if (!code.includes('DictWriter')) {
                return { success: false, message: "❌ 需要使用 csv.DictWriter" };
            }
            if (!code.includes('writeheader') && !code.includes('writerow')) {
                return { success: false, message: "❌ 需要写入表头和数据行" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了写入 CSV 文件。\n\nCSV 模块核心方法：\n• DictWriter - 以字典方式写入\n• writeheader() - 写入表头\n• writerow(dict) - 写入单行\n• writerows(list) - 写入多行\n\n📊 CSV vs JSON：\n• CSV：表格数据，Excel 兼容，文件更小\n• JSON：嵌套数据，Web API 常用，可读性好\n\n💡 实际应用：\n金融数据导出常用 CSV 格式，便于在 Excel 中分析。"
            };
        }
    },
    4: {
        title: "练习 4：读取 CSV 文件",
        description: "从 CSV 文件读取股票数据",
        initialCode: `import csv

def read_stocks_csv(filename):
    # 返回股票字典列表
    # 提示：使用 csv.DictReader
    pass`,
        test: function(code) {
            if (!code.includes('csv')) {
                return { success: false, message: "❌ 需要使用 csv 模块" };
            }
            if (!code.includes('DictReader')) {
                return { success: false, message: "❌ 需要使用 csv.DictReader" };
            }
            if (!code.includes('return')) {
                return { success: false, message: "❌ 需要返回读取的数据" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了读取 CSV 文件。\n\nDictReader 优势：\n• 自动解析表头\n• 返回字典而非列表\n• 代码更易读"
            };
        }
    },
    5: {
        title: "练习 5：JSON 操作",
        description: "保存和加载 JSON 数据",
        initialCode: `import json

def save_portfolio_json(portfolio, filename):
    # 将投资组合保存为 JSON 文件
    # 提示：使用 json.dump()
    pass`,
        test: function(code) {
            if (!code.includes('json')) {
                return { success: false, message: "❌ 需要使用 json 模块" };
            }
            if (!code.includes('dump')) {
                return { success: false, message: "❌ 需要使用 json.dump()" };
            }
            if (!code.includes('indent')) {
                return { success: false, message: "💡 建议添加 indent=4 使格式更美观" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了 JSON 操作。\n\nJSON 核心方法：\n• dump(obj, file) - 写入文件\n• load(file) - 从文件读取\n• dumps(obj) - 转为字符串\n• loads(string) - 从字符串解析\n\n🔍 深入理解：\n• indent=4 参数让 JSON 格式化输出\n• ensure_ascii=False 支持中文\n• JSON 只支持基本类型（dict, list, str, int, float, bool, None）\n\n💡 实际应用：\nJSON 是 Web API 的标准格式，也常用于配置文件。"
            };
        }
    },
    6: {
        title: "练习 6：异常处理基础",
        description: "安全地转换价格字符串",
        initialCode: `def safe_convert_price(price_str):
    # 尝试转换为浮点数，失败返回 0.0
    # 提示：使用 try-except ValueError
    pass`,
        test: function(code) {
            if (!code.includes('try')) {
                return { success: false, message: "❌ 需要使用 try-except 语句" };
            }
            if (!code.includes('except')) {
                return { success: false, message: "❌ 需要 except 块捕获异常" };
            }
            if (!code.includes('ValueError')) {
                return { success: false, message: "❌ 需要捕获 ValueError 异常" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了异常处理。\n\n常见异常类型：\n• ValueError - 值类型正确但值不合法\n• TypeError - 类型错误\n• FileNotFoundError - 文件不存在\n• KeyError - 字典键不存在\n• ZeroDivisionError - 除以零\n• IndexError - 索引越界\n\n🔍 异常处理最佳实践：\n• 捕获具体的异常类型，不要用空 except\n• 只在必要时捕获异常，不要隐藏错误\n• 可以用 else 块处理无异常情况\n• 用 finally 块清理资源\n\n💡 实际应用：\n处理用户输入、网络请求、文件操作时都需要异常处理。"
            };
        }
    },
    7: {
        title: "练习 7：文件异常处理",
        description: "安全地读取文件",
        initialCode: `def safe_read_file(filename):
    # 尝试读取文件，失败返回 None
    # 提示：捕获 FileNotFoundError
    pass`,
        test: function(code) {
            if (!code.includes('try')) {
                return { success: false, message: "❌ 需要使用 try-except 语句" };
            }
            if (!code.includes('FileNotFoundError')) {
                return { success: false, message: "❌ 需要捕获 FileNotFoundError" };
            }
            if (!code.includes('return None')) {
                return { success: false, message: "❌ 文件不存在时需要返回 None" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了处理文件异常。\n\n最佳实践：\n• 捕获具体的异常类型\n• 不要用空 except\n• 提供有意义的错误处理"
            };
        }
    },
    8: {
        title: "练习 8：综合应用 - 数据验证",
        description: "加载并验证 CSV 数据",
        initialCode: `import csv

def load_and_validate_stocks(filename):
    # 加载 CSV 并验证数据
    # 跳过无效行，返回有效股票列表
    # 提示：外层捕获 FileNotFoundError，内层捕获 ValueError
    pass`,
        test: function(code) {
            if (!code.includes('try')) {
                return { success: false, message: "❌ 需要使用异常处理" };
            }
            if (!code.includes('FileNotFoundError')) {
                return { success: false, message: "❌ 需要处理文件不存在的情况" };
            }
            if (!code.includes('csv')) {
                return { success: false, message: "❌ 需要使用 csv 模块" };
            }
            return {
                success: true,
                message: "✅ 恭喜！第 4 章全部完成！\n\n你已经掌握：\n• 文件读写操作\n• CSV 和 JSON 处理\n• 异常处理机制\n• 数据验证技巧\n\n下一步：进入第 5 章学习面向对象编程"
            };
        }
    }
};

// 初始化
function init() {
    loadExercise(0);
    updateProgress();
}

// 加载练习
function loadExercise(exerciseNum) {
    currentExercise = exerciseNum;

    // 更新侧边栏
    document.querySelectorAll('.exercise-item').forEach((item, index) => {
        item.classList.remove('active');
        if (index === exerciseNum) {
            item.classList.add('active');
        }
    });

    // 隐藏所有内容
    document.querySelectorAll('.lesson-content').forEach(content => {
        content.classList.remove('active');
    });

    // 检查是否已存在lesson div
    let currentLesson = document.getElementById(`lesson-${exerciseNum}`);

    // 如果不存在且是练习题，才动态生成
    if (!currentLesson && exerciseNum > 0 && exercises[exerciseNum]) {
        generateExerciseContent(exerciseNum);
        currentLesson = document.getElementById(`lesson-${exerciseNum}`);
    }

    // 激活当前练习
    if (currentLesson) {
        currentLesson.classList.add('active');
    }

    updateProgress();
}

// 生成练习内容
function generateExerciseContent(num) {
    const exercise = exercises[num];
    const contentArea = document.getElementById('contentArea');

    let lessonDiv = document.getElementById(`lesson-${num}`);
    if (!lessonDiv) {
        lessonDiv = document.createElement('div');
        lessonDiv.id = `lesson-${num}`;
        lessonDiv.className = 'lesson-content';
        contentArea.appendChild(lessonDiv);
    }

    lessonDiv.innerHTML = `
        <h2>${exercise.title}</h2>
        <p>${exercise.description}</p>

        <div class="code-editor">
            <textarea id="code-${num}" placeholder="在这里写你的代码...">${exercise.initialCode}</textarea>
            <div class="button-group">
                <button class="btn btn-primary" onclick="runTest(${num})">运行测试</button>
                <button class="btn btn-secondary" onclick="resetCode(${num})">重置代码</button>
            </div>
        </div>

        <div class="output-area" id="output-${num}"></div>

        <div class="nav-buttons">
            <button class="btn btn-secondary" onclick="prevExercise()">← 上一题</button>
            <button class="btn btn-primary" onclick="nextExercise()">下一题 →</button>
        </div>
    `;
}

// 运行测试
function runTest(num) {
    const code = document.getElementById(`code-${num}`).value;
    const output = document.getElementById(`output-${num}`);
    const exercise = exercises[num];

    const result = exercise.test(code);

    output.className = 'output-area show ' + (result.success ? 'success' : 'error');
    output.textContent = result.message;

    if (result.success) {
        document.querySelector(`[data-exercise="${num}"]`).classList.add('completed');
        updateProgress();
    }
}

// 重置代码
function resetCode(num) {
    const exercise = exercises[num];
    document.getElementById(`code-${num}`).value = exercise.initialCode;
    document.getElementById(`output-${num}`).className = 'output-area';
}

// 下一题
function nextExercise() {
    if (currentExercise < totalExercises) {
        loadExercise(currentExercise + 1);
    }
}

// 上一题
function prevExercise() {
    if (currentExercise > 0) {
        loadExercise(currentExercise - 1);
    }
}

// 更新进度
function updateProgress() {
    const completed = document.querySelectorAll('.exercise-item.completed').length;
    const progress = (completed / totalExercises) * 100;
    document.getElementById('progressFill').style.width = progress + '%';
}

// 侧边栏点击事件
document.addEventListener('DOMContentLoaded', function() {
    init();

    document.querySelectorAll('.exercise-item').forEach((item, index) => {
        item.addEventListener('click', function() {
            loadExercise(index);
        });
    });
});
