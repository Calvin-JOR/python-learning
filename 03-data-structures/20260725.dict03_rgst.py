'''请按照要求编写一个网站的注册模块
要求:
用户名不允许重复
数据库需要保存用户名及密码
初始用户及密码（"小甲鱼":"I_love_FishC"，"不二如是":"FishC5201314"）'''

import hashlib
users = {'小甲鱼':'I_love_FishC','不二如是':'FishC5201314'}
name = input('请输入用户名:')
if name in users:
    go = True
    while go:
        print('改用户名已被注册！')
        name = input('请重新输入用户名:')
        if name not in users:
            go = False
pswd = input('请输入密码：')
users[name] = pswd
print('目前已注册的用户有：')
for each in users:
    result = hashlib.md5(users[each].encode())
    print(f'{each}: {result.hexdigest()}')