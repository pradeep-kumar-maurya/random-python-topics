class A:
    def m1(self):
        print('m1 from A')

    def f1(self):  # same method in class B
        print('f1 from A')


class B:
    def m2(self):
        print('m2 from B')

    def f1(self):  # same method in class A
        print('f1 from B')


class C(A, B):  # multiple inheritance
    pass


c = C()
c.m1()
c.m2()

# Below method call will print 'f1 from A' because during multiple inheritance A comes first.
# Similarly, if multiple inheritance was C(B, A), it will print 'f1 from B' because now B comes first.
c.f1()

