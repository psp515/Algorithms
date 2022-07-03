from sorting import sorting_test

def left(i):
    return i*2 + 1

def right(i):
    return i*2 + 2

def parent(i):
    return i//2

def repair_heap(arr, n, i):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and arr[l] > arr[max_ind]:
        max_ind = l
    if r < n and arr[r] > arr[max_ind]:
        max_ind = r

    if max_ind != i:
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
        repair_heap(arr, n, max_ind)

def build_heap(arr, n):
    for i in range(parent(n), -1, -1):
        repair_heap(arr, n, i)

def heapsort(arr):
    n = len(arr)
    build_heap(arr, n)

    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        repair_heap(arr, i, 0)

def test():
    sorting_test.sorting_test(heapsort,[10],True)