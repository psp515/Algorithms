
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


def _test(G, V, s, v):
    ans = belmanford(G, s, v)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- belmanford ------------")
    graph = [(0, 1, 6), (0, 4, 7), (1, 2, 5), (1, 3, -4), (1, 4, 8), (2, 1, -2), (3, 0, 2), (3, 2, 7), (4, 3, 9),
         (4, 2, -3)]
    ans = [-1, 2, 4, 1, 0]
    _test(graph, ans, 0, 5)