'''展示扑克牌并识别牌型'''
#展示所有牌
def showcards():
    cards = ["♦A", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K",
             "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K",
             "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K",
             "♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K",
             "☀ ", "🌙"]

    for i in range(54):
        print(cards.pop(0), end='  ')
        if (i+1)%13 == 0:
            print()
    print()
    '''for i in range(0, len(cards), 13):
        print('   '.join(cards[i:i+13]))'''

#牌型判断
def is_what(play):
    play = sorted(play)
    is_what = '不符合规则'
    if len(play) == 1:
        is_what = '单张'
    elif len(play) == 2 and play[0] == play[1]:
        is_what = '对子'
    elif 19 in play and 20 in play:
        is_what = '王炸'
    elif len(play) == 3 and len(set(play)) == 1:
        is_what = '三个头'
    elif len(play) == 4:
        if len(set(play)) == 1:
            is_what = '炸弹'
        elif any(play.count(i) == 3 for i in play):
            is_what = '三带一'
    elif len(play) == 5:
        if all(play[i]+1 == play[i+1] for i in range(4))\
           and 15 not in play:
            is_what = '顺子'
        elif any(play.count(i) == 3 for i in play) and\
            len(set(play)) == 2:
            is_what = '三带二'
        elif any(play.count(i) == 4 for i in play):
            is_what = '四带一'
    elif len(play) == 6:
        if any(play.count(i) == 4 for i in play):
            is_what = '四带二'
        elif len(set(play)) == 2:
            air, rst = air_chk(play)
            if len(air) == 2 and air[0] + 1 == air[1] and\
               not set((15,19,20)) & set(air):
                is_what = '光板飞机'
        else:
            unique = sorted(set(play))
            if len(set(play)) == 3 and all(unique[i] + 1\
               == unique[i+1] for i in range(2)) and\
               all(play.count(i) == 2 for i in play)\
               and 15 not in play:
                is_what = '连对'
    elif len(play) == 8 or len(play) == 10:
        air, rst = air_chk(play)
        if len(air) == 2 and air[0] + 1 == air[1] and\
           not set((15,19,20)) & set(air) and len(set(rst)) == 2:
            is_what = '飞机'
    print(is_what)

#飞机检验
def air_chk(lst):
    air = []
    rst = []
    for each in lst:
        if lst.count(each) == 3:  #这一步会把每一项有3个的都添加进去
            air.append(each)
        else:
            rst.append(each)
    air = sorted(set(air))        #所以要用set去重
    return air, rst

#获取出牌
def get_play():
    play = input('输入你的牌型:(退出按q)  ')
    if play == 'q' or play == 'Q':
        return 0
    else:                   # split()默认将空白字符视为分隔符
        play = play.split() # "♠A ♠2 ♠3 ♠4 ♠5" -> ['♠A', '♠2', '♠3', '♠4', '♠5']
        return play

 # 将扑克牌映射成代表权限的数字
def change_play(play):
    result = []
    target = {'3':3, '4':4, '5':5, '6':6, '7':7,
              '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':15}
    for each in play:
        num = target.get(each[1:]) #去掉出牌中的花色
        if num:
            result.append(num)
        else:
            result.append(19 if each == '🌙' else 20)
    return result

#Main
showcards()
play = get_play()
while play:
    play = change_play(play)
    is_what(play)
    play = get_play()