def reverse(n):
    ans = []
    is_trailing = True

    while n > 0:
        digit = n % 10

        if digit == 0 and is_trailing:
            pass

        else:
            is_trailing = False
            ans.append(digit)

        n = n // 10

    return ans


print(reverse(7789))
print(reverse(100400))


# OR

def reverse(n: int):
    multiplier = 10 ** (len(str(n)) - 1)
    ans = 0

    while n > 0:
        ans += (n % 10) * multiplier
        n = n // 10
        multiplier = multiplier // 10

    return ans


print(reverse(7789))
print(reverse(100400))

# OR

def reverse(n):
    reverse_num = 0

    while n > 0:
        last_digit = n % 10
        reverse_num = (reverse_num * 10) + last_digit
        n = n // 10
    
    return reverse_num


print(reverse(7789))
print(reverse(100400))
