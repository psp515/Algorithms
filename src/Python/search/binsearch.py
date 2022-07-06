


def bin_search(arr, value):
    l, r = 0, len(arr) - 1

    while l <= r:
        q = (l + r) // 2

        if arr[q] == value:
            return q
        elif arr[q] > value:
            r = q - 1
        else:
            l = q + 1

    return -1