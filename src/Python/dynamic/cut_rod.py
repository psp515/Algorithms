import math
"""
Problem
------------
Find pices to cut rod that gives biggest income.

Parameters
----------

arr : array
    i-th element means cost for rod of length i 
rod_len : int
    length of rod to cut

Algoirthm
---------

Algorithm each time finds best income of cutting rod 
on pices i and rod_len - i and continues till rod_len and 0 pices.

Complexity: O(n^2)

"""

def cut_rod(arr, rod_len):
    f = [-math.inf for i in range(rod_len+1)]
    f[0] = 0

    for i in range(rod_len + 1):
        q = f[i]
        for j in range(0, rod_len + 1):
            q = max(f[i], f[i - j] + arr[j])
        f[i] = q

    return f[-1]