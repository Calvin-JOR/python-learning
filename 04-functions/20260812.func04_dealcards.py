'''运用上一个作业的打乱算法，设计一个 “斗地主” 的发牌程序'''
import random

cards = ["♦A", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K",
         "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K",
         "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K",
         "♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K",
         "☀ ", "🌙"]

def shuffle(x, n=1):  
    target = cards                      #洗牌
    for i in range(n):
        result = []
        while target:
            r = random.randrange(0, len(target))
            result.append(target.pop(r))
        target = result                 #重置target以多次洗牌

    return result

def dealcards():
    a = input('第一位玩家是：')
    b = input('第二位玩家是：')
    c = input('第三位玩就是：')
    r = {}                              #创建一个空字典r
    r[a], r[b], r[c] = [], [], []       #创建a,b,c三个键，值为三个空列表

    new_cards = shuffle(cards, 3)       #洗3次牌

    for i in range(17):
        r[a].append(new_cards.pop())    #洗牌结果分别派发给a,b,c
        r[b].append(new_cards.pop())
        r[c].append(new_cards.pop())

    d = random.choice((a, b, c))
    r[d].extend(new_cards)              #将剩余的牌作为键d的值
    print(f'\n地主是:{d}\n')
    print(f'{a}拿到的牌是:{' '.join(r[a])}\n')
    print(f'{b}拿到的牌是:{' '.join(r[b])}\n')
    print(f'{c}拿到的牌是:{' '.join(r[c])}\n')

dealcards()