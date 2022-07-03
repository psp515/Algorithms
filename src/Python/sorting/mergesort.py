from sorting import sorting_test
import math

# O(nlogn)


def _merge(arr, l, q, r):
    L = [arr[l + i] for i in range(0, q - l + 1)]
    R = [arr[q + i + 1] for i in range(0, r - q)]
    L.append(math.inf)
    R.append(math.inf)

    i, j = 0, 0

    for k in range(l, r + 1):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def _mergesort(arr, l , r):
    if l < r:
        q = (l + r) // 2
        _mergesort(arr, l, q)
        _mergesort(arr, q + 1, r)
        _merge(arr, l, q, r)

def mergesort(arr):
    _mergesort(arr, 0, len(arr)-1)

def test():
    sorting_test.sorting_test(mergesort)