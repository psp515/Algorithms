"""
Problem
------------
Sort elements that you can always go from elements on the left to element on the right

Parameters
----------
G : array
    Verticles of the graph with edges from verticle.

Algorithm
---------
Based on dfs, visits verticle and if it is processed - appended to the end of sorted list.
On the end list of verticles must be reversed.

Complexity O(V)

"""

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

def _test(G, V):
    ans = topsort(G)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- topsort ------------")
    graph = [[], [0], [0], [0]]
    ans = [3, 2, 1, 0]
    _test(graph, ans)

    graph = [[], [], [3], [1], [0, 1], [0, 2]]
    ans = [5, 4, 2, 3, 1, 0]
    _test(graph, ans)


