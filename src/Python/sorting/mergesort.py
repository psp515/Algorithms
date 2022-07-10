from sorting import sorting_test
import math

"""
Problem
------------
Sorting array.

Parameters
----------

arr : Array
    array of items to sort 
    
Algoirthm
---------

Algorithm first divides array into two subarrays and repeats the same with each half till one element
then algorithm mergres two sorted sub arrays into one and repats it till all elements are sorted.

Best Complexity O(nlogn)
Avg. Complexity: 0(nlogn)
Worst Complexity O(nlogn)

"""
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