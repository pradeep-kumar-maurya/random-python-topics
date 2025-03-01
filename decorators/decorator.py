def f1():
    print("called f1")


def f2(f):
    f()


'''
In python we can pass a function to another function because in python everything is an object at the end.
As objects can be passed to functions, similarly, function can be passed to a function.
'''
f2(f1)
