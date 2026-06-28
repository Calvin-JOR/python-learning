"""编写一个加密程序，其实现原理是通过替换指定的字符进行加密"""
s = input("输入明文:")
x = input("输入要替换的文本:")
y = input("输入替换后的文本:")

if len(x) != len(y):
    print("目标文本的长度不一样")
else:
    out_str = s.translate(str.maketrans(x,y))
    print("加密后的密文是:" + out_str)

    #检测冲突，用flag作为跳出检测的触发器
    flag = 0

    #如果x中有相同字符，y也应该对应相同
    for each in x:
        if x.count(each) > 1 and flag == 0:
            i = x.find(each)                        #返回重复字符的第一个下标
            last = y[i]
            while i != -1:                          #此处的循环条件i != -1是对应跳出循环
                if last != y[i]:                    #条件 i = x.find(each, i+1)一起看的，
                    flag = -1                       #虽然 i一开始必不等于-1，但随着遍历x
                    print("替换文本有冲突，无法解密") #中重复的each直至最后找不到，find()还
                    break                           #是会返回-1
                i = x.find(each, i+1)

    #y也做相同处理
    for each in y:
        if y.count(each) > 1 and flag == 0:
            i = y.find(each)
            last = x[i]
            while i != -1:
                if last != x[i]:
                    print("替换文本有冲突，无法解密")
                    flag = -1
                    break
                i = y.find(each, i+1)