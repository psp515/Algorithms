# most to krawędź która rozspójnia graf
import math


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


