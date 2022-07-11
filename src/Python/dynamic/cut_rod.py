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

Algorithm
---------

Algorithm each time finds best income of cutting rod 
on pices i and rod_len - i and continues till rod_len and 0 pices.

Complexity: O(n^2)

"""

def cut_rod(arr, n):
    f = [-1 for _ in range(0, n + 1)]
    f[0] = 0

    for i in range(1, n + 1):
        q = -math.inf
        for j in range(1, i + 1):
            q = max(q, f[i - j] + arr[j - 1])
        f[i] = q
    return f[n]

def _test(G, V):
    ans = cut_rod(G, len(G))
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- cut_rod ------------")
    array = [2, 5, 7, 8, 10, 12]
    ans = 15
    _test(array, ans)

