class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            return cls.instance
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        pass


a1 = Singleton()
a2 = Singleton()

print(a1 is a2)

