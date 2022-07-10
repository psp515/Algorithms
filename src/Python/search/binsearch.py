

"""
Problem
------------
Find index of element that has searched value.

Parameters
----------
arr : array
    sorted array of elements
value : int
    searched value

Algoirthm
---------
Binary search compares the target value to the middle element of the array.
If they are not equal, algorithm eliminates one half of the array and does
the same to the left half of array.

Complexity O(logn)

"""
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