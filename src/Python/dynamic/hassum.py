"""
Problem
------------
Finding if array has combination that sums to T.

Parameters
----------
arr : array
    array of numbers
T : int
    searched sum

Algorithm
---------
Algorithm takes i-th element and checks if each possible combination of arr[i] + j is
possible to create if yes it is saved in array.

Complexity O(n^2)
"""

def containssum(arr, T):
    n = len(arr)
    f = [[False for _ in range(T + 1)] for _ in range(n)]

    for i in range(n):
        f[i][0] = True

    for i in range(n):
        for j in range(1, T+1):
            if j >= arr[j]:
                f[i][j] = f[i-1][j] or f[i-1][j-arr[j]]
            else:
                f[i][j] = f[i-1][j]

    return f[-1][-1]