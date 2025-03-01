class Person:
    def __init__(self, name):
        self.name = name


p = Person('python')
print(p.name)

'''
Notice the class Person does not have any attribute names "version" but we added "version" attribute to the
already created object "p" andxl now we can use "version" attribute on the "p" object.
Dynamically attaching an attribute or method to a class or object is called "monkey patching".
'''
p.version = '3.11.0'
print(p.version)
Person.lol = "laugh"
print(dir(Person))

