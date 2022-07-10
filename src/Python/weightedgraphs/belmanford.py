
"""
Problem
------------
Finding shortest paths to verticles.

Parameters
----------
G : array
    Edges of the graph and does not contain cycle that its path is lower than 0.

Algorithm
---------
Perform relaxation for each combination of verticle and edge.

Complexity O(VE)

"""
def belmanford(G, s, v):
    n = len(G)
    parent = [-1 for _ in range(v)]
    dist = [float('inf') for _ in range(v)]
    dist[s] = 0

    for i in range(v):
        for j in range(n):
            x, y, w = G[j]
            if dist[y] > dist[x] + w:
                dist[y] = dist[x] + w
                parent[y] = x

    for j in range(n):
        x, y, w = G[j]
        if dist[y] > dist[x] + w:
            print("Wrong Graph")
            break

    return parent
