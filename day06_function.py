def say_hi():
    print("你好，欢迎学函数")

say_hi()
say_hi()

def show_expense(category,amount):
    print("一笔"+category+"支出",amount)
show_expense("餐饮",35)
show_expense("购物",300)
def add(a,b):
    return a+b

total=add(120,80)
print("120+80=", total)

# 4) 小练习函数：算平均（结合你昨天的财务场景）
def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

print("平均：", average([120, 45, 300, 88]))