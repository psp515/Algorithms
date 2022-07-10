
"""
Problem
------------

Finding longest increasing/decreasing sequence.

Parameters
----------
arr : array
    array of elements

Algoirthm
---------
For i-th element search j in 0...i-1 that sequence to j is the longest and arr[j] < arr[i].

Complexity: O(n^2)

"""

def lis(arr):
    n = len(arr)
    f = [1 for _ in range(n)]
    p = [-1 for _ in range(n)]
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if f[j] + 1 > f[i] and arr[i] > arr[j]:
                f[i] = f[j] + 1
                p[i] = j
        if f[i] > f[max_index]:
            max_index = i

    return max_index, p