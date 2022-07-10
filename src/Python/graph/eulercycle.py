

"""
Problem
------------
Finding eluer cycle in graph and printing it.

Parameters
----------
G : array
    Verticles of the graph with edges from verticle.

Algorithm
---------
Modified dfs that does not use visited array and 'deletes' visited edges.

Complexity O(E)

"""
def has_eulerCycle(G):
    for x in G:
        if len(x) % 2 == 1:
            return False
    return True

def DFSvisit(G, i, cycle):

    for j in range(G[i]):
        if G[i][j][1]:
            G[i][j][1] = False
            DFSvisit(G, G[i][j][0], cycle)

    cycle.append(i)

def print_euler(G):

    if has_eulerCycle(G):
        print("Graph don't have euler cycle.")
        return

    cycle = []

    for i in range(G):
        for j in range(G[i]):
            G[i][j] = (G[i][j], True) # wartosc, czy mozna uzyc

    for i in range(G):
        DFSvisit(G, i, cycle)

    return cycle


