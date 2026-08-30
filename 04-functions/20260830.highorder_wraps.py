import time
import functools

def time_m(func):
    @functools.wraps(func)
    def call_func():
        print('start')
        start = time.time()
        func()
        end = time.time()
        print('end')
        print(f'耗时{(start - end): .2f} 秒')
    return call_func

@time_m
def myfunc():
    time.sleep(1)
    print('Hello pal')

myfunc()
print(myfunc.__name__)