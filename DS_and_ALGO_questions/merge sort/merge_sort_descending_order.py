def merge(arr, start, mid, end):  # O(N)
    temp_arr = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] >= arr[j]:
            temp_arr.append(arr[i])
            i += 1
        else:
            temp_arr.append(arr[j])
            j += 1

    while i <= mid:
        temp_arr.append(arr[i])
        i += 1

    while j <= end:
        temp_arr.append(arr[j])
        j += 1

    for i in range(len(temp_arr)):
        arr[i + start] = temp_arr[i]


def merger_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merger_sort(arr, start, mid)  # left half
        merger_sort(arr, mid+1, end)  # right half
        merge(arr, start, mid, end)  # final merge array


arr = [4, 3, 1, 2]
merger_sort(arr, 0, len(arr) - 1)
print(arr)
