from collections import deque

"""
Problem
------------
Finding all posible verticles from verticle s

Parameters
----------
G : array
    Verticles of the graph with edges from verticle.
s = None : int
    index of starting verticle

Algorithm
---------
Algorithm does the waves and in each wave visits few verticles. (All verticles that are avaliable from previous wave.)

Complexity O(V)

"""
def bfs(G, s = None):
    n = len(G)

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visittimes = [0 for _ in range(n)]

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
                visittimes[v] = time
                q.append(v)

    return visited, parent, visittimes

def _test(G, V, s):
    v, p, vt = bfs(G, s)
    print("Is valid: ", vt == V, "Ans: ", vt)

def test():
    print("------------- BFS ------------")

    graph = [[1,4], [0,2,3], [1], [1], [0]]
    ans = [0,1,2,2,1]
    _test(graph, ans, 0)

