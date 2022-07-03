import math
import queue

def prim(G):
    Q = queue.PriorityQueue()
    wages = [math.inf for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    Q.put((0, 0))

    while len(Q.queue) != 0:
        prior, v = Q.get()
        visited[v] = True
        for el in G[v]:
            u, w = el
            if not visited[u]:
                if wages[u] > w:
                    wages[u] = w
                    parent[u] = v
                    Q.put((wages[u], u))

    res = []
    for i in range(len(parent)):
        if parent[i] is not None:
            res.append((i, parent[i]))

    return res