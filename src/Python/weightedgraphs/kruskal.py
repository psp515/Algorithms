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
First we sort edges by weight.
We take i-th element and checks if there will be a cycle in graph if no we take edge.

Complexity: O(ElogV)

"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(x, y, parent, rank):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def kruskal(G, verticles):
    G.sort(key=lambda x: x[2])

    e = 0
    i = 0
    parent = []
    rank = []
    for node in range(len(G)):
        parent.append(node)
        rank.append(0)

    minimumCost = 0

    while e < verticles - 1 and i < len(G):
        u, v, w = G[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e = e + 1
            union(x, y, parent, rank)
            minimumCost += w

    return minimumCost

def _test(G, V, v):
    ans = kruskal(G, v)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- Kruskal ------------")
    G = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    _test(G, 19, 4)

    G = [(0, 1, 4), (0, 7, 8), (1, 7, 11), (1, 2, 8), (2, 8, 2), (2, 5, 4), (2, 3, 7), (3, 4, 9), (3, 5, 14),
         (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 5), (7, 8, 7)]
    _test(G, 37, 9)