# 命令行记账本（第一次项目拆解 · L0）
# 只用 Python 标准库 json，不需要 pip 安装任何东西
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "records.json")


# 读取已保存的账单；第一次运行文件不存在，就返回空列表
def load_records():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# 把账单写回 records.json，这样关掉程序数据也不丢
def save_records(records):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


# 添加一笔记录
def add_record(records):
    kind = input("类型（收入/支出）：").strip()
    category = input("类别（如 工资/餐饮/交通）：").strip()
    amount = float(input("金额："))
    month = input("月份（如 2026-10）：").strip()
    note = input("备注（可留空）：").strip()

    records.append({
        "kind": kind,
        "category": category,
        "amount": amount,
        "month": month,
        "note": note,
    })
    save_records(records)
    print("已记录成功！")


# 列出全部记录
def list_records(records):
    if not records:
        print("还没有任何记录。")
        return
    print("-" * 40)
    for i, r in enumerate(records, start=1):
        print(i, r["month"], r["kind"], r["category"], r["amount"], r["note"])
    print("-" * 40)


# 按"类型 + 类别"汇总
def summary(records):
    total_income = 0.0
    total_expense = 0.0
    by_category = {}

    for r in records:
        if r["kind"] == "收入":
            total_income += r["amount"]
        else:
            total_expense += r["amount"]
            by_category[r["category"]] = by_category.get(r["category"], 0) + r["amount"]

    print("========== 汇总 ==========")
    print("总收入：", total_income)
    print("总支出：", total_expense)
    print("结余：", total_income - total_expense)
    print("--- 支出分类 ---")
    for cat, money in by_category.items():
        print(cat, "：", money)


# 主菜单：一直循环，直到用户选 4 退出
def main():
    records = load_records()
    while True:
        print("\n===== 我的记账本 =====")
        print("1. 记一笔")
        print("2. 查看全部")
        print("3. 查看汇总")
        print("4. 退出")
        choice = input("请选择（1-4）：").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            list_records(records)
        elif choice == "3":
            summary(records)
        elif choice == "4":
            print("再见！数据已保存。")
            break
        else:
            print("输入无效，请选 1-4。")


if __name__ == "__main__":
    main()