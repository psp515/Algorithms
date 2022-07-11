import math
import queue

"""
Problem
------------
Finding minimal spanning tree.

Parameters
----------
G : array
    Edges in graph.


Algorithm
---------
Adds lowest possible edge to mst each time till takes V-1 edges.

Complexity: O(ElogV)

"""

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

def _test(G, V):
    ans = prim(G)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- prim ------------")
    graph = [[[1, 1], [2, 2]],
         [[0, 1], [3, 1], [4, 3]],
         [[0, 2], [3, 3]],
         [[1, 1], [2, 3], [4, 1], [5, 2]],
         [[1, 3], [3, 1], [5, 4]],
         [[3, 2], [4, 4], [6, 1], [7, 5]],
         [[5, 1], [7, 2]],
         [[5, 5], [6, 2]]]
    ans = [(1, 0), (2, 0), (3, 1), (4, 3), (5, 3), (6, 5), (7, 6)]
    _test(graph, ans)