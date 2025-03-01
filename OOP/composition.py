class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def start(self):
        self.engine.start()


c = Car()
c.start()
