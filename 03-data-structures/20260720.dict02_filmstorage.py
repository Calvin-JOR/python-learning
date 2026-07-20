'''请利用字典类型，改进上一节课后作业的电影查询小程序'''
movies = {}

print('欢迎使用影评系统')
print('1.影片录入\n2.影片查找\n3.退出系统')
op = int(input('请输入想要的功能(1/2/3):'))

while op != 3:
    if op == 1:
        go = True
        while go:
            movie = (input('请输入电影名：'))
            date = (input('请输入上映日期：'))
            director = (input('请输入导演名：'))
            actors = (input('请输入演员名(多人请用 / 分割)：'))
            scores = (input('请输入评分：'))
            if input('是否继续录入？(y/n)') == 'n':
                go = False
            movies[movie] = {'date':date, 'director':director, 'actors':actors, 'scores':scores}

    if op == 2:
        name = input('请输入电影名：')
        if name in movies:
            print(f'电影名：{name}')
            print(f'上映日期：{movies[name]['date']}')
            print(f'导演：{movies[name]['director']}')
            print(f'演员：{movies[name]['actors']}')
            print(f'评分：{movies[name]['scores']}')
        else:
            print('查无此片')
    
    op = int(input('请输入想要的功能(1/2/3):'))