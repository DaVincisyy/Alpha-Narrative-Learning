# Web 文件结构说明

## 📁 新的文件结构

```
web/
├── index.html              # 🏠 主入口 - 选择学习世界
│
├── world1/                 # 🌱 世界1：Python基础村
│   ├── index.html          # 世界1入口（章节列表）
│   ├── chapter1.html       # 第1章：数据容器
│   ├── chapter1.js
│   ├── chapter2.html       # 第2章：循环与条件
│   ├── chapter2.js
│   ├── chapter3.html       # 第3章：函数与模块
│   ├── chapter3.js
│   ├── chapter4.html       # 第4章：文件操作与异常处理
│   ├── chapter4.js
│   ├── chapter5.html       # 第5章：面向对象编程
│   └── chapter5.js
│
├── world2/                 # 📊 世界2：Pandas数据王国（待创建）
├── world3/                 # 🧠 世界3：NLP魔法学院（待创建）
├── world4/                 # 📈 世界4：量化分析城（待创建）
├── world5/                 # 🚀 世界5：实战项目岛（待创建）
│
└── static/                 # 静态资源（待使用）
    ├── css/
    └── js/
```

## 🚀 如何使用

### 方式1：直接打开文件
1. 打开 `web/index.html` - 主入口页面
2. 点击"世界1：Python基础村"
3. 进入世界1，选择章节学习

### 方式2：启动本地服务器
```bash
cd web
python -m http.server 8000
# 然后访问 http://localhost:8000
```

## 📝 文件说明

### 主入口（index.html）
- 展示所有5个学习世界
- 显示每个世界的章节数、练习数、预计时间
- 世界1可点击，其他世界显示"即将推出"

### 世界入口（world1/index.html）
- 展示该世界的所有章节
- 显示学习进度
- 点击章节卡片进入学习

### 章节页面（chapter*.html）
- 左侧：练习列表
- 右侧：课程内容和代码编辑器
- 顶部：返回世界入口的按钮
- 底部：上一题/下一题导航

## 🎯 优势

1. **清晰的层级结构**
   - index.html → world1/index.html → chapter1.html
   - 用户一眼就知道从哪里开始

2. **模块化设计**
   - 每个世界独立文件夹
   - 便于管理和扩展

3. **易于维护**
   - 所有章节文件集中在对应世界文件夹
   - 添加新世界只需创建新文件夹

4. **路径简洁**
   - 相对路径清晰：`chapter1.html`、`index.html`
   - 不需要复杂的路径跳转

## 🔄 迁移说明

已完成的迁移：
- ✅ 创建新的目录结构
- ✅ 移动所有world1的HTML和JS文件
- ✅ 更新所有链接（返回按钮、章节链接）
- ✅ 创建新的主入口页面

## 📋 待办事项

- [ ] 创建world2、3、4、5的内容
- [ ] 提取公共CSS到static/css/styles.css
- [ ] 添加进度保存功能（localStorage）
- [ ] 添加主题切换功能
