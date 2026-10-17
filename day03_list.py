#一个购物清单，用一个名字装了三个东西
shopping=["牛奶","面包","鸡蛋"]
print(shopping)

amount=[35,6,8000,12.5]
print(amount)

shopping=["牛奶","面包","鸡蛋"]
print(shopping[0]) #第一个
print(shopping[1]) #第二个
print(shopping[2]) #第三个

shopping=["牛奶","鸡蛋"]
shopping.append("苹果") #在末尾添加一个元素
print(shopping)

amounts=[35,6,8000,12.5]
print(len(amounts)) #列表长度,即元素的个数
print(sum(amounts)) #列表元素求和,全部加起来
print(max(amounts)) #列表元素最大值
print(min(amounts)) #列表元素最小值
