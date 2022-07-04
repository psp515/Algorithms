import math


def cut_rod(arr, rod_len):
    f = [-math.inf for i in range(rod_len+1)]
    f[0] = 0

    for i in range(rod_len + 1):
        q = f[i]
        for j in range(0, rod_len + 1):
            q = max(f[i], f[i - j] + arr[j])
        f[i] = q

    return f[-1]