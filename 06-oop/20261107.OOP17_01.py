'''创建一个只读属性的描述符类 ReadOnly, 
使得被它管理的属性在实例创建后无法被修改
或删除。如果尝试修改或删除属性，应该抛出
AttributeError'''
class ReadOnly:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return obj.__dict__[self.name]
    
    def __set__(self, obj, val):
        if self.name in obj.__dict__:
            raise AttributeError('can\'t be setted')
        obj.__dict__[self.name] = val

    def __delete__(self, obj):
        raise AttributeError('can\'t be deleted')

class C:
    name = ReadOnly()
    def __init__(self, name):
        self.name = name

c = C('abc')
print(c.name)
c.x = 5
print(c.x)