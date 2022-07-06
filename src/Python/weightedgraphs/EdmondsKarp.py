from collections import deque

def get_path(G, Gflow, s, t, n):
    parent = [-1 for _ in range(n)]
    min_flow = [0 for _ in range(n)]
    min_flow[s] = float('inf')

    q = deque()
    q.append(s)

    while q:
        v = q.popleft()
        for i in range(len(G[v])):
            if G[v][i] == 0:
                continue
            diff = G[v][i] - Gflow[v][i]
            if diff <= 0 or parent[i] != -1:
                continue
            min_flow[i] = min(min_flow[v], diff)
            parent[i] = v
            q.append(i)
            if i == t:
                return min_flow[t], parent


    return 0, parent

# edmonds_karp
def get_flow(G, s, t, n):
    r_matrix = [[0 for _ in range(n)] for _ in range(n)]
    maxflow = 0
    while True:
        flow, path = get_path(G, r_matrix, s, t, n)
        if flow == 0:
            break
        maxflow += flow
        x = t

        while s != x:
            p = path[x]
            r_matrix[p][x] = r_matrix[p][x] + flow
            r_matrix[x][p] = r_matrix[x][p] - flow
            x = p

    return maxflow