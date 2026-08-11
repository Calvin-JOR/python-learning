import random

def shuffle(s, t):
    s = s.split(',')
    for times in range(t):
        r =[]                       #在循环内声明r以便每次刷新
        length = len(s)
        while length > 0:
            i = random.randrange(0,length)
            r.append(s[i])
            s.pop(i)
            length = len(s)

        out = ','.join(r)
        print(f'第{times+1}次洗牌结果为: {out}')
        s = out.split(',')          #重置s为上一次输出的结果,问题的关键！
        

s = input('请输入要打乱的序列:')
it = input('请输入要打乱的次数:')
ot = int(it)
shuffle(s, ot)