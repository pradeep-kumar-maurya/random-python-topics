def count_digits(n):
    count = 0

    while n > 0:
        count += 1
        n = n // 10

    return count

def check_armstrong(n):
    no_of_digits = count_digits(n)
    original_num = n
    ans = 0

    while n > 0:
        last_digit = n % 10
        ans += (last_digit ** no_of_digits)
        n = n // 10

    if ans == original_num:
        return True
    else:
        return False
    

print(check_armstrong(371))
print(check_armstrong(370))
print(check_armstrong(407))
print(check_armstrong(1634))
print(check_armstrong(8208))
print(check_armstrong(9474))
print(check_armstrong(35))
