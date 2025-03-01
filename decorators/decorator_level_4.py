def f1(func):
    def wrapper(*args, **kwargs):
        print('adding...')
        result = func(*args, **kwargs)
        print('added')
        return result

    return wrapper


@f1
def add(x, y):
    return x + y


print(add(5, 6))
