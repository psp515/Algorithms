import math

"""
Problem
------------
Finding articulation point (if we delete this verticle we enlarge number of scc) in graph.

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

def DFS_visit(G, u, visited, disc, low, parent, ap):
    child = 0
    global time
    time += 1
    disc[u] = time
    low[u] = time
    visited[u] = True

    for v in G[u]:
        if visited[v] == False:
            parent[v] = u
            child += 1
            DFS_visit(G, v, visited, disc, low, parent, ap)

            low[u] = min(low[u], low[v])

            if (parent[u] != -1 and low[v] >= disc[u]) or (child > 1 and parent[u] == -1):
                ap[u] = True

        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

def articulation(G):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    disc = [math.inf for _ in range(len(G))]
    low = [math.inf for _ in range(len(G))]

    global time
    time = -1

    ap = [False for _ in range(len(G))]

    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G, i, visited, disc, low, parent, ap)

    ret = []
    for i in range(len(G)):
        if ap[i] == True:
            ret.append(i)

    return ret

def test(G, V):
    ans = articulation(G)
    print("Is valid: ", ans == V, "Ans: ", ans)


def main_test():
    print("Articulation")
    graph = [[1, 2, 3], [0, 2], [0, 1], [0, 4], [3]]
    ans = [0,3]
    test(graph, ans)

    graph = [[1], [2], [3],[]]
    ans = [1, 2]
    test(graph, ans)

    graph = [[1, 2], [2, 3, 4, 6], [0, 1], [1, 5], [1, 5], [3, 4], [1]]
    ans = [1]
    test(graph, ans)