'''编写一个源代码，它的功能就是打开自己的源文件，然后打印出来'''

f = open('20260905.open_myself.py', 'r', encoding='utf-8')
for each in f:
    print(each)
f.close()