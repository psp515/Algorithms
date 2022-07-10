import math
"""
Problem
------------
Finding minimal paths to from each verticle to every other verticle.

Parameters
----------
G : array
    Martrix of routes with weights.


Algorithm
---------
Finds minmal route from i to k and from k to j.

Complexity: O(V^3)

"""
def floyd_warshall(G):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    return G
