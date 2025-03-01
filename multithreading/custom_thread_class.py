import time
from threading import Thread


class MyThread(Thread):  # Inheriting the parent Thread class
    def __init__(self, target=None, args: tuple = (), kwargs: dict = {}):
        super().__init__()  # initialize the parent Thread class
        self.target = target  # the function that needs to be executed when running a thread
        self.args = args  # parameters for the target function provided
        self.kwargs = kwargs

    # run method gets executed when thread.start() is called
    def run(self):
        self.target(*self.args)

    def join(self, thread_name: str):
        print(thread_name)
        super().join()  # Thread class join method must be called


def add_to_list(data: list, result: list):
    for i in data:
        result.append(i)
        time.sleep(0.00000000001)


def print_message(name, times):
    for i in range(times):
        print(f"{name}: Message {i+1}")


# thread1 = MyThread(target=print_message, args=("A", 100))
# thread2 = MyThread(target=print_message, args=("B", 200))

nos1 = [i for i in range(10)]
nos2 = [i for i in range(10, 20, 1)]  # range(i=10, i<20, i++)
result = []

thread1 = MyThread(target=add_to_list, args=(nos1, result))
thread2 = MyThread(target=add_to_list, args=(nos2, result))

thread1.start()
thread2.start()

thread1.join('joining Thread-1')
thread2.join('joining Thread-2')

# thread1.join()
# thread2.join()

print(result)
print(result == [i for i in range(20)])
