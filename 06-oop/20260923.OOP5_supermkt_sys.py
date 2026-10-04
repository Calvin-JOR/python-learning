'''https://fishc.com.cn/thread-214131-1-2.html
做一个超市会员管理系统'''
import time
import hashlib
# 创建一个会员类（Member），包含信息：卡号、用户名、密码（要求密码需要以 MD5 哈希值的形式存储）、积分、注册日期
class Member:
    def __init__(self, id, name, pswd, pts, regdate):
        self.id = id
        self.name = name
        self.pswd = pswd
        self.pts = pts
        self.regdate = regdate

#创建一个 Mixin 类（PasswdMixin），用于实现密码相关的功能组件（密码长度检测和将明文密码转换为 MD5 的操作）
class PswdMixin:
    def passchk(self, pswd):
        while len(pswd) < 6:
            pswd = input('密码长度不得低于6位，请重新输入：')
        else:
            bstr = str(pswd).encode('utf-8')
            pswd = hashlib.md5(bstr).hexdigest()
            return pswd
        
#创建一个 Mixin 类（LoggerMixin），用于实现日志记录相关的功能组件
class LoggerMixin:
    def log(self, msg, filename='system_log.txt'):
        with open(filename, 'a') as f:
            f.write(msg)

#创建一个管理类（Manage），用于实现上方要求的主要程序功能
class Manage(PswdMixin, LoggerMixin):
    def __init__(self):
        self.members = {}
        self.id = 10000
        
    #程序入口
    def welcome(self):
        order = 0
        print('欢迎使用会员系统')
        while order != '5':
            order = input('\n1.创建新卡 2.修改密码 3.商品支付 4.积分查询 5.退出系统\n')
            if order == '1':
                self.create_member()
            elif order == '2':
                self.modify_pswd()
            elif order == '3':
                self.pay()
            elif order == '4':
                self.pts_chk()

    #创建新卡
    def create_member(self):
        name = input('请输入用户名：')
        pswd = input('请输入密码：')
        pswd = self.passchk(pswd)
        pts  = 0
        regdate = time.localtime()
        self.members[self.id] = Member(self.id, name, pswd, pts, regdate)   #类中有其他类的实例：组合
        #key为卡号，value为类Member的字典
        print(f'创建成功， 卡号{self.id}, 用户名{name}')
        self.log(f'创建新卡, {self.id} -> {name}, 时间 {time.strftime('%m-%d-%Y %H:%M:%S',regdate)}\n')
        self.id += 1
        
    #确认卡号和秘密是否匹配
    def confirm_pswd(self):
        id = int(input('请输入卡号：'))
        while id not in self.members:
            id = int(input('改卡号不存在，请重新输入：'))
        old_pswd = input('请输入密码：')
        old_pswd = self.passchk(old_pswd)
        while old_pswd != self.members[id].pswd:
            old_pswd = input('密码错误，请重新输入：')
            old_pswd = self.passchk(old_pswd)
        return id

    #修改密码
    def modify_pswd(self):
        id = self.confirm_pswd()
        new_pswd = input('请输入新密码：')
        new_pswd = self.passchk(new_pswd)
        new_pswd2 = input('请再次输入新密码：')
        new_pswd2 = self.passchk(new_pswd2)
        while new_pswd2 != new_pswd:
            new_pswd2 = input('密码不一致，请重新输入：')
            new_pswd2 = self.passchk(new_pswd2)
        self.members[id].pswd = new_pswd
        print('密码修改成功')
        self.log(f'修改密码, 卡号 -> {id}, 时间 {time.strftime('%m-%d-%Y %H:%M:%S', time.localtime())}\n')

    #商品支付
    def pay(self):
        id = self.confirm_pswd()
        amount = int(input('请输入金额：'))
        pts = int(round(amount*0.1, 0))
        self.members[id].pts += pts
        self.log(f'消费积分, 卡号 -> {id} + {pts}分,'
                 f'时间 {time.strftime('%m-%d-%Y %H:%M:%S', time.localtime())}\n')

    #积分查询
    def pts_chk(self):
        id = self.confirm_pswd()
        print(f'卡号{id}的当前积分为：{self.members[id].pts}\n')

def main():
    m = Manage()
    m.welcome()
main()