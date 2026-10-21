# day07_function2.py 函数进阶：默认参数、多返回值、作用域

# 1) 默认参数
def greet(name,word="你好"):
    print(word+","+name)

greet("小明")  # 默认参数
greet("小红","早上好")  # 指定参数

# 2) 多返回值：一笔函数算出 总额、笔数、平均
def summary(numbers):
    total=0
    for n in numbers:
        total+=n
    return total,len(numbers),total/len(numbers)

t, cnt, avg = summary([35, 6, 28, 300])
print("总额：", t, " 笔数：", cnt, " 平均：", avg)

# 3) 默认参数 + 只统计指定类型
txns = [
    {"类型": "支出", "金额": 35},
    {"类型": "收入", "金额": 8000},
    {"类型": "支出", "金额": 28},
]

def total_amount(rows, ttype="支出"):
    s = 0
    for r in rows:
        if r["类型"] == ttype:
            s += r["金额"]
    return s

print("总支出：", total_amount(txns))            # 用默认值
print("总收入：", total_amount(txns, "收入"))    # 改传"收入"