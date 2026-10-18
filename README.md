# 💻 100 天编程自学计划 · coding-100-days

> 从零基础到能独立写脚本、做数据分析与小项目的 100 天成长记录。
> **每天有代码、每天有提交（绿点）、每天有可运行的成果。**
> 起点：2026-10-15　|　主语言：Python　|　目标：2028 考研（人工智能 / 软件工程方向）

![Language](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Progress](https://img.shields.io/badge/进度-Day%204%2F100-2ea44f)
![Commits](https://img.shields.io/badge/连续打卡-4%20天-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows%2011-0078D4?logo=windows&logoColor=white)
![Editor](https://img.shields.io/badge/Editor-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)

---

## 📌 关于这个仓库

这是我从零开始系统学习编程的主仓库，记录**每天的学习代码、练习和真实项目拆解**。
我相信「**代码要每天写、项目要亲手跑、踩坑要记下来**」，所以这里没有复制粘贴的答案，只有自己敲过、运行过、调试过的代码。

学习主线：

```
Python 基础  →  文件 / CSV / Excel 自动化  →  pandas 数据分析  →  SQL
          →  数据结构与算法  →  机器学习 / 深度学习  →  真实项目 & 考研
```

---

## 🗂 仓库结构

```
coding-100-days/
├── day01_hello.py        # Day1 第一个程序 + Git/GitHub 环境
├── day02_type.py         # Day2 数据类型、运算、输入
├── day02_practice.py     # Day2 条件判断 if/else 练习
├── day03_list.py         # Day3 列表 list：下标/append/len/sum/max
├── day03_practice.py     # Day3 列表练习
├── day04_for.py          # Day4 for 循环、累加器、range
├── day04_practice.py     # Day4 循环统计练习（报销明细）
├── day04_csv.py          # Day4 用标准库 csv 读文件做财务统计
├── transactions.csv      # Day4 csv 练习用的交易数据
└── projects/
    └── day03_ledger/     # 小项目：命令行记账本
        ├── ledger.py
        └── records.json
```

---

## 📅 每日学习进度

| Day | 日期 | 主题 | 核心知识点 | 产出 | 状态 |
|---|---|---|---|---|---|
| 1 | 10-15 | 环境与起步 | 安装配置、VS Code、Git、注册 GitHub、运行第一个程序 | `day01_hello.py` | ✅ |
| 2 | 10-16 | 数据类型与条件 | int/float/str、类型转换、算术运算、`input()`、if/else | `day02_type.py` `day02_practice.py` | ✅ |
| 3 | 10-17 | 列表 list | 下标从 0 开始、`append`、`len/sum/max/min` | `day03_list.py` `day03_practice.py`、命令行记账本 | ✅ |
| 4 | 10-18 | for 循环 + CSV | 遍历、累加器/计数器、`range`、循环嵌套 if、打擂台求最值、标准库 `csv` 读文件统计 | `day04_for.py` `day04_practice.py` `day04_csv.py` `transactions.csv` | ✅ |
| 5 | … | 字典 dict、字符串 | 待更新 | — | ⏳ |

> 表格会随着每天的学习持续更新。

---

## 🛠 开发环境

| 工具 | 版本 / 说明 |
|---|---|
| 操作系统 | Windows 11 |
| Python | 3.13 |
| 编辑器 | Visual Studio Code |
| 版本控制 | Git 2.55 + GitHub |
| C++ 编译器 | MinGW-w64 GCC 16.2.0（为后续机试准备） |
| Java | Temurin JDK 21（考研后系统学习，当前仅了解） |

---

## 📚 学习方法

1. **每天一个小脚本**：当天知识点必须落成可运行的 `.py` 文件。
2. **先手写原理，再用现成函数**：比如先用循环手写累加，再去理解 `sum()` 内部做了什么。
3. **每天提交 GitHub**：保持绿点不断，用命令行 `add / commit / push` 全流程。
4. **真实项目拆解**：周末从 GitHub 挑真实开源项目，亲手 clone、跑通、改一行看变化。
5. **错题图文归档**：每个报错都记录「现象 → 原因 → 解决」，配截图，避免再踩。
6. **AI 当助教而非答案机**：用 ChatGPT / Claude 读报错、讲概念、出练习，但代码自己敲、结果自己验。

---

## 🚀 如何运行

确保已安装 Python 3，然后克隆并运行任意一天的脚本：

```bash
git clone https://github.com/797loy/coding-100-days.git
cd coding-100-days
python day04_csv.py
```

> 提示：脚本里若含中文输出，建议在 VS Code 集成终端中运行，避免部分输出面板的编码乱码。

---

## 🧭 14 个月总路线（2026.10 → 2027.12 初试）

| 阶段 | 时间 | 目标 |
|---|---|---|
| P0 环境与习惯 | 2026.10 | 装好软件、Git 提交、跑通第一个程序 |
| P1 Python 基础 | 2026.11–12 | 语法主干，能写百行内脚本处理文件和表格 |
| P2 数据分析 + 项目 1 | 2026.12–2027.01 | numpy / pandas，完成金融数据分析项目 |
| P3 寒假专项 | 2027.01–02 | SQL、数学一轮、机器学习预热 |
| P4 专业课 + ML | 2027.02–05 | 数据结构、C++、吴恩达 ML、确定院校 |
| P5 暑期强化 | 2027.05–08 | 专业课二轮、深度学习、简历项目 2 |
| P6–P7 冲刺 | 2027.08–12 | 真题、模考、政治，走上考场 |

---

## 📝 备注

- 本仓库为个人学习记录，代码以「清晰、能跑、能讲清楚」为第一目标。
- 如有错误或更好的写法，欢迎在 Issues 里交流指正。
- 金融 / 审计 / AI 是我最感兴趣的应用方向，后续项目会尽量围绕真实数据场景展开。

⭐ 如果这份循序渐进的自学记录对你也有启发，欢迎点个 Star 一起进步！