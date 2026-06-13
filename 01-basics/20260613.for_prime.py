for i in range(2,11):
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        print(i, end = "\t")