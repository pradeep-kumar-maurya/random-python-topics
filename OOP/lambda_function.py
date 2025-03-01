import uuid

'''
lambda functions are anonymous functions with no name which does simple computations with the parameters passed.
a, b are the inputs of the lambda function and a + b is returned by the lambda function.
'''
add = lambda a, b: a + b

print(add(10, 20))

# below we are directly calling the lambda function with 10 as the parameter
print((lambda x: x ** 2)(10))

# below lambda function takes an uuid4 guid and then add "I" at the front and replaces '-' with ''.
print((lambda uui4_guid: ('I' + uui4_guid).replace('-', ''))(str(uuid.uuid4())))

# we can use lambda functions when using map on any iterable
nos = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, nos))  # squares the numbers in nos list
print(result)

# lambda with filter function
nos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nos = list(filter(lambda x: x % 2 == 0, nos))  # checks if the number is even
print(even_nos)

