""" 用Pyhon设计第一个游戏 """

temp = input("猜一个数字：")
guess = int(temp)

if guess == 8:
    print("BINGO")
    print("厉害厉害")
else:
    print("猜错了， 是8")

print("Game over")
 