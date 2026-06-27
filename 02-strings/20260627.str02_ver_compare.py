v1 = input("输入第一个版本号：")
v2 = input("输入第二个版本号：")

n, m = len(v1), len(v2)
i, j = 0, 0

while i < n or j < m:               #最外层循环，跨越"."计算
    x = 0
    while i < n and v1[i] != ".":   #内层v1计算
        x = x * 10 + int(v1[i])
        i += 1
    i += 1                          #遇到"."时i依然+1
    
    y = 0
    while j < m and v2[j] != ".":   #内层v2计算
        y = y * 10 + int(v2[j])
        j += 1
    j +=1                           #遇到"."时j依然+1

    if x > y:
        print("v1为更新版本")
        break
    elif x < y:
        print("v2为更新版本")
        break

if x == y:
    print("v1 == v2")