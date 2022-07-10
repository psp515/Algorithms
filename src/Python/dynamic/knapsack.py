
"""
Problem
------------
Finding most valuable items to take that weight less than maxsize.

Parameters
----------

items : arr
    item sizes
cost : arr
    item price
maxsize : int
    backpack size

Algoirthm
---------

Finding most valuable combination to take to i-th item and j of backpack size.

Complexity: O(n^2)
"""

def knapsack(items, cost, maxsize):
    n = len(items)
    f = [[0 for _ in range(maxsize + 1)] for _ in range(n)]

    for i in range(maxsize + 1):
        if i - items[0] >= 0:
            f[0][i] = cost[0]


    for i in range(1, n):
        for j in range(maxsize+1):
            f[i][j] = max(f[i - 1][j], f[i - 1][j - items[i]] + cost[i])


    return f[-1][-1]