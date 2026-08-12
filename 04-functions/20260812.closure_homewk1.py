def outter():
    def innerA():
        x = 100
    def innerB():
        nonlocal x
        x = 250
    def innerC():
        global x
        x = 520
    x = 880
    
    innerA()
    print(f"调用完 innerA() 函数之后，x = {x}")
    innerB()
    print(f"调用完 innerB() 函数之后，x = {x}")
    innerC()
    print(f"调用完 innerC() 函数之后，x = {x}")
outter()
print(f"此时此刻，全局变量 x = {x}")