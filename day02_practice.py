month_money=input("请输入本月报销金额")
month_money=int(month_money)
print("本月报销金额为：",month_money)
print("本年预计报销总金额为：",month_money*12)  
if month_money % 2 ==0:
    print( "本月报销金额为偶数")
else:
    print("本月报销金额为奇数")
