// 第3章练习数据和测试逻辑

const exercises = {
    1: {
        title: "练习 1：定义基础函数",
        description: "计算股票收益率",
        initialCode: `def calculate_profit(buy_price, sell_price):
    # 在这里写你的代码
    # 提示：return (sell_price - buy_price) / buy_price * 100
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def calculate_profit\(buy_price, sell_price\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要返回计算结果" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 函数需要返回计算结果\n\n使用 return 语句" };
                }

                if (!funcBody.includes('-') || !funcBody.includes('/')) {
                    return { success: false, message: "❌ 需要计算收益率\n\n公式：(sell_price - buy_price) / buy_price * 100" };
                }

                if (!funcBody.includes('100') && !funcBody.includes('* 100')) {
                    return { success: false, message: "❌ 别忘了乘以 100 转换成百分比" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你创建了第一个函数。\n\n关键概念：\n• def 关键字定义函数\n• 函数名使用小写+下划线命名\n• 参数在括号中定义\n• return 返回结果\n\n🔍 深入理解：\n• 函数是一等公民，可以赋值给变量\n• 函数调用时会创建新的作用域\n• 参数传递是引用传递（传递对象引用）\n\n💡 最佳实践：\n• 函数应该只做一件事\n• 函数名应该清楚描述功能（动词开头）\n• 避免副作用（修改全局变量）\n• 保持函数简短（一般不超过20行）"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    2: {
        title: "练习 2：多个参数",
        description: "计算股票价值并返回字典",
        initialCode: `def calculate_stock_value(ticker, price, shares):
    # 在这里写你的代码
    # 返回格式：{"ticker": ticker, "value": price * shares}
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def calculate_stock_value\(ticker, price, shares\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回一个字典" };
                }

                if (!funcBody.includes('{')) {
                    return { success: false, message: "❌ 需要返回字典类型\n\n格式：return {\"ticker\": ticker, \"value\": ...}" };
                }

                const hasTicker = funcBody.includes('"ticker"') || funcBody.includes("'ticker'");
                const hasValue = funcBody.includes('"value"') || funcBody.includes("'value'");

                if (!hasTicker || !hasValue) {
                    return { success: false, message: "❌ 字典需要包含 ticker 和 value 两个键" };
                }

                if (!funcBody.includes('*')) {
                    return { success: false, message: "❌ 需要计算价值：price * shares" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了多参数函数和复合返回值。\n\n关键概念：\n• 参数传递：按位置匹配到局部变量\n• 返回字典：创建 PyDictObject 并返回引用\n• 时间复杂度：O(1) - 字典创建和返回\n\n字节码分析：\nreturn {\"ticker\": ticker, \"value\": price * shares}\n\n# BUILD_MAP (2)           # 创建空字典，预分配 2 个槽位\n# LOAD_CONST (\"ticker\")\n# LOAD_FAST (ticker)\n# STORE_MAP               # 存储键值对\n# LOAD_CONST (\"value\")\n# LOAD_FAST (price)\n# LOAD_FAST (shares)\n# BINARY_MULTIPLY\n# STORE_MAP\n# RETURN_VALUE\n\n参数传递机制：\n• 位置参数：按顺序绑定到 LOAD_FAST 槽位\n• 所有对象通过引用传递（指针）\n• 不可变对象：安全共享\n• 可变对象：修改会影响调用者"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    3: {
        title: "练习 3：返回多个值",
        description: "同时返回最大值和最小值",
        initialCode: `def get_min_max(prices):
    # 在这里写你的代码
    # 提示：return min(prices), max(prices)
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def get_min_max\(prices\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回最小值和最大值" };
                }

                const hasMin = funcBody.includes('min(') || funcBody.includes('min (');
                const hasMax = funcBody.includes('max(') || funcBody.includes('max (');

                if (!hasMin || !hasMax) {
                    return { success: false, message: "❌ 需要使用 min() 和 max() 函数\n\n提示：return min(prices), max(prices)" };
                }

                if (!funcBody.includes(',')) {
                    return { success: false, message: "❌ 返回多个值时用逗号分隔\n\n格式：return 值1, 值2" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了多返回值。\n\n关键概念：\n• return a, b 实际返回一个元组 (a, b)\n• 接收时可以解包：min_val, max_val = get_min_max(prices)\n• 元组是不可变的，创建后不能修改\n\n🔍 深入理解：\n• 多返回值是元组打包（tuple packing）\n• Python 自动将多个值打包成元组\n• 解包时数量必须匹配，否则报错\n\n💡 实际应用：\n• 函数需要返回多个相关值时使用\n• 比返回列表或字典更轻量\n• 常用于返回计算结果和状态"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    4: {
        title: "练习 4：默认参数",
        description: "带默认值的函数",
        initialCode: `def calculate_total(price, quantity=1, tax=0.1):
    # 在这里写你的代码
    # 计算总价：price * quantity * (1 + tax)
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def calculate_total\(price, quantity=1, tax=0\.1\):([\s\S]*)/);
                if (!match) {
                    return { success: false, message: "❌ 函数定义不正确\n\n确保参数有默认值：quantity=1, tax=0.1" };
                }

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回计算结果" };
                }

                if (!funcBody.includes('*')) {
                    return { success: false, message: "❌ 需要计算总价\n\n公式：price * quantity * (1 + tax)" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了默认参数。\n\n关键概念：\n• 默认参数在函数定义时设置\n• 调用时可以省略有默认值的参数\n• 默认参数必须在必需参数之后\n• 默认值在函数定义时计算（只执行一次）\n\n🔍 深入理解：\n• 默认参数存储在函数对象的 __defaults__ 属性中\n• 可以通过 func.__defaults__ 查看\n• 默认参数让函数更灵活，减少重复代码\n\n⚠️ 重要陷阱：\n不要使用可变对象（列表、字典）作为默认值！\n\n错误示例：\ndef add_item(item, items=[]):\n    items.append(item)\n    return items\n# 多次调用会共享同一个列表！\n\n正确做法：\ndef add_item(item, items=None):\n    if items is None:\n        items = []\n    items.append(item)\n    return items"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    5: {
        title: "练习 5：关键字参数",
        description: "使用关键字参数调用函数",
        initialCode: `def create_stock_info(ticker, price, volume, change):
    # 在这里写你的代码
    # 返回包含所有信息的字典
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def create_stock_info\(ticker, price, volume, change\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回字典" };
                }

                if (!funcBody.includes('{')) {
                    return { success: false, message: "❌ 需要返回字典类型" };
                }

                const keys = ['ticker', 'price', 'volume', 'change'];
                let missingKeys = [];
                for (let key of keys) {
                    if (!funcBody.includes(`"${key}"`) && !funcBody.includes(`'${key}'`)) {
                        missingKeys.push(key);
                    }
                }

                if (missingKeys.length > 0) {
                    return {
                        success: false,
                        message: `❌ 字典缺少以下键：${missingKeys.join(', ')}\n\n需要包含所有参数`
                    };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了关键字参数的调用机制。\n\n关键概念：\n• 关键字参数：通过名称传递，不依赖位置\n• 字节码：CALL_FUNCTION_KW 指令\n• 时间复杂度：O(k) - k 为关键字参数数量\n• 参数匹配：按名称查找对应的局部变量槽位\n\n字节码分析：\ncreate_stock_info(\n    ticker=\"AAPL\",\n    price=150.25,\n    volume=1000000,\n    change=2.5\n)\n\n# LOAD_GLOBAL (create_stock_info)\n# LOAD_CONST (\"AAPL\")\n# LOAD_CONST (150.25)\n# LOAD_CONST (1000000)\n# LOAD_CONST (2.5)\n# LOAD_CONST ((\"ticker\", \"price\", \"volume\", \"change\"))\n# CALL_FUNCTION_KW (4)  # 4 个关键字参数\n\n参数匹配过程：\n1. 解析关键字元组\n2. 按名称查找参数位置\n3. 绑定到对应的 LOAD_FAST 槽位\n\n混合调用：\nfunc(1, 2, c=3, d=4)  # 位置 + 关键字\n# 位置参数必须在关键字参数之前"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    6: {
        title: "练习 6：lambda 函数",
        description: "使用 lambda 创建匿名函数",
        initialCode: `# 创建一个 lambda 函数，计算平方
square = # 在这里写你的 lambda 函数
# 提示：lambda x: x ** 2`,
        test: function(code) {
            try {
                if (!code.includes('lambda')) {
                    return { success: false, message: "❌ 需要使用 lambda 关键字\n\n格式：lambda 参数: 表达式" };
                }

                if (!code.includes('**') && !code.includes('* x')) {
                    return { success: false, message: "❌ 需要计算平方\n\n提示：x ** 2 或 x * x" };
                }

                if (!code.includes('square =')) {
                    return { success: false, message: "❌ 需要将 lambda 函数赋值给 square 变量" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了 lambda 表达式。\n\n关键概念：\n• lambda 创建匿名函数\n• 语法：lambda 参数: 表达式\n• 只能包含单个表达式，不能有语句\n• 表达式的值自动返回\n\n🔍 lambda vs def：\n• lambda 适合简单的一次性函数\n• def 适合复杂逻辑和需要复用的函数\n• 性能完全相同，只是语法不同\n\n💡 使用场景：\n• 作为 map、filter、sorted 的参数\n• 简单的回调函数\n• 避免定义只用一次的函数\n\n示例：\n# 排序时指定排序键\nstocks.sort(key=lambda s: s['price'])\n\n# 过滤列表\nexpensive = filter(lambda s: s['price'] > 100, stocks)"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    7: {
        title: "练习 7：map 函数",
        description: "使用 map 对列表中每个元素应用函数",
        initialCode: `def double_prices(prices):
    # 使用 map 将所有价格翻倍
    # 提示：list(map(lambda x: x * 2, prices))
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def double_prices\(prices\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('map')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要使用 map" };
                }

                if (!funcBody.includes('map')) {
                    return { success: false, message: "❌ 需要使用 map() 函数\n\n格式：map(函数, 列表)" };
                }

                if (!funcBody.includes('lambda') && !funcBody.includes('def ')) {
                    return { success: false, message: "❌ map 需要一个函数作为参数\n\n可以使用 lambda 或定义的函数" };
                }

                if (!funcBody.includes('list(')) {
                    return { success: false, message: "❌ map 返回迭代器，需要转换成列表\n\n提示：list(map(...))" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回结果列表" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了 map 函数。\n\n关键概念：\n• map(函数, 可迭代对象) 对每个元素应用函数\n• 返回迭代器（惰性求值）\n• 需要用 list() 转换成列表\n• 不修改原列表，返回新结果\n\n🔍 map vs 列表推导式：\n\nmap 方式：\nlist(map(lambda x: x * 2, prices))\n\n列表推导式：\n[x * 2 for x in prices]\n\n区别：\n• map 返回迭代器，节省内存\n• 列表推导式立即创建列表\n• 列表推导式可读性更好\n• map 适合链式操作\n\n💡 实际应用：\n# 转换数据类型\nstr_prices = ['100', '200', '300']\nprices = list(map(float, str_prices))\n\n# 批量处理\nuppercase = list(map(str.upper, names))"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    8: {
        title: "练习 8：filter 函数",
        description: "使用 filter 筛选列表元素",
        initialCode: `def filter_high_prices(prices, threshold):
    # 使用 filter 筛选大于阈值的价格
    # 提示：list(filter(lambda x: x > threshold, prices))
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def filter_high_prices\(prices, threshold\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('filter')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要使用 filter" };
                }

                if (!funcBody.includes('filter')) {
                    return { success: false, message: "❌ 需要使用 filter() 函数\n\n格式：filter(函数, 列表)" };
                }

                if (!funcBody.includes('lambda')) {
                    return { success: false, message: "❌ filter 需要一个返回布尔值的函数\n\n提示：lambda x: x > threshold" };
                }

                if (!funcBody.includes('list(')) {
                    return { success: false, message: "❌ filter 返回迭代器，需要转换成列表\n\n提示：list(filter(...))" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回结果列表" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了 filter 函数。\n\n关键概念：\n• filter(函数, 可迭代对象) 筛选满足条件的元素\n• 函数返回 True 的元素被保留\n• 返回迭代器（惰性求值）\n• 需要用 list() 转换成列表\n\n🔍 filter vs 列表推导式：\n\nfilter 方式：\nlist(filter(lambda x: x > 100, prices))\n\n列表推导式：\n[x for x in prices if x > 100]\n\n区别：\n• 列表推导式更 Pythonic，可读性更好\n• filter 适合已有判断函数的情况\n• 列表推导式可以同时转换和筛选\n\n💡 实际应用：\n# 筛选有效数据\nvalid_prices = list(filter(lambda x: x > 0, prices))\n\n# 组合 map 和 filter\nresult = list(map(\n    lambda x: x * 2,\n    filter(lambda x: x > 100, prices)\n))"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    9: {
        title: "练习 9：函数作为参数",
        description: "高阶函数：接收函数作为参数",
        initialCode: `def apply_operation(prices, operation):
    # 对列表中每个元素应用 operation 函数
    # 提示：return [operation(price) for price in prices]
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def apply_operation\(prices, operation\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('for')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('operation(')) {
                    return { success: false, message: "❌ 需要调用 operation 函数\n\n提示：operation(price)" };
                }

                if (!funcBody.includes('for')) {
                    return { success: false, message: "❌ 需要遍历 prices 列表" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回结果列表" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了高阶函数的本质。\n\n关键概念：\n• 高阶函数：接收函数作为参数或返回函数\n• 函数是一等公民（first-class citizen）\n• 时间复杂度：O(n) - 遍历 + O(1) 函数调用\n• 实现了策略模式（strategy pattern）\n\n字节码分析：\ndef apply_operation(prices, operation):\n    return [operation(price) for price in prices]\n\n# 调用 operation(price)\n# LOAD_FAST (operation)  # 加载函数对象\n# LOAD_FAST (price)\n# CALL_FUNCTION (1)      # 调用函数\n\n函数对象传递：\ndef double(x):\n    return x * 2\n\napply_operation(prices, double)\n# LOAD_GLOBAL (apply_operation)\n# LOAD_FAST (prices)\n# LOAD_GLOBAL (double)   # 传递函数对象引用\n# CALL_FUNCTION (2)\n\n高阶函数的优势：\n• 代码复用：相同逻辑，不同操作\n• 解耦：操作与遍历分离\n• 可扩展：轻松添加新操作\n\n实际应用：\n• sorted(list, key=func)  # key 是高阶参数\n• map/filter/reduce\n• 装饰器（下一章）\n• 回调函数"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    10: {
        title: "练习 10：综合应用",
        description: "综合运用函数知识，创建股票分析工具",
        initialCode: `def analyze_stocks(stocks, min_price=100, operation=None):
    # stocks: 股票价格列表
    # min_price: 最低价格阈值（默认100）
    # operation: 可选的转换函数
    #
    # 返回字典：
    # - filtered: 价格 >= min_price 的股票
    # - transformed: 如果提供了 operation，对 filtered 应用该函数
    # - average: filtered 的平均价格
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def analyze_stocks\(stocks, min_price=100, operation=None\):([\s\S]*)/);
                if (!match) {
                    return { success: false, message: "❌ 函数定义不正确\n\n确保参数有默认值：min_price=100, operation=None" };
                }

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('return')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('filter') && !funcBody.includes('if ') && !funcBody.includes('>=')) {
                    return { success: false, message: "❌ 需要筛选价格 >= min_price 的股票" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回结果字典" };
                }

                const hasFiltered = funcBody.includes('"filtered"') || funcBody.includes("'filtered'");
                const hasTransformed = funcBody.includes('"transformed"') || funcBody.includes("'transformed'");
                const hasAverage = funcBody.includes('"average"') || funcBody.includes("'average'");

                if (!hasFiltered || !hasTransformed || !hasAverage) {
                    return {
                        success: false,
                        message: "❌ 返回的字典需要包含三个键：\n• filtered\n• transformed\n• average"
                    };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你完成了第 3 章的综合应用。\n\n关键概念：\n• 组合多个函数式编程技术\n• 默认参数 + 高阶函数 + 条件逻辑\n• 时间复杂度：O(n) - 单次遍历完成筛选和转换\n\n代码模式分析：\nfiltered = [s for s in stocks if s >= min_price]\ntransformed = [operation(s) for s in filtered] if operation else None\naverage = sum(filtered) / len(filtered) if filtered else 0\n\n优化建议：\n# 避免多次遍历\nfiltered = list(filter(lambda x: x >= min_price, stocks))\n# 使用生成器表达式节省内存\naverage = sum(s for s in stocks if s >= min_price) / len(filtered)\n\n函数式编程特点：\n• 声明式：描述做什么，而非怎么做\n• 不可变性：不修改输入数据\n• 组合性：小函数组合成大函数\n• 惰性求值：按需计算\n\n第 3 章总结：\n✓ PyFunctionObject 结构\n✓ LEGB 作用域规则\n✓ 参数传递机制（位置、默认、关键字）\n✓ lambda 表达式\n✓ map/filter 惰性求值\n✓ 高阶函数模式\n\n下一章：装饰器、闭包、生成器"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    }
};

// 当前练习索引
let currentExercise = 0;
const totalExercises = 10;
let completedExercises = new Set();

// 初始化
document.addEventListener('DOMContentLoaded', function() {
    updateProgress();

    document.querySelectorAll('.exercise-item').forEach((item, index) => {
        item.addEventListener('click', function() {
            switchExercise(index);
        });
    });
});

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

// 切换练习（保留兼容性）
function switchExercise(index) {
    loadExercise(index);
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
