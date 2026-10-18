#day04_for.py学习for循环遍历列表
expense=[35,6,28,50,12]

#1)遍历：把每一笔都打印出来
print("===每一笔支出===")
for amount in expense:
    print("一笔支出：",amount)

#2)累加器：自己算总额（不使用sum，理解循环原理）
total=0
for amount in expense:
    total=total+amount
print("循环算出的总额：",total)
print("用sum验算：",sum(expense))

#3)边遍历边计数，统计有几笔
count=0
for amount in expense:
    count=count+1
print("循环算出的笔数：",count)
print("用len验算：",len(expense))

# 4)range:让数字按规律跑一遍
print("===range(5)生成0到4===")
for i in range(5):
    print(i)

print("===range(1,6)生成1到5===")
for i in range(1,6):
    print(i)

# 5)用下标遍历：range+len组合（重要写法）
print("===按下标遍历===")
for i in range(len(expense)):
    print("第",i+1,"笔是",expense[i])

