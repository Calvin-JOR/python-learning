'''制作一个电影数据库'''
movie = []
date = []
director = []
actors = []
scores = []

print('欢迎使用影评系统')
print('1.影片录入\n2.影片查找\n3.退出系统')
op = int(input('请输入想要的功能(1/2/3):'))

while op != 3:
    if op == 1:
        go = True
        while go:
            movie.append(input('请输入电影名：'))
            date.append(input('请输入上映日期：'))
            director.append(input('请输入导演名：'))
            actors.append(input('请输入演员名(多人请用 / 分割)：'))
            scores.append(input('请输入评分：'))

            if 'n' == input('是否继续录入？(y/n)'):
                go = False
    if op == 2:
        name = input('请输入电影名：')
        for each in movie:
            if each.find(name) != -1:
                print(f'电影名称：{each}')
                print(f'上映日期：{date[movie.index(each)]}')
                print(f'导演：{director[movie.index(each)]}')
                print(f'演员：{actors[movie.index(each)]}')
                print(f'评分：{scores[movie.index(each)]}')
                break
        else:
            print('查无此片')

    op = int(input('请输入想要的功能(1/2/3):'))