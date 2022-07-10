import math
from sorting import sorting_test
from sorting import quicksort

"""
Problem
------------
Sorting array.

Parameters
----------

arr : Array
    array of items to sort 
    
Algorithm
---------

Algorithms simply creates n buckets and each bucket menas elements range. We are asignings array elements to buckets 
then we have to sort each bucket (but each bucket contains few elements). At the end we rewrite elements

Best Complexity O(n)
Avg. Complexity: O(n)
Worst Complexity O(n^2)

* we have to assume that elements are from uniform distribution 


"""

def bucketsort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n+1)]
    m = max(arr)
    for i in range(n):
        index = math.floor(n * arr[i] / m)
        buckets[index].append(arr[i])

    for bucket in buckets:
        quicksort.quicksort2(bucket)

    n_arr = []

    for bucket in buckets:
        for x in bucket:
            n_arr.append(x)

    for i in range(n):
        arr[i] = n_arr[i]

def test():
    sorting_test.sorting_test(bucketsort)