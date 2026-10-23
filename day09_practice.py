# day09_practice.py 练习②：追加模式 a + 文件指针

# 第1个with：只数原文件有几行
with open("accounts.txt", "r", encoding="utf-8") as f:
    print("原行数：", len(f.readlines()))

# 第2个with：用 a 追加2行（不清空原内容）
with open("accounts.txt", "a", encoding="utf-8") as f1:
    f1.write("娱乐,50\n")
    f1.write("学习,0\n")

# 第3个with：重新打开，只做逐行循环累加（这里不能再readlines，否则指针到末尾读不到）
total = 0
count = 0
with open("accounts.txt", "r", encoding="utf-8") as f2:
    for line in f2:
        i = line.strip().split(",")
        amount = int(i[1])
        total = total + amount
        count = count + 1
        print("类别：", i[0], " 金额：", amount)

print("追加后行数：", count)
print("总金额：", total)
