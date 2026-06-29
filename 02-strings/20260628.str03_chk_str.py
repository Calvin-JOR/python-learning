#编写一个程序，判断输入的字符串是否由多个子字符串重复多次构成
txt = input("input your text:")
n = len(txt)

for i in range(1, n // 2 + 1):      #一个字符串能由重复子串构成，子串长度最长只能是 n // 2，
                                    #因为至少要重复2次才叫"重复子串"，又因为Python左闭右开
                                    #的特性，需要n整除2再加1
    if n % i == 0:
        if txt.startswith(txt[i:i*2]) and txt.count(txt[i:i*2]) == n / i:
            print(True)
            break
else:
    print(False)
#因为子字符串的长度为i，所以切片操作txt[i:i*2]，起点和终点一定是子字符串开始的下标，又因为
#Python左闭右开的特性，终点的取值会-1，所以切片下来就是一个子字符串
#以“abcabcabc”为例，子字符串长度是3，txt[3:6]就是下标3~5的字符abc