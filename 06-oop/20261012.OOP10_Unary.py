'''做一个一进制
加法：1 + 1 = 11；1 + 11 = 111，11 + 111 = 11111
减法：1 - 1 = 没有；11 - 1 = 1；11111 - 11 = 111
乘法：1 * 1 = 1；11 * 11 = 1111；11 * 111 = 111111
除法：111111 / 11 = 111；1111 / 11 = 11；1 / 1 = 1'''
#老师的版本更好
class Unary:
    def __init__(self, num):
        self.num = num
        self.frac = self.sub = self.mul = self.div =''
        for i in range(self.num):
            self.frac += '1'
        self.len = len(self.frac)
    def __str__(self):
        return self.frac
    def __add__(self, other):
        return self.frac + other.frac
    def __sub__(self, other):
        for i in range(abs(self.len - other.len)):
            self.sub += '1'
        if self.len >= other.len:
            return self.sub
        return '-' + self.sub
    def __mul__(self, other):
        pos = self.len * other.len
        for i in range(pos):
            self.mul += '1'
        return self.mul
    def __truediv__(self, other):
        pos = self.len // other.len
        if pos < 1:
            self.div = '无'
        for i in range(pos):
            self.div += '1'
        return self.div
    __floordiv__ = __truediv__
    def __int__(self):
        return self.num

x = Unary(3)
y = Unary(0)
print(x-y)
print(int(y))