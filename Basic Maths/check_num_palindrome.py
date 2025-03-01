def check_palindrome(n):
    original_num = n
    reverse_num = 0

    while n > 0:
        last_digit = n % 10
        reverse_num = (reverse_num * 10) + last_digit
        n = n // 10

    if original_num == reverse_num:
        return True
    else:
        return False
    

print(check_palindrome(121))
print(check_palindrome(1))
print(check_palindrome(000))
print(check_palindrome(123321))
print(check_palindrome(12321))
print(check_palindrome(12341))