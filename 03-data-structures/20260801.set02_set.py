'''题目要求：不用集合的特性
生成一个随机数列表，一共有 100 个元素，每个元素取 1~100 的随机值，赋值给变量 x
生成另一个随机数列表，一共有 100 个元素，每个元素取 50~150 的随机值，赋值给变量 y
利用字典的 “键” 不会重复的特点，计算 x 和 y 的交集（就是两者共有的元素）'''
import random

x = [random.randint(1,100) for i in range(1,101)]
y = [random.randint(50,150) for i in range(1,101)]
inter = dict.fromkeys([z for z in x if z in y])
print(list(inter.keys()))