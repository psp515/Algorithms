from search import search_tests
"""
Problem
------------
Find i-th element in array.

Parameters
----------
arr : array
    array of elements
k : int
    searched number

Algorithm
---------
Algorithm takes a pivot and sorts array in two subarrays bigger than pivot and lower
than pivot then cheks if pivot is searched element, if not it continues to do the same. 

Complexity O(n)
"""

def partition(arr, l, r):
     i = l
     pivot = arr[r]
     for j in range(l, r):
         if arr[j] < pivot:
             arr[i], arr[j] = arr[j], arr[i]
             i += 1

     arr[i], arr[r] = arr[r], arr[i]

     return i

def select(arr, k):
    l, r = 0, len(arr)-1

    while l <= r:
        q = partition(arr, l, r)
        if q == k:
            return arr[q]
        elif k < q:
            r = q - 1
        else:
            l = q + 1

def test():
    search_tests.quickselect_test(select)