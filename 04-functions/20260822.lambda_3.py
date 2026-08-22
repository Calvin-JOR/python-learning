power = {"吕布":999, "关羽":888, "刘备":666, "张飞":900, "赵云":789, "不二如是":999}

# 请使用一行代码，替换下面的代码
greater = []
'''for k, v in power.items():
    if v > 800:
        greater.append((k,v))'''
# 请使用一行代码，替换上面的代码
greater = [(name, strength)  for name, strength in power.items() if strength > 800]
print(greater)
[('吕布', 999), ('关羽', 888), ('张飞', 900), ('不二如是', 999)]