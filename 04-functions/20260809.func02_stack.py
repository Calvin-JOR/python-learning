'''将压栈命令(push)、取出命令(pop)和打印栈的功能分别封装为独立的函数。'''

def push(lst):
    content = input()
    lst.append(content)
    print('当前栈为：')
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])

def pop(lst):
    if len(lst) > 0:
        lst.pop(len(lst)-1)
    else:
        print('栈为空')
    if len(lst) > 0:
        print('当前栈为：')
        for i in range(len(lst)-1, -1, -1):
                print(lst[i])
    else:
        print('栈为空')
    
def top(lst):
    if len(lst) > 0:
        print(lst[len(lst)-1])
    else:
        print('栈为空')

lst = []
cmd = None
while True:
    cmd = input('请输入指令(push/pop/top/exit):')
    if cmd == 'push':
        push(lst)
    elif cmd == 'pop':
        pop(lst)
    elif cmd == 'top':
        top(lst)
    elif cmd == 'exit':
        break
    else:
        print('非法指令，请重新输入')