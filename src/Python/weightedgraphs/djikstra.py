from queue import PriorityQueue
import math
"""
Problem
------------
Finding shortest paths to verticles from s

Parameters
----------
G : array
    Verticles of the graph with edges from verticle and each edge has positive weight.
s : int 
    Index of starting verticle.

Algorithm
---------

From PQ pop verticla that has minimal path from first verticle and relax each edge
from this verticle if edge is relaxed put verticle to PQ. Then again pop verticle and repeat.
    
Complexity: O(ElogV)

"""
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

# matrix implementation
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


def _test(G, V, s):
    ans = dijkstra(G, s)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- dijkstra ------------")
    graph = [[(1, 10), (3, 5)],
         [(0, 10), (2, 1)],
         [(1, 1), (3, 5)],
         [(0, 5), (2, 5)]]
    ans = [-1, 0, 3, 0]
    _test(graph, ans, 0)

    graph = [[(1, 4), (7, 8)],
         [(1, 4), (7, 11), (2, 8)],
         [(1, 8), (3, 7), (5, 4), (8, 2)],
         [(2, 7), (4, 9), (5, 15)],
         [(4, 9), (4, 10)],
         [(3, 14), (2, 4), (6, 2), (4, 10)],
         [(5, 2), (8, 6), (7, 1)],
         [(0, 8), (6, 1), (7, 8)],
         [(2, 2), (7, 7), (6, 6)]]
    ans = [-1, 0, 1, 2, 5, 6, 7, 0, 2]
    _test(graph, ans, 0)

