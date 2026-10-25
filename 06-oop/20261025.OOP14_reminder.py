'''使用 Python 编写一个类，模拟类似 iPhone 的提醒事项功能
程序应具备以下功能:
1.使用文件(如:reminders.pkl)来存储提醒事项
2.添加提醒事项
3.查看提醒事项列表
4.删除提醒事项
5.标记提醒事项为已完成
6.搜索提醒事项
7.按不同属性对提醒事项进行排序'''
import pickle, time
from pathlib import Path

class Reminder:
    def __init__(self, file):
        self.file = Path(file)
        self.msgs = self.loadData()

    def loadData(self):
        if self.file.exists():
            with self.file.open('rb') as f:
                return pickle.load(f)
        return []

    def saveData(self):
        with self.file.open('wb') as f:
            pickle.dump(self.msgs, f)

    def __call__(self, oper, content, category,rank):
        addtime = time.strftime('%Y-%m-%d %H:%M:%S')
        self.msgs.append([oper, content, category, rank, addtime, '未完成'])
        self.saveData()
        print(f'已添加事项: {content}, 分类: {category}, 优先级: {rank}, 添加时间: {addtime}')

    def chkMsg(self):
        print('提醒事项:')
        for each in self.msgs:
            print(f'{each[1]}({each[2]})({each[5]}), 优先级: {each[3]}')

    def delMsg(self, num):
        _ = self.msgs.pop(num-1)
        self.saveData()
        print(f'已删除提醒: {_[1]}')

    def done(self, num):
        self.msgs[num-1][5] = '已完成'
        self.saveData()
        print(f'已完成事项: {self.msgs[num-1][1]}')

    def search(self, msg):
        for each in self.msgs:
            if msg in each[1]:
                print(f'搜索结果:\n{each[1]}({each[2]})({each[5]}), 优先级: {each[3]}')

    def rnkMsg(self, attr):
        if attr in '优先级':
            order = 3
        elif attr in '添加时间':
            order = 5
        else:
            raise ValueError('只能按"优先级"或"添加时间"排序')
        srt_msgs = sorted(self.msgs, key = lambda x:x[order])
        print(f'按{attr}排序:')
        for each in srt_msgs:
            print(f'{each[1]}({each[2]})({each[5]}), 优先级: {each[3]}, 添加时间: {each[4]}')

if __name__ == "__main__":
    # 测试阶段为了防止数据重复添加
    # 在每次启动时自动删除pickle文件
    p = Path.cwd() / "reminders.pkl"
    p.unlink(missing_ok=True)

    reminder = Reminder("reminders.pkl")
   
    # 添加提醒
    print("添加提醒 >>>")
    reminder('添加', '买牛奶', '购物', 1)
    reminder('添加', '发邮件', '工作', 2)
    reminder('添加', '学编程', '学习', 1)
    reminder('添加', '打游戏', '娱乐', 4)
    reminder('添加', '谈恋爱', '娱乐', 1)
    reminder('添加', '打酱油', '购物', 3)

    # 删除提醒
    print("\n删除提醒 >>>")
    reminder.delMsg(6)

    # 列举提醒
    print("\n列举提醒 >>>")
    reminder.chkMsg()

    # 完成提醒
    print("\n完成提醒 >>>")
    reminder.done(5)

    print("\n列举提醒 >>>")
    reminder.chkMsg()

    # 搜索提醒
    print("\n搜索提醒 >>>")
    reminder.search("编程")

    # 排序
    print("\n属性排序 >>>")
    reminder.rnkMsg("时间")