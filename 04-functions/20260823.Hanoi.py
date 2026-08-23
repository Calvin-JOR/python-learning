def hanoi(n, A, B, C):
    '''把n个盘子从A借助B移动到C'''
    if n == 1:
        print(f'将盘子从 {A} 移动到 {C}')
    else:
        hanoi(n - 1, A, C, B)   # 先把上面n-1个盘子从A移到B（借助C）
        print(f'将盘子从 {A} 移动到 {C}')  # 移动最底下最大的盘子
        hanoi(n - 1, B, A, C)   # 再把n-1个盘子从B移到C（借助A）

n = int(input('输入盘子层数：'))
hanoi(n, 'A', 'B', 'C')