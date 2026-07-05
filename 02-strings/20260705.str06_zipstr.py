'''利用字符重复出现的次数，编写一个程序，实现基本的字符串压缩功能。
比如:字符串FFiiiisshCCCCCC压缩后变成F2i4s2h1C6 15字符 -> 10字符 66%压缩率
这种朴素的压缩算法并不总是理想的 比如FFishCC压缩后反而变长了F2i1s1h1C2这可就
不是我们想要的了 所以对于重复次数小于3的字符 我们的程序应该选择不对其进行压缩'''

zipstr = input('输入要压缩的字符串：')
process = list(zipstr)
outstr = []
outstr2 =[]

while process:
    current = process[0]
    count = process.count(current)
    if count > 3:
        outstr.append(current)
        outstr2.append(count)
    else:
        for i in range(count):
            outstr.append(current)
            outstr2.append('')
    #process.remove(current) remove()之后删除一次，除非进循环
    process = [x for x in process if x != current] #列表推导式是最优解

outstr3 = ''.join(f'{ch}{n}' for ch, n in zip(outstr, outstr2))
c = 1 - len(outstr3) / len(zipstr)
print(outstr3)
print(f'压缩率：{c:.2%}')