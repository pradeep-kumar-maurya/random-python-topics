class Person:
    language = 'python'

    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        self.full_name = f"{self.fn} {self.ln}"

    # this is an instance method
    def introduction(self):
        print(self)
        print(self.language)  # language attribute can be accessed from the object
        print(f"Name: {self.full_name}")

    @staticmethod
    def how_are_you():  # static method does not have access to any object or class attributes and methods
        print("I'm doing good. Thanks for asking!")

    @classmethod
    def what_are_you_doing():  # NOTE:- below method does not throw any error unless called
        print("I'm learning OOP in python")

    @classmethod
    def what_movie_do_you_like(cls):
        print(cls)
        print(cls.language)  # cls can only access class attributes and methods but not the object attributes
        cls.how_are_you()
        print("I like horror movies")

    def __str__(self) -> str:
        return f'{self.full_name}'

    def __repr__(self):
        return f'{self.__class__.__name__}(fn={self.fn}, ln={self.ln}, full_name={self.full_name})'


p = Person('pradeep', 'maurya')
# p.introduction()
# Person.how_are_you()
# Person.what_are_you_doing()
# Person.what_movie_do_you_like()

print(p)
print(repr(p))
