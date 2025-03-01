from abc import ABC, abstractmethod


class Computer(ABC):  # Computer is an abstract class
    @abstractmethod
    def process(self):  # process is an abstract method
        pass

    def add(self):  # add is a normal method
        print('adding nos')


class Laptop(Computer):  # Laptop must extend Computer i.e. abstract class
    def process(self):  # definition of the abstract method
        print('laptop is running')


l = Laptop()
l.process()
l.add()
