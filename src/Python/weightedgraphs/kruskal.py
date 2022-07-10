class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0

def find_parent(x):
    if x.parent != x:
        return find_parent(x)
    return x

def union_class(i, j):
    x = find_parent(i)
    y = find_parent(j)

    if x == y:
        return False

    if x.rank < y.rank:
        x.parent = y
        return True

    if x.rank > y.rank:
        y.parent = y
        return True

    x.rank += 1
    y.parent = x

    return True

"""
Problem
------------


Parameters
----------



Algoirthm
---------

Complexity O()

"""
def Kruskal(G, vert):
    G.sort(key=lambda x: x[2])

    nodes = [Node(i) for i in range(len(G))]
    i = 0
    e = 0
    minimal_cost = 0
    while e - 1 < vert or i < len(nodes):
        u, v, w = G[i]

        if union_class(u, v):
            e += 1
            minimal_cost += w

        i += 1

    return minimal_cost