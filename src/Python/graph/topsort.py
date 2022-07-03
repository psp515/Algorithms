
def topsortvisit(G, v, visited, sorted):
    visited[v] = True
    for u in G[v]:
        if visited[u] == False:
            topsortvisit(G, u, visited, sorted)
    sorted.append(v)

def topsort(G):
    sorted = []
    visited = [False for _ in range(len(G))]

    for i in range(len(G)):
        if visited[i] == False:
            topsortvisit(G, i, visited, sorted)

    return sorted[::-1]

