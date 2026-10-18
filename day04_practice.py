expense=[120,45,300,88,60,210,75]

# 第一题：算总额和平均
# 用循环累加求总额；再用 总额 / 笔数 求平均。
total=0
for amount in expense:
    total+=amount
average=total/len(expense)
print("总额：",total)
print("平均：",round(average, 2))

# 第二题：统计“大额支出”有几笔
# 规定 **超过 100（含 100 以上，即 >=100）算大额**，用循环数出来有几笔、分别是多少。
big_count=0
for amount in expense:
    if amount>=100:
        big_count+=1
        print("大额支出：",amount)
print("大额支出笔数：",big_count)


# 第三题：print("大额支出：",amount)

biggest=expense[0]
for amount in expense:
    if amount>biggest:
        biggest=amount
print("最大支出：",biggest)
