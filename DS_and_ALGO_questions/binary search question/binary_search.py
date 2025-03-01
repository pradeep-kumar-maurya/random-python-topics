def search(my_list):
    left = 0
    right = len(my_list) - 1
    mid = (left + right) // 2

    while left <= right:
        if my_list[mid] == mid:
            return mid, my_list[mid]

        elif my_list[mid] - mid > 0:
            right = mid - 1
            mid = (left + right) // 2

        else:
            left = mid + 1
            mid = (left + right) // 2

    return None, None


# TODO - I have assumed that there will only be 1 element in the entire list whose value is same as its index
a = [-1, 0, 1, 2, 3, 4, 6]
index, num_at_index = search(a)
print(f'index = {index}, num_at_index = {num_at_index}')

# if index is None that means there is no such element with its index same as element
if index is not None:
    print(a[index] == num_at_index)  # assures if our output is correct
