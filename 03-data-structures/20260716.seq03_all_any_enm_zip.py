'''利用 for 循环语句，模拟 all()、any()、enumerate()、zip() 这4个函数的实现'''

x = [1, 2, 0]
y = ['a', 'b', 'c']
#all()
for each in x:
    if not each:
        print(False)
        break
else:
    print(True)

#any()
for each in x:
    if each:
        print(True)
        break
else:
    print(False)

#enumerate()
enu = []
for i in range(len(x)):
    enu.append((i, x[i]))
print(enu)

#zip()
length = min(len(x), len(y))
zp = []
for i in range(length):
    zp.append((x[i], y[i]))
print(zp)