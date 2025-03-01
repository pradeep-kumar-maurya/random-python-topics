class A:
    count = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        cls.count += 1
        return instance
    
    @classmethod
    def get_count(cls):
        return cls.count
    

a1 = A()
a2 = A()
print(A.get_count())
a3 = A()
print(A.get_count())
