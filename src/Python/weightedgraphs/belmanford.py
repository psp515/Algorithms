
"""
Problem
------------


Parameters
----------


Algoirthm
---------

Complexity O()

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
