# day04_csv.py 用 Python 自带的 csv 库读取交易文件并统计（不装任何第三方库）
import csv

income = 0      # 收入累加器
expense = 0     # 支出累加器

# open 打开文件；encoding="utf-8-sig" 能兼容带表头标记的csv，避免中文/首列出错
with open("transactions.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)   # DictReader：把每一行变成"字典"，用列名取值

    for row in reader:                       # 一次循环处理一行，和今天学的 for 一模一样
        amount = float(row["金额"])          # 取"金额"列，从文字转成数字
        kind = row["类型"]                   # 取"类型"列：收入 或 支出
        category = row["类别"]

        if kind == "收入":
            income = income + amount
        else:
            expense = expense + amount
            if category == "餐饮":           # 顺手统计餐饮花了多少
                print("一笔餐饮支出：", amount)

print("总收入：", income)
print("总支出：", expense)
print("结余：", income - expense)

