def add_attribute(cls):
    def wrapper():
        print("adding an attribute to the class")
        cls.name = "monkey patched attribute"
        print("added the attribute to the class")
    
    return wrapper


@add_attribute
class A:
    pass


f = add_attribute(A)
f()
print(A.name)


# ------------------------------ ALTERNATE --------------------------------

def add_attribute(cls):
    cls.name = "monkey patched attribute"    
    return cls


@add_attribute
class A:
    pass


a = A()
print(a.name)  # name attribute can be called on the instance, despite being a class attribute
print(A.name)
