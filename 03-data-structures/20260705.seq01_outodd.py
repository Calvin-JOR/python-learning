'''给定一个字符串s 请编程求出该字符串中的最大奇数
举例：
输入 43383
输出 43383
输入 5926
输出 59
输入 966
输出 9
输入 64062
输出 0'''
s = input('type your number:')
result = '0'

for i in range(len(s)-1, -1, -1):
    if int(s[i]) % 2 != 0:
        result = s[:i+1]
        break
print(result)