#0.编写一个递归函数，计算从 1 + 2 + 3 + ... + n 的结果（比如 n = 10，那么结果就是 55）
def get_sum(n):
    if n == 1:
        return 1
    return n + get_sum(n-1)

#print(get_sum(10))
#print(get_sum(100))

#1.编写一个递归函数，判断该整数是否为 2 的幂次方。如果是返回 True，否则返回 False
def poweroftwo(n):
    if n > 0:
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return poweroftwo(n/2)
    else:
        return False

#print(poweroftwo(10))
#print(poweroftwo(8))

#2.请实现一个递归函数，要求只使用加号运算符（+）来实现乘法运算的结果
def mul(a, b):
    if b == 0:
        return 0
    return a + mul(a, b-1)

print(mul(3,4))

#3.编写一个递归函数，找到该列表中最大的元素
def getMax(L):
    if len(L) == 2:
        return L[0] if L[0] > L[1] else L[1]
    else:
        sub = getMax(L[1:])
        return L[0] if L[0] > sub else sub

print(getMax([1,2,3,4,5,9]))    