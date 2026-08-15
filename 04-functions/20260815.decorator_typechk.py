# 题目要求：
# 请在此处补充装饰器 type_check() 的代码
def type_check(input_type):
    def outer(func):
        def inner(*args, **kwargs):
            if all(type(x) == input_type for x in args):
                return func(*args, **kwargs)
            else:
                return '数据类型错误'
        return inner
    return outer

print("<<<--- 测试整数 --->>>")

@type_check(int)
def iptint(x):
    return x * 2

print(iptint(2))      # 这里打印结果应该是 4
print(iptint(2,'b'))    # 这里打印结果应该是 “参数类型错误”

@type_check(int)
def iptint2(x, y, z):
    return tuple(a * 2 for a in (x, y, z))

print(iptint2(1,2,3))

print("\n<<<--- 测试字符串 --->>>")

@type_check(str)
def upper(s):
    return s.upper()

print(upper('I love FishC.'))   # 这里打印结果应该是 I LOVE FISHC
print(upper(250))               # 这里打印结果应该是 “参数类型错误”
