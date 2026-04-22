# 第1章剩余练习更新指南

## 练习 3：索引访问

### 添加知识框
```html
<div class="knowledge-box">
    <h4>🔍 深入理解：索引机制</h4>
    <p><strong>索引本质：</strong>指针偏移量</p>
    <pre><code># 内存布局
list = [obj1, obj2, obj3]
# 实际存储：[ptr1, ptr2, ptr3]

# 索引访问
list[2]  # 等价于：*(ob_item + 2 * sizeof(PyObject*))

# 负索引
list[-1]  # 等价于：list[len(list) - 1]

# 时间复杂度
# 正索引：O(1) - 直接计算地址
# 负索引：O(1) - 先计算 len，再偏移</code></pre>
</div>
```

---

## 练习 4：字典修改

### 添加知识框
```html
<div class="knowledge-box">
    <h4>🔍 深入理解：字典的原地修改</h4>
    <p><strong>可变对象的特性：</strong></p>
    <pre><code># 原地修改不改变对象 id
d = {"price": 100}
print(id(d))  # 例如：140234567890

d["price"] = 200
print(id(d))  # 相同的地址

# 对比：不可变对象
t = (1, 2, 3)
# t[0] = 99  # TypeError: 不支持修改

# 字典修改的内部过程
# 1. hash("price") -> 哈希值
# 2. 定位槽位（不需要重新哈希）
# 3. 更新值指针
# 4. 不改变字典结构</code></pre>
</div>
```

---

## 练习 5：元组

### 添加知识框
```html
<div class="knowledge-box">
    <h4>🔍 深入理解：元组的不可变性</h4>
    <p><strong>不可变 vs 可变：</strong></p>
    <pre><code># 元组的内存结构
typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];  // 固定大小
} PyTupleObject;

# 不可变的含义
t = (1, 2, 3)
# t[0] = 99  # TypeError

# 但元组可以包含可变对象
t = ([1, 2], [3, 4])
t[0].append(99)  # ✓ 可以修改列表内容
# t[0] = [5, 6]  # ✗ 不能替换引用

# 元组的优势
# 1. 可哈希 -> 可作为 dict key
# 2. 内存效率高（无扩容开销）
# 3. 线程安全
# 4. 解释器优化（小元组缓存）</code></pre>
</div>
```

---

## 练习 6：列表 append

### 添加知识框
```html
<div class="knowledge-box">
    <h4>🔍 深入理解：动态扩容</h4>
    <p><strong>CPython 扩容策略：</strong></p>
    <pre><code># 扩容公式
new_allocated = (n + (n >> 3) + 6) & ~3

# 扩容序列
n=0  -> 4
n=4  -> 8
n=8  -> 16
n=16 -> 24
n=24 -> 32

# 为什么平摊 O(1)？
# 假设从 0 append 到 n：
# - 扩容次数：log(n)
# - 总拷贝次数：n + n/2 + n/4 + ... ≈ 2n
# - 平均每次 append：2n/n = O(1)

# 对比其他策略
# 每次 +1：O(n²) 总时间
# 每次 ×2：浪费空间
# CPython：平衡时间和空间</code></pre>
</div>
```

---

## 练习 7：字典访问

### 添加知识框
```html
<div class="knowledge-box">
    <h4>🔍 深入理解：哈希查找</h4>
    <p><strong>查找过程：</strong></p>
    <pre><code># 1. 计算哈希值
h = hash(key)

# 2. 计算初始索引
index = h & (table_size - 1)  # 等价于 h % table_size

# 3. 处理冲突（开放寻址）
while True:
    entry = table[index]
    if entry.key == key:
        return entry.value
    if entry is EMPTY:
        raise KeyError
    # 探测下一个位置
    index = (index * 5 + 1) & mask

# 时间复杂度
# 平均：O(1)
# 最坏：O(n) - 所有键冲突（极少）

# 负载因子控制
# 当 used/size > 2/3 时 resize
# 保证查找效率</code></pre>
</div>
```

---

## 练习 8：len 函数

### 添加知识框
```html
<div class="knowledge-box">
    <h4>🔍 深入理解：序列协议</h4>
    <p><strong>len() 的实现：</strong></p>
    <pre><code># CPython 实现
Py_ssize_t PyObject_Size(PyObject *o) {
    PySequenceMethods *m = o->ob_type->tp_as_sequence;
    if (m && m->sq_length)
        return m->sq_length(o);
    // ...
}

# 对于列表
static Py_ssize_t list_length(PyListObject *a) {
    return Py_SIZE(a);  // 直接返回 ob_size 字段
}

# 时间复杂度：O(1)
# 不需要遍历，直接读取字段

# 序列协议方法
__len__()      # 长度
__getitem__()  # 索引读取
__setitem__()  # 索引赋值
__delitem__()  # 删除元素
__contains__() # in 运算符
__iter__()     # 迭代器</code></pre>
</div>
```

---

## 总结

所有练习都需要：
1. 添加"深入理解"知识框
2. 展示 CPython 实现细节
3. 说明时间/空间复杂度
4. 对比不同实现方式

这样可以让学习者真正理解底层原理，而不只是记住语法。
