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