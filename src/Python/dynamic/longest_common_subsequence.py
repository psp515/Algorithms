"""
Problem
------------
Find longest common subsequence.

Parameters
----------
A: array
    array of elements
B: array
    array of elements

Algorithm
---------

Finding longest common to i-th element in A array and in whole B array.

Complexity O(n^2)

"""
def lcs(A, B):
    n, m = len(A), len(B)
    f = [[0 for _ in range(m+1)]for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            tmp = 0
            if A[i-1] == B[j-1]:
                tmp = f[i-1][j-1] + 1
            f[i][j] = max(tmp, f[i-1][j], f[i][j-1])

    return f[-1][-1]

def _test(A, B, V):
    ans = lcs(A, B)
    print("Is valid: ", ans == V, "Ans: ", ans)

def test():
    print("------------- lcs ------------")
    A = [1, 5, 3, 2, 5, 4, 22, 1230]
    B = [3, 7, 2, 5, 7, 9, 4, 23]
    ans = 4
    _test(A, B, ans)