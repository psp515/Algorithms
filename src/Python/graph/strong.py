

"""
Problem
------------
Finding subgrafs that for verticle v you can always visit u and from u you can visit v.

Parameters
----------
G : array
    Verticles of the graph with edges from verticle.

Algoirthm
---------

First algorithm does similar thing that topological sort does.
Secondly graph is transposed.
Thirdly it does modified dfs in order of topological sort and appends processed verticle.

Complexity O(V)

"""
def DFS_visit(G, i, visited, stack):
    visited[i] = True

    for j in G[i]:
        if visited[j] == False:
            DFS_visit(G, j, visited, stack)

    stack.append(i)

def transpose(G):
    g = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G[i])):
            g[j].append(i)

    return g

def DFS_visit2(G, x, visited, strong, i):
    visited[x] = True
    strong[i].append(x)
    for u in G[x]:
        if visited[u] == False:
            DFS_visit2(G, u, visited, strong, i)

def strong_components(G):

    visited = [False for _ in range(len(G))]
    stack = []

    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G, i, visited, stack)

    G2 = transpose(G)

    visited = [False for _ in range(len(G))]

    strong = []
    i = 0
    while stack:
        x = stack.pop()
        if visited[x] == False:
            strong.append([])
            DFS_visit2(G2, x, visited, strong, i)
            i += 1

    return strong


