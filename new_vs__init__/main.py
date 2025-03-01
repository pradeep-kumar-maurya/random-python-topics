class Person:
    # __new__ creates and returns an instance of the current class
    def __new__(cls, *args, **kwargs):  # this method will be executed 1st
        print('__new__ method called')
        instance = super().__new__(cls)
        return instance

    # __init__ initializes the instance with some values after the instance creation
    def __init__(self, fn, ln):  # this method will be executed 2nd
        print('__init__ method called')
        self.fn = fn
        self.ln = ln


p = Person('pradeep', 'maurya')
print(p.fn)
print(p.ln)


# Demonstration of how to personalize the instance creation of a class
class Language:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print(f'creating an instance of class {cls.__name__}')
            cls.__instance = super().__new__(cls)
        return cls.__instance


l1 = Language()
l2 = Language()

'''
it will print True because the creation of 2nd instance just returned the 1st instance from the very 1st instance
creation rather than creating a new instance.
'''
print(l1 is l2)
