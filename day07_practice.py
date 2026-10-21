# day07_practice.py 综合：默认参数 + 多返回值 + 字典/循环

def stats(txns, ttype="支出"):
    total = 0
    count = 0
    for row in txns:
        if row["类型"] == ttype:
            total = total + row["金额"]
            count = count + 1
    if count > 0:
        avg = total / count
    else:
        avg = 0            # 防止没有该类型时除以0
    return total, count, avg

txns = [
    {"类别": "餐饮", "类型": "支出", "金额": 35},
    {"类别": "工资", "类型": "收入", "金额": 8000},
    {"类别": "交通", "类型": "支出", "金额": 6},
    {"类别": "餐饮", "类型": "支出", "金额": 28},
    {"类别": "购物", "类型": "支出", "金额": 300},
    {"类别": "奖金", "类型": "收入", "金额": 2000},
]

# 统计支出（用默认参数）
e_total, e_count, e_avg = stats(txns)
print("支出：总额", e_total, " 笔数", e_count, " 平均", e_avg)

# 统计收入（第二个参数传"收入"）
i_total, i_count, i_avg = stats(txns, "收入")
print("收入：总额", i_total, " 笔数", i_count, " 平均", i_avg)