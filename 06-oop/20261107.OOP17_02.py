'''创建一个描述符类 Typed, 用于对属性进行类型检查。
在设置属性值时，如果类型不匹配，抛出 TypeError'''
class Typed:
    def __init__(self, tp=int):
        self.tp = tp

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return obj.__dict__[self.name]
    
    def __set__(self, obj, val):
        if not isinstance(val, self.tp):
            raise TypeError('数据类型不符')
        obj.__dict__[self.name] = val
        
class Product:
    name = Typed(str)
    price = Typed(float)

    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Apple", 10.0)
print(f'{p.name}价格为{p.price}')
p.price = 12.5        # 正常修改
print(f'{p.name}价格为{p.price}')
p.price = '12.5'      # 应该抛出 TypeError