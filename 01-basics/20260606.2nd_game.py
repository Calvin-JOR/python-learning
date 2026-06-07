import random
goal = random.randint(0,9)
i = 3
while i > 0:
    temp = input(f"猜一个数字,你还有{i}次机会\n")
    guess = int(temp)
    if guess == goal:
        print("BINGO")
        print("厉害厉害")
        break
    elif guess > goal:
        print("大了")
    elif guess < goal:
        print("小了")
    i -= 1

print("Game over")
