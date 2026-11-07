'''编写一个描述符类 ValidString, 用于管理属性的自动验证和格式化
属性值必须是字符串类型。
设置属性值时，自动去除首尾空白字符。
属性值长度不能超过指定的最大长度，否则抛出 ValueError。'''
class ValidStr:
    def __init__(self, length=5):
        self.length = length
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return obj.__dict__[self.name]
    def __set__(self, obj, val):
        val = val.strip()
        if len(val) > self.length:
            raise ValueError('超过最大长度')
        obj.__dict__[self.name] = val

class User:
    username = ValidStr(length=20)
    email = ValidStr(length=50)

    def __init__(self, username, email):
        self.username = username
        self.email = email

u = User("   FishC   ", " fishc@ilovefishc.com ")
print(u.username)     # 输出："FishC"
print(u.email)        # 输出："fishc@ilovefishc.com"
u.username = "FishC" * 5  # 应该抛出 ValueError