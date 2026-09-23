'''利用 __bases__ 属性，获取一个类的 MRO 顺序
还根据父类的层数，添加了相应数量的横杆'''
import tkinter
def get_bases(cls, count = 0): 
    for i in range(count):
        print('-', end = ' ')
    print(cls)

    if cls.__bases__[0] is not object:
        for each in cls.__bases__:
            count += 1
            get_bases(each, count)
            count -= 1
            
get_bases(tkinter.Text)