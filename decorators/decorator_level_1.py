def f1(func):
    # wrapper here is a nested function which would be returned like an object from f1
    def wrapper():
        print('started')
        func()  # this is the function we have defined to be wrapped with other logic
        print('ended')

    return wrapper


def f():
    print('hello')


wrapper_function = f1(f)  # this would return a wrapper function
wrapper_function()  # call the function with () brackets
