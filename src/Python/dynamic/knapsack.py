

# f[i][b] -> i - item index, b - package size

# items - sizes, cost - item price, maxsize - backpack size
def knapsack(items, cost, maxsize):
    n = len(items)
    f = [[0 for _ in range(maxsize + 1)] for _ in range(n)]

    for i in range(maxsize + 1):
        if i - items[0] >=0:
            f[0][i] = cost[0]


    for i in range(1, n):
        for j in range(maxsize+1):
            f[i][j] = max(f[i - 1][j], f[i - 1][j - items[i]] + cost[i])


    return f[-1][-1]