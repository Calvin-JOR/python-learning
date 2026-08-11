'''编写一个函数，将指定的数字转换为罗马字符的形式'''
N1R = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]
N2R = zip((1000,900,500,400,100,90,50,40,10,9,5,4,1),
          ('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'))
def num2roman(num):
    r = []
    for v, s in N2R:
        while num >= v:
            num -= v
            r.append(s)
        if num == 0:
            break
   
    return "".join(r)
n = input("请输入一个整数：")
r = num2roman(int(n))
print(f"转换后的结果是：{r}")