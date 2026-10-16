#三种最基本的数据类型
age=22       #int整数类型，没有小数点的数字
height=1.76  #float浮点类型，带小数点的数字
name="南宫子玉"  #str字符串类型，文字，必须加引号

#type（）可以查看一个变量是什么类型
print(type(age))    #<class 'int'>
print(type(height)) #<class 'float'>
print(type(name))   #<class 'str'>

#整数和小数可以直接做运算
a=10
b=3

print(a+b)  #加法
print(a-b)  #减法
print(a*b)  #乘法
print(a/b)  #除法，结果是小数
print(a//b) #整除，结果是整数
print(a%b)  #取余，结果是整数
print(a**b) #幂运算，结果是整数

#情况一：数字相加
x=100
y=200
print(x+y)  #结果是整数

#情况二：文字“相加”其实是拼接
s1="100"
s2="200"
print(s1+s2)  #结果是字符串

s="100"
n=int(s)  #把字符串转换为整数
print(n+1)  #结果是整数

f=float("3.14")  #把字符串转换为小数
print(f*2)  #结果是小数

#input（）函数可以让用户输入数据，输入的数据都是字符串类型
name=input("请输入你的名字：")
print("你好，" + name + "，欢迎回来！")
money=input("请输入本月工资：")
money=int(money)  #把字符串转换为整数
print("你今年预计总收入为：",money*12)
