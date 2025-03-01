import pickle


class Fruits:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')


if __name__ == '__main__':
    fruit = Fruits('banana', 100)
    fruit.describe_fruit()

    # serializing the fruit object i.e. converting an object to a byte stream
    with open('data.pickle', 'wb') as file:
        pickle.dump(fruit, file)  # dump the fruit object into the pickle file as a byte stream

    # deserializing the fruit object i.e. converting a byte stream to an object
    with open('data.pickle', 'rb') as file:
        data: Fruits = pickle.load(file)  # load the fruit object back from the pickle file
        print(data, type(data))
        data.describe_fruit()
