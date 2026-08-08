'''请编写一个实现【注册】和【登陆】功能的代码，这次要求将不同的功能封装成独立的函数
程序要求如下：
编写 4 个函数分别用于获取用户指令get_int()、注册register()、登陆login()、MD5加密encrypt()
使用一个 Python 的字典作为数据库。
注册时需验证用户名是否已存在于数据库
登陆时需验证用户名和密码是否匹配
密码保存需使用 MD5 加密'''
import hashlib

def get_int():
    print('======================')
    print('1.注册\n2.登录\n3.退出')
    print('请输入指令：')
    i = input()
    while not(i == '1' or i == '2' or i == '3'):
        i = input('无效之令，请重新输入：')
    print('======================')
    return i

def register(records):
    name = input('请输入用户名：')
    while name in records:
        name = input('用户名已存在，请重新输入：')
    pswd = input('请输入秘密：')
    code = encrypt(pswd)
    records[name] = code
    print('恭喜，注册成功')

def login(records):
    name = input('请输入用户名：')
    if name in records:
        pswd = input('请输入秘密：')
        while records[name] != encrypt(pswd):
            pswd = input('密码错误，请重新输入:')
            code = encrypt(pswd)
        print('登录成功')
    else:
        print('该用户名不存在')

def encrypt(pswd):
    bstr = str(pswd).encode('utf-8')
    code = hashlib.md5(bstr).hexdigest()
    return code

#main logic
print('欢迎来到论坛')
records = {}
i = None
while i != '3':
    i = get_int()
    if i == '1':
        register(records)
    elif i == '2':
        login(records)