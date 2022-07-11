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

Algorithm
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
            if j - items[i] >= 0:
                f[i][j] = max(f[i - 1][j], f[i - 1][j - items[i]] + cost[i])


    return f[-1][-1]

def _test(items, cost, maxsize, V):
    ans = knapsack(items, cost, maxsize)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- knapsack ------------")
    items = [5, 4, 3, 2, 1, 1]
    cost = [10, 10, 2, 5, 6, 5]
    maxsize = 10
    ans = 26
    _test(items, cost, maxsize, ans)

    items = [5, 4, 6, 2, 10]
    cost = [10, 10, 2, 5, 6]
    maxsize = 15
    ans = 25
    _test(items, cost, maxsize, ans)