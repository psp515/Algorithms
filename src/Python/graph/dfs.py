"""
Problem
------------
Finding all possible routes in graph.

Parameters
----------
G : array
    Verticles of the graph with edges from verticle.

Algorithm
---------
Simply if verticle is not visited algorithm visits it.

Complexity O(V)

"""
def dfsVisit(G, u, visited, visittime, quittime, parent):
    global time
    time += 1
    visited[u] = True
    visittime[u] = time

    for i in G[u]:
        if visited[i] == False:
            parent[i] = u
            dfsVisit(G, i, visited, visittime, quittime, parent)
    time += 1
    quittime[u] = time

def dfs(G):
    global time
    time = 0
    n = len(G)

    visited = [False for _ in range(n)]
    visittime = [0 for _ in range(n)]
    quittime = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
            dfsVisit(G, i, visited, visittime, quittime, parent)

    return G

