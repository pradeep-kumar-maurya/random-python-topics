def get_digits(n):
    digits = []
    
    while n > 0:  # T.C = O(log n base 10) because n=10 
        digits.append(n % 10)
        n = n // 10

    return digits


print(get_digits(7789))



import math

def get_no_of_digits(n):
    # dividing by 10 is nothing but log base to 10 of the number "n"
    return int(math.log(n, 10)) + 1


print(get_no_of_digits(7789))
