# most to krawędź która rozspójnia graf
import math

"""
Problem
------------
Finding bridges (deleting this verticle breaks graph) in graph.

Parameters
----------
G : array
    Verticles of the graph with edges from verticle.

Algorithm
---------
Based on dfs, algorithm visit verticles and perform low function.
low[parent] = min(dist[parent], low[connected verticles], dist[connected verticles])
and if certain condittons occure we can know if edge is bridge.

Complexity O(V)

"""
def DFS_visit(G, u, visited, disc, low, parent, bridges):
    global time
    time += 1
    disc[u] = time
    low[u] = time
    visited[u] = True

    for v in G[u]:
        if visited[v] == False:
            parent[v] = u
            DFS_visit(G, v, visited, disc, low, parent, bridges)
            low[u] = min(low[u], low[v])

            if low[v] > disc[u]:
                bridges.append((u, v))

        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

def find_bridges(G):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    disc = [math.inf for _ in range(len(G))]
    low = [math.inf for _ in range(len(G))]

    global time
    time = -1

    bridges = []

    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G, i, visited, disc, low, parent, bridges)

    return bridges


def _test(G, V):
    ans = find_bridges(G)
    ans.sort(key=lambda x: x[0])
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- Bridges ------------")
    graph = [[1, 2, 3], [0, 2], [0, 1], [0, 4], [3]]
    ans = [(0, 3), (3, 4)]
    _test(graph, ans)

    graph = [[1], [2], [3], []]
    ans = [(0, 1), (1, 2), (2, 3)]
    _test(graph, ans)

    graph = [[1, 2], [2, 3, 4, 6], [0, 1], [1, 5], [1, 5], [3, 4], [1]]
    ans = [(1, 6)]
    _test(graph, ans)


