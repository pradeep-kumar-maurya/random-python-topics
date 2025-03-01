def f1(func):
    def wrapper():
        print('started')
        func()
        print('ended')

    return wrapper


@f1
def f():
    print('hello')


f()
