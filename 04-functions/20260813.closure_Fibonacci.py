'''设计一个闭包函数，它的功能是每次调用返回一个斐波那契数列'''
def fib():
    x = 0
    y = 1
    def calc():
        nonlocal x, y
        print(x)
        z = x
        x += y
        y = z
    return calc
f = fib()

f()
f()
f()
f()
f()
f()
f()
f()
f()