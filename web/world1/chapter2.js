// 第2章练习数据和测试逻辑

const exercises = {
    1: {
        title: "练习 1：for 循环基础",
        description: "使用 for 循环计算所有价格的总和",
        initialCode: `def calculate_total(prices):
    # 在这里写你的代码
    # 提示：创建 total = 0，然后用 for 循环累加
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def calculate_total\(prices\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('for')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要使用 for 循环" };
                }

                if (!funcBody.includes('for')) {
                    return { success: false, message: "❌ 需要使用 for 循环遍历 prices\n\n格式：for price in prices:" };
                }

                if (!funcBody.includes('total') && !funcBody.includes('sum')) {
                    return { success: false, message: "❌ 需要创建一个变量来累加总和\n\n提示：total = 0" };
                }

                if (!funcBody.includes('+=') && !funcBody.includes('= total +') && !funcBody.includes('= sum +')) {
                    return { success: false, message: "❌ 需要在循环中累加\n\n提示：total += price" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回总和\n\n添加：return total" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了 for 循环的迭代机制。\n\n关键概念：\n• for 循环基于迭代器协议（__iter__ 和 __next__）\n• 时间复杂度：O(n) - 遍历所有元素\n• 累加操作：total += x 等价于 total = total + x\n\n字节码优化：\nfor 循环比 while 更高效：\n• GET_ITER：一次性获取迭代器\n• FOR_ITER：优化的迭代指令\n• 避免重复的条件检查\n\n迭代器协议：\niter(obj) -> 调用 obj.__iter__()\nnext(it) -> 调用 it.__next__()\nStopIteration -> 迭代结束"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    2: {
        title: "练习 2：while 循环",
        description: "使用 while 循环从 1 数到 n",
        initialCode: `def count_to_n(n):
    # 在这里写你的代码
    # 提示：使用 while count <= n
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def count_to_n\(n\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('while')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要使用 while 循环" };
                }

                if (!funcBody.includes('while')) {
                    return { success: false, message: "❌ 需要使用 while 循环\n\n格式：while count <= n:" };
                }

                if (!funcBody.includes('count') && !funcBody.includes('i')) {
                    return { success: false, message: "❌ 需要创建计数器变量\n\n提示：count = 1" };
                }

                if (!funcBody.includes('append')) {
                    return { success: false, message: "❌ 需要将数字添加到列表中\n\n提示：result.append(count)" };
                }

                if (!funcBody.includes('+=') && !funcBody.includes('= count + 1') && !funcBody.includes('= i + 1')) {
                    return { success: false, message: "❌ 别忘了递增计数器，否则会无限循环！\n\n提示：count += 1" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回结果列表" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了 while 循环机制。\n\n关键概念：\n• while 循环每次迭代前检查条件\n• 必须手动更新循环变量（避免无限循环）\n• 适合不确定迭代次数的场景\n\n字节码结构：\n1. LOAD_NAME (count)\n2. LOAD_CONST (n)\n3. COMPARE_OP (<=)\n4. POP_JUMP_IF_FALSE (exit)\n5. ... 循环体 ...\n6. JUMP_ABSOLUTE (step 1)\n\nfor vs while：\n• for：迭代已知序列（更快）\n• while：条件驱动（更灵活）\n• for 有迭代器优化\n• while 每次都要检查条件"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    3: {
        title: "练习 3：if 条件判断",
        description: "判断价格是否大于阈值",
        initialCode: `def is_high_price(price, threshold):
    # 在这里写你的代码
    # 提示：if price > threshold: return True
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def is_high_price\(price, threshold\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('if')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要使用 if 判断" };
                }

                if (!funcBody.includes('if')) {
                    return { success: false, message: "❌ 需要使用 if 条件判断\n\n格式：if price > threshold:" };
                }

                if (!funcBody.includes('>')) {
                    return { success: false, message: "❌ 需要比较价格和阈值\n\n使用 > 运算符" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回 True 或 False" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了条件判断的布尔求值。\n\n关键概念：\n• 比较运算符返回布尔对象（True/False）\n• Python 中 True/False 是单例对象\n• 布尔值是 int 的子类（True == 1, False == 0）\n\n字节码：\nLOAD_NAME (price)\nLOAD_NAME (threshold)\nCOMPARE_OP (>)\nRETURN_VALUE\n\n短路求值：\nand：左侧为 False 时不求值右侧\nor：左侧为 True 时不求值右侧\n\n真值测试：\n• 假值：False, None, 0, \"\", [], {}, ()\n• 其他都是真值\n• 自定义类可实现 __bool__() 或 __len__()"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    4: {
        title: "练习 4：if-elif-else",
        description: "根据价格分类（高/中/低）",
        initialCode: `def categorize_price(price):
    # 在这里写你的代码
    # 提示：使用 if-elif-else
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def categorize_price\(price\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('if')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('if')) {
                    return { success: false, message: "❌ 需要使用 if 判断" };
                }

                if (!funcBody.includes('elif') && !funcBody.includes('else if')) {
                    return { success: false, message: "❌ 需要使用 elif 处理多个条件\n\n格式：elif price >= 100:" };
                }

                if (!funcBody.includes('else')) {
                    return { success: false, message: "❌ 需要使用 else 处理其他情况" };
                }

                const hasHigh = funcBody.includes('"高价股"') || funcBody.includes("'高价股'");
                const hasMid = funcBody.includes('"中价股"') || funcBody.includes("'中价股'");
                const hasLow = funcBody.includes('"低价股"') || funcBody.includes("'低价股'");

                if (!hasHigh || !hasMid || !hasLow) {
                    return {
                        success: false,
                        message: "❌ 需要返回正确的分类\n\n• >= 200: 返回 \"高价股\"\n• >= 100: 返回 \"中价股\"\n• < 100: 返回 \"低价股\""
                    };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了多分支条件判断。\n\n关键概念：\n• if-elif-else 实现多路分支\n• 从上到下依次检查，匹配第一个为真的分支\n• 只执行一个分支（互斥）\n\n字节码结构：\nLOAD_NAME (price)\nLOAD_CONST (200)\nCOMPARE_OP (>=)\nPOP_JUMP_IF_FALSE (elif_block)\n... if 块 ...\nJUMP_FORWARD (end)\nelif_block:\nLOAD_NAME (price)\nLOAD_CONST (100)\nCOMPARE_OP (>=)\nPOP_JUMP_IF_FALSE (else_block)\n... elif 块 ...\nJUMP_FORWARD (end)\nelse_block:\n... else 块 ...\nend:\n\n优化建议：\n• 将最常见的条件放在前面\n• 减少不必要的比较"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    5: {
        title: "练习 5：循环 + 条件",
        description: "筛选出大于阈值的价格",
        initialCode: `def filter_high_prices(prices, threshold):
    # 在这里写你的代码
    # 提示：结合 for 循环和 if 判断
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def filter_high_prices\(prices, threshold\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('for')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('for')) {
                    return { success: false, message: "❌ 需要使用 for 循环遍历 prices" };
                }

                if (!funcBody.includes('if')) {
                    return { success: false, message: "❌ 需要使用 if 判断价格是否大于阈值" };
                }

                if (!funcBody.includes('append')) {
                    return { success: false, message: "❌ 需要将符合条件的价格添加到结果列表\n\n提示：result.append(price)" };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回结果列表" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了循环与条件的组合。\n\n关键概念：\n• 循环内的条件判断实现过滤\n• 时间复杂度：O(n) - 遍历 + O(1) 判断\n• 空间复杂度：O(k) - k 为满足条件的元素数\n\n字节码分析：\nGET_ITER\nFOR_ITER\nSTORE_NAME (price)\nLOAD_NAME (price)\nLOAD_NAME (threshold)\nCOMPARE_OP (>)\nPOP_JUMP_IF_FALSE (FOR_ITER)\nLOAD_NAME (result)\nLOAD_METHOD (append)\nLOAD_NAME (price)\nCALL_METHOD\nJUMP_ABSOLUTE (FOR_ITER)\n\n性能考虑：\n• append 是 O(1) 平摊\n• 总体 O(n) 线性时间\n• 下一题会学习更高效的写法"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    6: {
        title: "练习 6：列表推导式",
        description: "用列表推导式筛选价格（一行代码）",
        initialCode: `def filter_with_comprehension(prices, threshold):
    # 在这里写你的代码
    # 提示：return [price for price in prices if price > threshold]
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def filter_with_comprehension\(prices, threshold\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('[')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('[') || !funcBody.includes('for')) {
                    return { success: false, message: "❌ 需要使用列表推导式\n\n格式：[表达式 for 变量 in 列表 if 条件]" };
                }

                if (!funcBody.includes('if')) {
                    return { success: false, message: "❌ 列表推导式中需要 if 条件筛选" };
                }

                // 检查是否是一行代码（不包含多个语句）
                const lines = funcBody.trim().split('\n').filter(line => line.trim() && !line.trim().startsWith('#'));
                if (lines.length > 1) {
                    return {
                        success: false,
                        message: "❌ 列表推导式应该是一行代码\n\n提示：return [price for price in prices if price > threshold]"
                    };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了列表推导式的优化。\n\n关键概念：\n• 列表推导式是语法糖，但有字节码优化\n• 时间复杂度：O(n) - 与循环相同\n• 空间复杂度：O(k) - 预分配结果列表\n\n字节码对比：\n传统循环：\n  BUILD_LIST (0)\n  GET_ITER\n  FOR_ITER\n  ... 条件判断 ...\n  LIST_APPEND\n  JUMP_ABSOLUTE\n\n列表推导式：\n  BUILD_LIST (0)\n  LOAD_FAST (.0)  # 优化的迭代器\n  FOR_ITER\n  ... 条件判断 ...\n  LIST_APPEND (1)  # 直接追加\n  JUMP_ABSOLUTE\n\n性能优势：\n• 减少 LOAD_NAME 指令\n• 使用 LOAD_FAST（局部变量更快）\n• 编译器优化：预估大小、减少扩容\n• 实测快 10-30%"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    7: {
        title: "练习 7：enumerate 函数",
        description: "使用 enumerate 同时获取索引和值",
        initialCode: `def get_stock_with_index(stocks):
    # 在这里写你的代码
    # 提示：使用 enumerate(stocks)
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def get_stock_with_index\(stocks\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('enumerate')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要使用 enumerate" };
                }

                if (!funcBody.includes('enumerate')) {
                    return { success: false, message: "❌ 需要使用 enumerate() 函数\n\n格式：for index, stock in enumerate(stocks):" };
                }

                if (!funcBody.includes('for')) {
                    return { success: false, message: "❌ 需要使用 for 循环遍历" };
                }

                if (!funcBody.includes('append')) {
                    return { success: false, message: "❌ 需要将结果添加到列表\n\n提示：result.append(f\"{index}: {stock}\")" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了 enumerate 的迭代器组合。\n\n关键概念：\n• enumerate() 返回 enumerate 对象（迭代器）\n• 每次迭代产生 (index, value) 元组\n• 时间复杂度：O(n) - 单次遍历\n• 空间复杂度：O(1) - 惰性求值\n\n底层实现：\nclass enumerate:\n    def __init__(self, iterable, start=0):\n        self.iter = iter(iterable)\n        self.count = start\n    \n    def __iter__(self):\n        return self\n    \n    def __next__(self):\n        value = next(self.iter)\n        result = (self.count, value)\n        self.count += 1\n        return result\n\n迭代器组合：\n• enumerate 包装原始迭代器\n• 不创建新列表（内存高效）\n• 支持任意可迭代对象\n\n对比手动计数：\ni = 0\nfor stock in stocks:\n    # 需要手动 i += 1\n# enumerate 自动管理索引"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    8: {
        title: "练习 8：zip 函数",
        description: "使用 zip 同时遍历多个列表",
        initialCode: `def combine_stock_price(tickers, prices):
    # 在这里写你的代码
    # 提示：使用 zip(tickers, prices)
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def combine_stock_price\(tickers, prices\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('zip')) {
                    return { success: false, message: "❌ 你还没有实现函数，需要使用 zip" };
                }

                if (!funcBody.includes('zip')) {
                    return { success: false, message: "❌ 需要使用 zip() 函数\n\n格式：for ticker, price in zip(tickers, prices):" };
                }

                if (!funcBody.includes('for')) {
                    return { success: false, message: "❌ 需要使用 for 循环遍历" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了 zip 的惰性求值机制。\n\n关键概念：\n• zip() 返回 zip 对象（迭代器）\n• 惰性求值：按需生成元组，不预先创建列表\n• 时间复杂度：O(min(n, m)) - 以最短序列为准\n• 空间复杂度：O(1) - 不存储中间结果\n\n底层实现：\nclass zip:\n    def __init__(self, *iterables):\n        self.iters = [iter(it) for it in iterables]\n    \n    def __iter__(self):\n        return self\n    \n    def __next__(self):\n        return tuple(next(it) for it in self.iters)\n        # 任一迭代器耗尽时抛出 StopIteration\n\n长度不等时的行为：\nlist1 = [1, 2, 3]\nlist2 = ['a', 'b']\nlist(zip(list1, list2))  # [(1, 'a'), (2, 'b')]\n# 以最短的为准，不会报错\n\n严格模式（Python 3.10+）：\nfrom itertools import zip_longest\nzip_longest(list1, list2, fillvalue=None)\n# 填充缺失值到最长序列"
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    9: {
        title: "练习 9：嵌套循环",
        description: "使用嵌套循环生成所有组合",
        initialCode: `def generate_pairs(list1, list2):
    # 在这里写你的代码
    # 提示：使用两层 for 循环
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def generate_pairs\(list1, list2\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('for')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                // 计算 for 出现的次数
                const forCount = (funcBody.match(/\bfor\b/g) || []).length;
                if (forCount < 2) {
                    return { success: false, message: "❌ 需要使用嵌套循环（两层 for 循环）\n\n格式：\nfor item1 in list1:\n    for item2 in list2:" };
                }

                if (!funcBody.includes('append')) {
                    return { success: false, message: "❌ 需要将配对添加到结果列表" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你掌握了嵌套循环的复杂度分析。\n\n关键概念：\n• 嵌套循环生成笛卡尔积（所有组合）\n• 时间复杂度：O(n × m) - n 和 m 分别是两个列表长度\n• 空间复杂度：O(n × m) - 存储所有配对\n\n字节码结构：\nGET_ITER (list1)          # 外层迭代器\nFOR_ITER (outer_loop)\n  STORE_NAME (item1)\n  GET_ITER (list2)        # 内层迭代器（每次重新创建）\n  FOR_ITER (inner_loop)\n    STORE_NAME (item2)\n    ... 处理 (item1, item2) ...\n    JUMP_ABSOLUTE (inner_loop)\n  JUMP_ABSOLUTE (outer_loop)\n\n性能考虑：\n• 外层 n 次，内层每次 m 次 → 总共 n×m 次\n• 避免不必要的嵌套（考虑哈希表优化）\n• 三层嵌套 → O(n³)，谨慎使用\n\n优化示例：\n# 不好：O(n²)\nfor x in list1:\n    for y in list2:\n        if x == y: ...\n\n# 更好：O(n)\nset2 = set(list2)\nfor x in list1:\n    if x in set2: ..."
                };
            } catch (e) {
                return { success: false, message: `❌ 代码错误：${e.message}` };
            }
        }
    },
    10: {
        title: "练习 10：综合应用",
        description: "综合运用循环和条件，分析股票数据",
        initialCode: `def analyze_portfolio(stocks):
    # stocks 是一个字典列表，每个字典包含 ticker, price, shares
    # 返回一个字典，包含：
    # - total_value: 总价值
    # - high_value_stocks: 价值 > 10000 的股票代码列表
    # - stock_count: 股票数量
    pass`,
        test: function(code) {
            try {
                const match = code.match(/def analyze_portfolio\(stocks\):([\s\S]*)/);
                if (!match) return { success: false, message: "❌ 找不到函数定义" };

                const funcBody = match[1];
                if (funcBody.includes('pass') && !funcBody.includes('for')) {
                    return { success: false, message: "❌ 你还没有实现函数" };
                }

                if (!funcBody.includes('for')) {
                    return { success: false, message: "❌ 需要使用 for 循环遍历 stocks" };
                }

                if (!funcBody.includes('if')) {
                    return { success: false, message: "❌ 需要使用 if 判断筛选高价值股票" };
                }

                const hasTotal = funcBody.includes('total_value') || funcBody.includes('"total_value"');
                const hasHighValue = funcBody.includes('high_value_stocks') || funcBody.includes('"high_value_stocks"');
                const hasCount = funcBody.includes('stock_count') || funcBody.includes('"stock_count"');

                if (!hasTotal || !hasHighValue || !hasCount) {
                    return {
                        success: false,
                        message: "❌ 返回的字典需要包含三个键：\n• total_value\n• high_value_stocks\n• stock_count"
                    };
                }

                if (!funcBody.includes('return')) {
                    return { success: false, message: "❌ 需要返回结果字典" };
                }

                return {
                    success: true,
                    message: "✅ 测试通过！\n\n你完成了第 2 章的综合应用。\n\n关键概念：\n• 组合使用循环、条件、累加、筛选\n• 时间复杂度：O(n) - 单次遍历\n• 空间复杂度：O(k) - k 为高价值股票数\n\n代码模式分析：\ntotal = 0\nhigh_value = []\nfor stock in stocks:\n    value = stock['price'] * stock['shares']\n    total += value  # 累加\n    if value > 10000:  # 条件筛选\n        high_value.append(stock['ticker'])\n\n字节码优化建议：\n• 使用局部变量缓存字典访问\n• 避免重复计算（如 price * shares）\n• 考虑列表推导式（但需权衡可读性）\n\n实际应用：\n• 投资组合分析\n• 数据聚合和筛选\n• 报表生成\n\n下一章预告：\n第 3 章将学习函数对象、闭包、装饰器等高级特性，\n深入理解 Python 的函数式编程能力。"
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

    // 绑定侧边栏点击事件
    document.querySelectorAll('.exercise-item').forEach((item, index) => {
        item.addEventListener('click', function() {
            switchExercise(index);
        });
    });
});

// 切换练习
function switchExercise(index) {
    document.querySelectorAll('.lesson-content').forEach(content => {
        content.classList.remove('active');
    });

    document.getElementById(`lesson-${index}`).classList.add('active');

    document.querySelectorAll('.exercise-item').forEach(item => {
        item.classList.remove('active');
    });
    document.querySelector(`[data-exercise="${index}"]`).classList.add('active');

    currentExercise = index;
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
