#凯撒密码是一种通过位移加密的方法，对 26 个（大小写）字母进行位移加密，
# 比如下方是正向位移 6 位的字母对比表
#明文字母表如下
#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
#密文字母表如下
#GHIJKLMNOPQRSTUVWXYZABCDEFghijklmnopqrstuvwxyzabcdef
#所以，如果给定加密的明文是
#I love FishC
#那么程序加密后输出的密文便是
#O rubk LoynI

plain = list(input("input your plain(only english):"))
key = int(input("移动位数"))

base_A = ord('A')
base_a = ord('a')

cipher = []
for each in plain:
    if each == ' ':
        cipher.append(each)
    else:
        if each.isupper():
            base = base_A
        else:
            base = base_a
        cipher.append(chr((ord(each)- base + key) % 26 + base))

print(''.join(cipher))

