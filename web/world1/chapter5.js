// 第5章：面向对象编程 - 练习数据和测试逻辑

let currentExercise = 0;
const totalExercises = 7;

const exercises = {
    1: {
        title: "练习 1：创建基础股票类",
        description: "定义一个 Stock 类，包含 code、name、price 属性",
        initialCode: `class Stock:
    def __init__(self, code, name, price):
        # 在这里初始化属性
        # self.code = code
        pass`,
        test: function(code) {
            if (!code.includes('class Stock')) {
                return { success: false, message: "❌ 需要定义 Stock 类" };
            }
            if (!code.includes('__init__')) {
                return { success: false, message: "❌ 需要定义 __init__ 方法" };
            }
            if (!code.includes('self.code') || !code.includes('self.name') || !code.includes('self.price')) {
                return { success: false, message: "❌ 需要初始化 code、name、price 属性" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你创建了第一个类。\n\n关键概念：\n• class 关键字定义类\n• __init__ 是构造函数（初始化方法）\n• self 代表实例本身，类似其他语言的 this\n• 实例属性通过 self.属性名 定义\n\n🔍 深入理解：\n• 类是对象的模板，对象是类的实例\n• 每个对象有独立的属性空间\n• self 参数自动传递，调用时不需要显式传入\n\n💡 命名规范：\n• 类名使用大驼峰（PascalCase）\n• 方法名和属性名使用小写+下划线（snake_case）"
            };
        }
    },
    2: {
        title: "练习 2：添加方法",
        description: "为 Stock 类添加 get_value() 方法",
        initialCode: `class Stock:
    def __init__(self, code, price, shares):
        self.code = code
        self.price = price
        self.shares = shares

    def get_value(self):
        # 返回总价值（price * shares）
        pass`,
        test: function(code) {
            if (!code.includes('def get_value')) {
                return { success: false, message: "❌ 需要定义 get_value 方法" };
            }
            if (!code.includes('return')) {
                return { success: false, message: "❌ get_value 需要返回计算结果" };
            }
            if (!code.includes('self.price') || !code.includes('self.shares')) {
                return { success: false, message: "❌ 需要使用 self.price 和 self.shares" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了定义实例方法。\n\n实例方法：\n• 第一个参数是 self\n• 可以访问实例属性\n• 可以调用其他方法"
            };
        }
    },
    3: {
        title: "练习 3：实现魔法方法",
        description: "实现 __str__ 和 __eq__ 方法",
        initialCode: `class Stock:
    def __init__(self, code, price):
        self.code = code
        self.price = price

    def __str__(self):
        # 返回格式："AAPL: $150.25"
        pass

    def __eq__(self, other):
        # 比较股票代码是否相同
        pass`,
        test: function(code) {
            if (!code.includes('def __str__')) {
                return { success: false, message: "❌ 需要定义 __str__ 方法" };
            }
            if (!code.includes('def __eq__')) {
                return { success: false, message: "❌ 需要定义 __eq__ 方法" };
            }
            if (!code.includes('return') || code.split('return').length < 3) {
                return { success: false, message: "❌ 两个方法都需要返回值" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了魔法方法。\n\n常用魔法方法：\n• __str__ - print() 和 str() 时调用\n• __repr__ - 开发者友好的表示\n• __eq__ - == 比较时调用\n• __lt__ - < 比较时调用\n• __len__ - len() 时调用\n• __getitem__ - [] 索引时调用\n• __add__ - + 运算时调用\n\n🔍 __str__ vs __repr__：\n• __str__：面向用户，可读性优先\n• __repr__：面向开发者，应该能重建对象\n• 如果只定义一个，优先定义 __repr__\n\n💡 实际应用：\n实现魔法方法让自定义对象像内置类型一样使用。"
            };
        }
    },
    4: {
        title: "练习 4：继承",
        description: "创建 TradableStock 类继承 Stock",
        initialCode: `class Stock:
    def __init__(self, code, price):
        self.code = code
        self.price = price

class TradableStock(Stock):
    def __init__(self, code, price, shares):
        # 调用父类的 __init__
        # 添加 shares 属性
        pass

    def buy(self, amount):
        # 增加持有数量
        pass`,
        test: function(code) {
            if (!code.includes('class TradableStock(Stock)')) {
                return { success: false, message: "❌ TradableStock 需要继承 Stock" };
            }
            if (!code.includes('super()')) {
                return { success: false, message: "❌ 需要使用 super() 调用父类方法" };
            }
            if (!code.includes('def buy')) {
                return { success: false, message: "❌ 需要定义 buy 方法" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了继承。\n\n继承的优势：\n• 代码复用 - 避免重复代码\n• 扩展功能 - 在父类基础上添加新功能\n• 多态性 - 子类对象可以当作父类使用\n• 维护性 - 修改父类影响所有子类\n\n🔍 super() 的作用：\n• 调用父类的方法\n• 支持多重继承的 MRO（方法解析顺序）\n• 比直接调用父类名更灵活\n\n💡 设计原则：\n• 继承表示 \"is-a\" 关系（TradableStock 是一种 Stock）\n• 组合表示 \"has-a\" 关系\n• 优先使用组合而非继承（更灵活）"
            };
        }
    },
    5: {
        title: "练习 5：属性装饰器",
        description: "使用 @property 装饰器",
        initialCode: `class Stock:
    def __init__(self, code, price):
        self.code = code
        self._price = price

    @property
    def price(self):
        # 返回价格
        pass

    @price.setter
    def price(self, value):
        # 设置价格，必须 > 0
        pass`,
        test: function(code) {
            if (!code.includes('@property')) {
                return { success: false, message: "❌ 需要使用 @property 装饰器" };
            }
            if (!code.includes('@price.setter')) {
                return { success: false, message: "❌ 需要使用 @price.setter 装饰器" };
            }
            if (!code.includes('if') && !code.includes('ValueError')) {
                return { success: false, message: "💡 建议添加价格验证（> 0）" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了属性装饰器。\n\n@property 的优势：\n• 像访问属性一样调用方法\n• 可以添加验证逻辑\n• 保持接口一致性\n• 延迟计算（只在访问时计算）\n\n🔍 使用场景：\n• 需要验证的属性（如价格必须 > 0）\n• 计算属性（如根据其他属性计算）\n• 只读属性（只定义 getter，不定义 setter）\n• 需要在访问时触发副作用\n\n💡 命名约定：\n• 私有属性用下划线开头：_price\n• 公开属性通过 @property 暴露：price\n• 这样可以在不改变接口的情况下添加逻辑"
            };
        }
    },
    6: {
        title: "练习 6：类方法和静态方法",
        description: "实现类方法和静态方法",
        initialCode: `class Stock:
    total_stocks = 0

    def __init__(self, code):
        self.code = code
        Stock.total_stocks += 1

    @classmethod
    def get_total(cls):
        # 返回总股票数
        pass

    @staticmethod
    def is_valid_code(code):
        # 检查代码是否有效（1-5个大写字母）
        pass`,
        test: function(code) {
            if (!code.includes('@classmethod')) {
                return { success: false, message: "❌ 需要使用 @classmethod 装饰器" };
            }
            if (!code.includes('@staticmethod')) {
                return { success: false, message: "❌ 需要使用 @staticmethod 装饰器" };
            }
            if (!code.includes('cls.total_stocks') && !code.includes('Stock.total_stocks')) {
                return { success: false, message: "❌ 类方法需要访问类属性" };
            }
            return {
                success: true,
                message: "✅ 测试通过！\n\n你学会了类方法和静态方法。\n\n区别：\n• 实例方法：第一个参数 self\n• 类方法：第一个参数 cls\n• 静态方法：无特殊参数"
            };
        }
    },
    7: {
        title: "练习 7：综合应用 - 投资组合类",
        description: "创建完整的 Portfolio 类",
        initialCode: `class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = {}  # {code: Stock}

    def add_stock(self, stock):
        # 添加股票到组合
        pass

    def get_total_value(self):
        # 计算总价值
        pass

    def __len__(self):
        # 返回股票数量
        pass

    def __contains__(self, code):
        # 检查是否包含某只股票
        pass`,
        test: function(code) {
            if (!code.includes('class Portfolio')) {
                return { success: false, message: "❌ 需要定义 Portfolio 类" };
            }
            if (!code.includes('def add_stock')) {
                return { success: false, message: "❌ 需要定义 add_stock 方法" };
            }
            if (!code.includes('def __len__')) {
                return { success: false, message: "❌ 需要实现 __len__ 魔法方法" };
            }
            if (!code.includes('def __contains__')) {
                return { success: false, message: "❌ 需要实现 __contains__ 魔法方法" };
            }
            return {
                success: true,
                message: "✅ 恭喜！第 5 章全部完成！\n\n🎉 世界 1：Python 基础村 - 全部完成！\n\n你已经掌握：\n• 数据容器（列表、字典、元组）\n• 循环与条件判断\n• 函数定义与使用\n• 文件操作与异常处理\n• 面向对象编程\n\n下一步：进入世界 2 学习 Pandas 数据处理！"
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
