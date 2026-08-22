'''利用生成器定义一个支持浮点数的 frange() 函数，其功能与 range() 函数相仿'''

def frange(start, stop=None, inc=0.1):  # 用stop=None做哨兵
     s = str(inc)
     pre = len(s[s.find('.')+1:])
     float(start)                       # 确保start变成浮点数

     if stop == None:                   # 当只有一个参数输入时自动将
                                        #其转为stop而start变成0.0
        stop = start                    # 确保stop变成浮点数
        start = 0.0

     while start < stop:
        yield round(start, pre)
        start += inc

for i in frange(1, 2, 0.05):
    print(i)