# from typing import overload
#
#
# class A(metaclass=):
#     @overload
#     def f(self, x: int):
#         print(type(x))
#
#     @overload
#     def f(self, x: str):
#         print(type(x))
#
#     @overload
#     def f(self, x, y):
#         print(x, y)
#
#
# a = A()
# a.f(10)
# a.f("hello")
# a.f(1, 2)
