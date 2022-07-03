from queue import PriorityQueue
import math

def dijkstra(G, s):
    n = len(G)
    pq = PriorityQueue()
    parent = [-1 for _ in range(n)]
    dist = [math.inf for _ in range(n)]
    pq.put((0, s))
    dist[s] = 0

    while len(pq.queue) != 0:
        dis, v = pq.get()
        for z in G[v]:
            u, w = z
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                parent[u] = v
                pq.put((dist[u], u))

    return parent

# matrix

def min_val(G, dist, set):
    min = math.inf
    min_index = -1
    for u in range(len(G)):
        if dist[u] < min and set[u] == False:
            min = dist[u]
            min_index = u

    return min_index

def dijkstra2(G, s):
    n = len(G)
    dist = [math.inf for _ in range(n)]
    dist[s] = 0
    set = [False for _ in range(n)]

    for count in range(n):
        i = min_val(G, dist, set)
        set[i] = True

        for j in range(n):
            weight = G[i][j]
            if weight != math.inf and weight > 0 and not set[j]:
                if weight + dist[i] < dist[j]:
                    dist[j] = dist[i] + weight


