def f1(func):
    # we need to pass *args and **kwargs if the func takes arguments
    def wrapper(*args, **kwargs):
        print('started')
        func(*args, **kwargs)  # call func with the provided arguments
        print('ended')

    return wrapper


@f1
def f(text1, text2='world'):
    print(text1, text2)


f('hello', text2='python')
