class A:
    def __init__(self):
        super().__init__()
        print('A')


class B:
    def __init__(self):
        print('B')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C')


c = C()
print(C.mro())

'''
1. super() follows MRO, not the immediate parent.
2. In C(A, B), the MRO is [C, A, B, object], so super() in A calls B if A uses super().
3. If A.__init__() does not call super(), B.__init__() will never be executed.
'''
