with open("accounts.txt","w",encoding="utf-8")as f:
    f.write("餐饮,35\n")
    f.write("交通,6\n")
    f.write("购物,300\n")

with open("accounts.txt","r",encoding="utf-8")as f:

    total=0
    for line in f:
        i=line.strip().split(",")
        amount=int(i[1])
        total+=amount
        print("类别：",i[0] ,"金额:",amount)
    print(total)






