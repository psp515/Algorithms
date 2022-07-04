

def bigknapsack(widths, heights, cost, maxheight, maxwidth):
    n = len(widths)
    f = [[[0 for _ in range(maxwidth + 1)] for _ in range(maxheight + 1)] for _ in range(n)]

    for w in range(maxheight + 1):
        for h in range(maxwidth + 1):
            if w - widths[0] >= 0 and h - heights[0] >= 0:
                f[0][w][h] = cost[0]

    for i in range(1, n):
        for j in range(maxheight + 1):
            for k in range(maxheight + 1):
                val = f[i-1][j][k]
                if j - widths[0] >= 0 and k - heights[0] >= 0:
                    val = max(val, f[i-1][j - widths[0]][k - heights[0]] + cost[i])
                f[i][j][k] = val

    return f[-1][-1][-1]