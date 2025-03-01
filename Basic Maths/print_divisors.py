def divisors(n):  # O(N)
    divisors = []
    i = 1

    while i <= n:
        if n % i == 0:
            divisors.append(i)
        
        i += 1
    
    return divisors


print(divisors(36))
print(divisors(1001))
print(divisors(4))
print(divisors(25))


# OR optimized way
import math


def divisors(n):  # T.C: O(srqt(N))
    divisors = []
    sqrt = int(math.sqrt(n)) + 1  # calculating sqrt also takes some time

    for i in range(1, sqrt, 1):
        if n % i == 0:
            quotient = n // i
            divisors.append(i)
            if quotient == i:
                continue
            divisors.append(n // i)
    
    return divisors


print(divisors(36))
print(divisors(1001))
print(divisors(4))
print(divisors(25))

