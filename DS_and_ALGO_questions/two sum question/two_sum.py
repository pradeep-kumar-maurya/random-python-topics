def two_sum(my_list, target):
    my_dict = {}

    for i in range(len(my_list)):
        my_dict[my_list[i]] = i

    for i in range(len(my_list)):
        j = my_dict.get(target - my_list[i])
        if j and j > i:
            return [i, j]


indexes = two_sum([3, 2, 4], target=6)
print(indexes)
