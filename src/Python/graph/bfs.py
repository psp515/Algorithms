from collections import deque

# Odzwiedza wszystkie wierzchołki do których da się dojść z s
def bfs_list(G, s = None):
    n = len(G)

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visittimes = [-1 for _ in range(n)]

    q = deque()
    q.append(s)
    visited[0] = True
    time = 0

    while q:
        time += 1
        u = q.popleft()
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                parent[v] = u
                visittimes[s] = time
                q.append(v)

    return visited, parent, visittimes
