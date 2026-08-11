'''编写一个函数，将指定的罗马字符转换为数字的形式'''

dicnum = dict(zip(('I', 'V', 'X', 'L', 'C', 'D', 'M'), (1,5,10,50,100,500,1000)))

def roman2num(s):
    r = 0
    n = len(s)
    for i, ch in enumerate(s):
        val = dicnum[ch]
        if i < n-1 and val < dicnum[s[i+1]]:
            r -= val
        else:
            r += val
   
    return r

s = None
while s!= 'exit':
    s = input("请输入一个罗马字符：")
    for each in s:
        if each not in dicnum.keys():
            print('illeagal input')
            break
    else:
        r = roman2num(s)
        print(f"转换后的结果是：{r}")