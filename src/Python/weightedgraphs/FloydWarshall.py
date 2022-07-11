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


def _test(G, V):
    ans = floyd_warshall(G)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- floyd_warshall ------------")
    graph = [[0, 3, 8, math.inf, -4],
         [math.inf, 0, math.inf, 1, 7],
         [math.inf, 4, 0, math.inf, math.inf],
         [2, math.inf, -5, 0, math.inf],
         [math.inf, math.inf, math.inf, 6, 0]]
    ans = [[0, 1, -3, 2, -4],
           [3, 0, -4, 1, -1],
           [7, 4, 0, 5, 3],
           [2, -1, -5, 0, -2],
           [8, 5, 1, 6, 0]]
    _test(graph, ans)
