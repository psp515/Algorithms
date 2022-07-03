from sorting import sorting_test

def countingsort(arr):
    n = len(arr)
    count_arr = [0 for _ in range(n)]
    sorted_arr = [0 for _ in range(n)]

    for i in arr:
        count_arr[i] += 1

    for i in range(1, n):
        count_arr[i] += count_arr[i-1]

    for i in range(n):
        sorted_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1

    for i in range(n):
        arr[i] = sorted_arr[i]


def test():
    sorting_test.sorting_test(countingsort, [1000000], False, 0, 9)