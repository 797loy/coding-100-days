raw_lines=[" 餐饮,35 "," 交通,6元 "," 购物,300元 "]
total=0
for line in raw_lines:
    clean=line.strip()
    cat,money_text=clean.split(",")
    cat=cat.strip()
    money=int(money_text.strip().replace("元",""))
    print("类别：",cat,"金额",money)
    total=total+money

print("总支出：",total)


    


