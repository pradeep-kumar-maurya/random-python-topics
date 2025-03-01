class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):  # multiple inheritance
    pass


print(D.mro())  # MRO = Method Resolution Order
''' output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>] '''


class A:
    pass


class B(A):
    pass


class C(B):  # multi level inheritance
    pass


print(C.mro())
''' output: [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>] '''
