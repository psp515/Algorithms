"""
Problem
------------
Geting order of matrix multiplification that needs minimal number of operations.

Parameters
----------
p : array
    list of matrix sizes

Algorithm
---------

Finding minimal number of actios with multyplying matrix 0..i * j * k...n.

Complexity: O(n^3)

"""

def mcs(p):
    n = len(p)
    f = [[0 for _ in range(n)] for _ in range(n)]
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            f[i][j] = float('inf')
            for k in range(i, j):

                # q = cost / scalar multiplications
                q = f[i][k] + f[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < f[i][j]:
                    f[i][j] = q

    return f[1][n-1]