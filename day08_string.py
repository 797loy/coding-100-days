# day08_string.py 字符串：切片/查找/分割/替换/互转

s="adcdef"
print(s[0],s[-1])
print(s[0:3],s[3:])

line ="2026-10-01,餐饮,支出,35"
parts=line.split(",")
print("切出来：",parts)
print("类别是：",parts[1])

amount=int(parts[3])
print("加10元后：",amount+10)

print("包含'支出'吗：","支出"in line)
print("'收入'的位置是：",line.find("收入"))

msg=" 本月餐饮很多 "
print("去空格：",msg.strip())
print("替换：",msg.strip().replace("很多","偏多"))

# join：把列表拼回字符串
names=["餐饮","交通","购物"]
print("、".join(names))