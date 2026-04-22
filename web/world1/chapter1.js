// 练习数据
const exercises = {
    1: {
        title: "练习 1：创建股票列表",
        description: "创建一个包含以下 5 个股票代码的列表：AAPL, GOOGL, MSFT, TSLA, NVDA",
        initialCode: `def create_stock_list():
    # 在这里写你的代码
    # 提示：return ["AAPL", ...]
    pass`,
        test: function(code) {
            try {
                // 提取函数体
                const match = code.match(/def create_stock_list\(\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数，删除 pass 并写你的代码" };
                }

                // 检查是否有 return 语句
                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 函数需要返回一个列表，使用 return 语句" };
                }

                // 检查是否返回列表
                if (!funcBody.includes('[')) {
                    return { success: false, message: "❌ 需要返回一个列表，使用方括号 []" };
                }

                // 检查是否包含所有股票代码
                const expected = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"];
                let allFound = true;
                let missing = [];

                for (let stock of expected) {
                    if (!funcBody.includes(stock)) {
                        allFound = false;
                        missing.push(stock);
                    }
                }

                if (!allFound) {
                    return {
                        success: false,
                        message: `❌ 列表中缺少以下股票代码：${missing.join(', ')}\n期望：["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]`
                    };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你成功创建了一个列表对象。\n\n关键概念：\n• 列表是动态数组，存储对象引用（PyObject*）\n• 时间复杂度：索引 O(1)，append 平摊 O(1)\n• 内存布局：连续的指针数组\n• 可变对象：支持原地修改（in-place modification）\n\n扩容机制：\n当 len > allocated 时，按公式扩容：\nnew_size = (n + (n >> 3) + 6) & ~3"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    2: {
        title: "练习 2：创建公司信息字典",
        description: "创建一个字典，包含 name, ticker, price, industry 四个键",
        initialCode: `def create_company_dict():
    # 在这里写你的代码
    # 提示：return {"name": "Apple Inc.", ...}
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def create_company_dict\(\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数，删除 pass 并写你的代码" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 函数需要返回一个字典，使用 return 语句" };
                }

                if (!funcBody.includes('{')) {
                    return { success: false, message: "❌ 需要返回一个字典，使用花括号 {}" };
                }

                // 检查必需的键
                const requiredKeys = {
                    "name": "Apple Inc.",
                    "ticker": "AAPL",
                    "price": "150.25",
                    "industry": "Technology"
                };

                let missing = [];
                for (let key in requiredKeys) {
                    if (!funcBody.includes(`"${key}"`) && !funcBody.includes(`'${key}'`)) {
                        missing.push(key);
                    }
                }

                if (missing.length > 0) {
                    return {
                        success: false,
                        message: `❌ 字典中缺少以下键：${missing.join(', ')}\n\n期望的字典格式：\n{\n  "name": "Apple Inc.",\n  "ticker": "AAPL",\n  "price": 150.25,\n  "industry": "Technology"\n}`
                    };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你成功创建了一个字典对象。\n\n关键概念：\n• 字典基于哈希表实现（hash table）\n• 平均时间复杂度：查找/插入/删除 O(1)\n• 键必须是可哈希对象（immutable + __hash__）\n• Python 3.7+ 保持插入顺序（通过索引数组）\n\n哈希冲突：\n• 使用开放寻址法（open addressing）\n• 探测序列避免聚集（clustering）\n• 负载因子 > 2/3 时触发 resize"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    3: {
        title: "练习 3：获取列表的第 3 个元素",
        description: "给定一个列表，返回第 3 个元素（索引为 2）",
        initialCode: `def get_third_element(my_list):
    # 在这里写你的代码
    # 提示：记住索引从 0 开始！
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def get_third_element\(my_list\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 函数需要返回第 3 个元素" };
                }

                // 检查是否使用了索引 2
                if (funcBody.includes('[2]')) {
                    return {
                        success: true,
                        message: "✅ 测试通过！\n\n你掌握了索引访问机制。\n\n关键概念：\n• 索引是指针偏移量：base_ptr + index * sizeof(PyObject*)\n• 时间复杂度：O(1) 常数时间\n• 负索引：-1 表示最后一个元素（len + index）\n• 越界访问会抛出 IndexError\n\n内存访问过程：\nlist[2] 实际执行：\n1. 检查索引范围：0 <= index < len\n2. 计算地址：ob_item + 2 * sizeof(PyObject*)\n3. 解引用指针获取对象"
                    };
                } else if (funcBody.includes('[3]')) {
                    return {
                        success: false,
                        message: "❌ 索引错误\n\n第 3 个元素的索引是 2，不是 3\n\n索引计算：\n• 第 n 个元素的索引 = n - 1\n• 这是因为索引从 0 开始\n• 索引 0 指向第一个元素的指针"
                    };
                } else {
                    return {
                        success: false,
                        message: "❌ 需要使用索引访问\n\n语法：list[index]\n提示：第 3 个元素的索引是 2"
                    };
                }
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    4: {
        title: "练习 4：更新字典中的价格",
        description: "给定一个公司信息字典和新价格，更新字典中的 price 键的值",
        initialCode: `def update_price(company_dict, new_price):
    # 在这里写你的代码
    # 提示：company_dict["price"] = new_price
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def update_price\(company_dict, new_price\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('company_dict')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('["price"]') && !funcBody.includes("['price']")) {
                    return { success: false, message: "❌ 需要访问字典的 'price' 键\n\n格式：company_dict[\"price\"]" };
                }

                if (!funcBody.includes('=') || !funcBody.includes('new_price')) {
                    return { success: false, message: "❌ 需要将 new_price 赋值给 price 键\n\n格式：company_dict[\"price\"] = new_price" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回更新后的字典\n\n添加：return company_dict" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了字典的原地修改。\n\n关键概念：\n• 字典是可变对象，支持原地修改\n• 修改操作不改变对象 id（内存地址）\n• 时间复杂度：O(1) 平均情况\n• 哈希值不变：修改值不影响键的哈希\n\n内部实现：\n1. 计算 hash(\"price\")\n2. 定位到哈希表槽位\n3. 更新值指针（不重新哈希）\n\n可变 vs 不可变：\n• dict 可变：d[\"k\"] = v 原地修改\n• tuple 不可变：t[0] = x 会报错"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    5: {
        title: "练习 5：创建公司成立信息元组",
        description: "创建一个元组，包含：公司名称、成立年份、成立地点",
        initialCode: `def create_company_tuple():
    # 在这里写你的代码
    # 提示：return ("Apple", 1976, "California")
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def create_company_tuple\(\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 函数需要返回一个元组" };
                }

                if (!funcBody.includes('(') || !funcBody.includes(')')) {
                    return { success: false, message: "❌ 需要返回一个元组，使用圆括号 ()" };
                }

                const hasApple = funcBody.includes('"Apple"') || funcBody.includes("'Apple'");
                const has1976 = funcBody.includes('1976');
                const hasCalifornia = funcBody.includes('"California"') || funcBody.includes("'California'");

                if (!hasApple || !has1976 || !hasCalifornia) {
                    return {
                        success: false,
                        message: "❌ 元组内容不完整\n\n期望：(\"Apple\", 1976, \"California\")\n\n请确保包含：\n• 公司名称：\"Apple\"\n• 成立年份：1976\n• 成立地点：\"California\""
                    };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了元组的不可变性。\n\n关键概念：\n• 元组是不可变对象（immutable）\n• 创建后无法修改、添加、删除元素\n• 可以作为字典的键（因为可哈希）\n• 内存效率更高（无需预留扩容空间）\n\nCPython 实现：\ntypedef struct {\n    PyObject_VAR_HEAD\n    PyObject *ob_item[1];  // 固定大小数组\n} PyTupleObject;\n\n不可变的优势：\n• 线程安全（无需加锁）\n• 可哈希（可作为 dict key 或 set 元素）\n• 内存占用更小\n• 解释器可以优化（如缓存小元组）"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    6: {
        title: "练习 6：向列表添加新股票",
        description: "给定一个股票列表和一个新股票代码，将新股票添加到列表末尾",
        initialCode: `def add_stock_to_list(stock_list, new_stock):
    # 在这里写你的代码
    # 提示：使用 .append() 方法
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def add_stock_to_list\(stock_list, new_stock\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('append')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('append')) {
                    return { success: false, message: "❌ 需要使用 .append() 方法添加元素\n\n格式：stock_list.append(new_stock)" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回更新后的列表\n\n添加：return stock_list" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了列表的动态扩容机制。\n\n关键概念：\n• append() 操作平摊时间复杂度 O(1)\n• 当 len == allocated 时触发扩容\n• 扩容策略避免频繁 realloc\n\nCPython 扩容算法：\nnew_allocated = (n + (n >> 3) + 6) & ~3\n\n示例：\n• n=0: new=4\n• n=4: new=8\n• n=8: new=16\n• n=16: new=24\n\n为什么平摊 O(1)？\n虽然单次扩容是 O(n)，但扩容频率随 n 递减，\n平均每次 append 的成本是常数。"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    7: {
        title: "练习 7：从字典获取公司名称",
        description: "给定一个公司信息字典，返回 name 键对应的值",
        initialCode: `def get_company_name(company_dict):
    # 在这里写你的代码
    # 提示：return company_dict["name"]
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def get_company_name\(company_dict\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 函数需要返回公司名称" };
                }

                if (!funcBody.includes('["name"]') && !funcBody.includes("['name']")) {
                    return { success: false, message: "❌ 需要访问字典的 'name' 键\n\n格式：company_dict[\"name\"]" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了字典的键访问。\n\n关键概念：\n• dict[key] 通过哈希查找，O(1) 平均时间\n• KeyError：键不存在时抛出异常\n• dict.get(key, default)：安全访问，返回默认值\n\n哈希查找过程：\n1. 计算 hash(key)\n2. index = hash & (table_size - 1)\n3. 处理冲突（开放寻址）\n4. 返回值指针\n\n最坏情况 O(n)：\n• 所有键哈希冲突\n• 实际中极少发生\n• 负载因子控制在 2/3 以下"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    8: {
        title: "练习 8：计算列表中有多少个股票",
        description: "给定一个股票列表，返回列表的长度",
        initialCode: `def count_stocks(stock_list):
    # 在这里写你的代码
    # 提示：使用 len() 函数
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def count_stocks\(stock_list\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 函数需要返回列表长度" };
                }

                if (!funcBody.includes('len')) {
                    return { success: false, message: "❌ 需要使用 len() 函数计算长度\n\n格式：len(stock_list)" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n🎉 恭喜完成第 1 章！\n\n你掌握了 len() 函数和序列协议。\n\n关键概念：\n• len() 调用对象的 __len__() 方法\n• 时间复杂度：O(1) - 直接读取 ob_size 字段\n• 适用于所有实现了 __len__ 的对象\n\nCPython 实现：\nPyObject_Size(obj) {\n    return obj->ob_type->tp_as_sequence->sq_length(obj);\n}\n\n序列协议：\n• __len__：返回长度\n• __getitem__：索引访问\n• __setitem__：索引赋值\n• __delitem__：删除元素\n\n已掌握的核心概念：\n• 列表：动态数组、对象引用、扩容机制\n• 字典：哈希表、O(1)查找、可哈希性\n• 元组：不可变、可哈希、内存效率\n\n下一章：循环与条件判断"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    }
};

// 当前练习索引
let currentExercise = 0;
const totalExercises = 8;
let completedExercises = new Set();

// 初始化
document.addEventListener('DOMContentLoaded', function() {
    updateProgress();

    // 绑定侧边栏点击事件
    document.querySelectorAll('.exercise-item').forEach((item, index) => {
        item.addEventListener('click', function() {
            switchExercise(index);
        });
    });
});

// 切换练习
function switchExercise(index) {
    // 隐藏所有内容
    document.querySelectorAll('.lesson-content').forEach(content => {
        content.classList.remove('active');
    });

    // 显示选中的内容
    document.getElementById(`lesson-${index}`).classList.add('active');

    // 更新侧边栏状态
    document.querySelectorAll('.exercise-item').forEach(item => {
        item.classList.remove('active');
    });
    document.querySelector(`[data-exercise="${index}"]`).classList.add('active');

    currentExercise = index;

    // 滚动到顶部
    document.querySelector('.content-area').scrollTop = 0;
}

// 下一题
function nextExercise() {
    if (currentExercise < totalExercises) {
        switchExercise(currentExercise + 1);
    }
}

// 上一题
function prevExercise() {
    if (currentExercise > 0) {
        switchExercise(currentExercise - 1);
    }
}

// 运行测试
function runTest(exerciseNum) {
    const code = document.getElementById(`code-${exerciseNum}`).value;
    const output = document.getElementById(`output-${exerciseNum}`);
    const exercise = exercises[exerciseNum];

    if (!exercise) {
        output.textContent = "❌ 练习配置错误";
        output.className = "output-area show error";
        return;
    }

    const result = exercise.test(code);

    output.textContent = result.message;
    output.className = `output-area show ${result.success ? 'success' : 'error'}`;

    // 如果测试通过，标记为完成
    if (result.success) {
        completedExercises.add(exerciseNum);
        const exerciseItem = document.querySelector(`[data-exercise="${exerciseNum}"]`);
        if (exerciseItem) {
            exerciseItem.classList.add('completed');
        }
        updateProgress();
    }
}

// 重置代码
function resetCode(exerciseNum) {
    const exercise = exercises[exerciseNum];
    if (exercise) {
        document.getElementById(`code-${exerciseNum}`).value = exercise.initialCode;
        const output = document.getElementById(`output-${exerciseNum}`);
        output.className = "output-area";
    }
}

// 更新进度条
function updateProgress() {
    const progress = (completedExercises.size / totalExercises) * 100;
    document.getElementById('progressFill').style.width = `${progress}%`;
}
