print('欢迎使用电话薄')
op = input('请输入指令 i.录入 / s.查询 / d.删除 / p.打印 / e.退出:\n')

phonebook = {}

while op != 'e':
    if op == 'i':
        print('-- 录入模式 --')
        go = True
        while go:
            name = input('请输入姓名：\n')
            number = input('请输入号码：\n')
            while len(number) != 11 or not number.isdigit():
                number = input('输入不合法，请重新输入：\n')
            while True:
                choice = input('是否继续录入？(y/n)\n')
                if choice == 'y':
                    break
                elif choice == 'n':
                    go = False
                    break
            phonebook[name] = number
    
    elif op == 's':
        print('-- 查询模式 --')
        go = True
        while go:
            search_name = input('请输入要查找的姓名：\n')
            if search_name in phonebook:
                print(f'{search_name}: {phonebook[search_name]}')
            else:
                print('未找到')
            while True:
                choice = input('是否继续查询？(y/n)\n')
                if choice == 'y':
                    break
                elif choice == 'n':
                    go = False
                    break
        
    elif op == 'd':
        print('-- 删除模式 --')
        go = True
        while go:
            del_name = input('请输入要删除的姓名：\n')
            if del_name in phonebook:
                del phonebook[del_name]
                print('该姓名已删除')
            else:
                print('电话簿中没有该名字')
            while True:
                choice = input('是否继续删除？(y/n)\n')
                if choice == 'y':
                    break
                elif choice == 'n':
                    go = False
                    break
    
    elif op == 'p':
        print('-- 打印模式 --')
        for each in phonebook:
            print(f'{each}:{phonebook[each]}')

    op = input('请输入指令 i.录入 / s.查询 / d.删除 / p.打印 / e.退出:\n')