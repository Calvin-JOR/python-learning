def make_avg():
    x = 0
    cnt = 0
    def divide(n):
        nonlocal x,cnt
        x += n
        cnt +=1
        print(x/cnt)
    return divide

avg = make_avg()
avg(5)
avg(3)
avg(7)
avg(19)