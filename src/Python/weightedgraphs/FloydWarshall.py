import math
"""
Problem
------------


Parameters
----------



Algoirthm
---------

Complexity O()

"""
def floyd_warshall(G):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    return G
