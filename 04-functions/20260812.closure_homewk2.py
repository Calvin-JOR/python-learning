'''通过funcA(3)(4)(5)得出60'''

def A(x):
    def B(y):
        def C(z):
            return x*y*z
        return C
    return B

funA = A
print(funA(3)(4)(5))