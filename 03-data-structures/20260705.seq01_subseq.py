'''给定字符串 s 和 t ，请编程判断 s 是否为 t 的子序列
字符串的子序列是原始字符串删除一些（也可以不删除）字符
而不改变剩余字符相对位置形成的新字符串
例如，"ace" 是 "abcde" 的子序列，而 "aec" 则不是'''

s_str = input('输入字符串s:')
t_str = input('输入字符串t:')

n = len(s_str)
m = len(t_str)
j = k = 0

while j < n and k < m:
    if s_str[j] == t_str[k]:
        j += 1
    k += 1
if j == n:
    print('s is the subseq of t')
else:
    print('s is not subseq of t')