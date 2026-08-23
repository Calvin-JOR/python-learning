import timeit

def fibRecur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibRecur(n-1) + fibRecur(n-2)

def tailFibRecur(n, x, y):
    if n == 1 or n == 2:
        return y
    else:
        return tailFibRecur(n-1, y, x+y)

def fibIter(n):
    a, b, c = 1, 1, 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

# 这个耗时会比较久（因为默认是重复测试 5 次），请大家耐心等待
FR = timeit.timeit("fibRecur(12)", setup="from __main__ import fibRecur")
print(f"普通递归耗时：{FR:.2f}秒。")

TFR = timeit.timeit("tailFibRecur(12, 1, 1)", setup="from __main__ import tailFibRecur")
print(f"优化递归耗时：{TFR:.2f}秒。")

FI = timeit.timeit("fibIter(12)", setup="from __main__ import fibIter")
print(f"普通迭代耗时：{FI:.2f}秒。")