'''编写一个装饰器，并将其放到适当的位置，目的是让代码 1 秒钟打印一个结果'''
import time

def delay(func):
    def exe ():
        print('tik tok')
        time.sleep(1)
        func()
    return exe

def fib():
    back1, back2 = 0, 1
    @delay
    def func():
        nonlocal back1, back2
        print(back1)
        back1, back2 = back2, back1 + back2
    return func

n = int(input("请输入需要获取的斐波那契数："))   
f = fib()
for i in range(n):
    f()