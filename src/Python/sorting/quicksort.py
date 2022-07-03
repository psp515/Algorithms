from sorting import sorting_test

# O(nlogn)


def _partition(arr, l, r):
    i = l
    for j in range(l, r):
        if arr[j] <= arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

def _quicksort(arr, l, r):
    if l < r:
        q = _partition(arr, l, r)
        _quicksort(arr, l, q - 1)
        _quicksort(arr, q + 1, r)

def quicksort(arr):
    _quicksort(arr, 0, len(arr)-1)

def quicksort2(arr):
    stack = []
    stack.append( (0, len(arr)-1) )
    while stack:
        l, r = stack.pop()
        if l < r:
            q = _partition(arr, l, r)
            stack.append( (l, q - 1) )
            stack.append( (q + 1, r) )


def test():
    sorting_test.sorting_test(quicksort)
    sorting_test.sorting_test(quicksort2)