

def _partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

def _quicksort(arr, l, r):

    if l < r:
        q = _partition(arr, l, r)
        _quicksort(arr, l, q)
        _quicksort(arr, q + 1, r)

def quicksort(arr):
    _quicksort(arr, 0, len(arr))

def test():
    pass