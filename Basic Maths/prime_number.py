import math

def prime(n):
    if n == 1:
        return False

    count = 0
    sqrt = int(math.sqrt(n)) + 1

    for i in range(1, sqrt, 1):
        if n % i == 0:
            count += 1
        
        if count > 1:
            return False
        
    return True


print(prime(1000000007))
