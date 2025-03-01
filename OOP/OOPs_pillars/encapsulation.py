class MyClass:
    __private_num = 1000
    _protected_num = 2000

    def __init__(self):
        self.__private_var = 1
        self._protected_var = 2

    def get_private_var(self):
        return self.__private_var

    def get_protected_var(self):
        return self._protected_var


m = MyClass()

# simply accessing private and protected attributes by using the instance methods created in the class
print(m.get_private_var())
print(m.get_protected_var())

# protected attributes from instance or class can be accessed from the instance of the class
print(m._protected_var)
print(m._protected_num)

# private attributes could also be accessed but using "_ClassName__private_attribute_name"
print(m._MyClass__private_var)
print(m._MyClass__private_num)

# both private and protected class attributes could also be accessed
print(MyClass._protected_num)
print(MyClass._MyClass__private_num)
