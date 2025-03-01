class A:

    def __new__(cls):
        instance = super().__new__(cls)
        return instance
    
    def __init__(self):
        self.count = 1

    def get_count(self):
        return self.count


a1 = A()
a2 = A()
print(a1.get_count())
print(a2.get_count())
