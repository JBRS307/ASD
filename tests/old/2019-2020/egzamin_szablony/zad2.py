from zad2testy import runtests
from math import inf



def opt_sum(tab):
    arr = tab # wolę takie nazewnictwo, a to jest tylko przypisanie wskaźnika w O(1)
    n = len(arr)

    S = [arr[i] for i in range(n)]
    for i in range(1, n):
        S[i] += S[i-1]
    
    A = [[inf]*n for _ in range(n)]

    def rec(i, j):
        nonlocal A, S
        if i == j:
            A[i][j] = 0
        elif j-i == 1:
            A[i][j] = abs(arr[i]+arr[j])
        elif A[i][j] == inf:
            curr_sum = abs(S[j]-S[i-1] if i > 0 else S[j])
            for k in range(i, j):
                A[i][j] = min(A[i][j], max(curr_sum, rec(i, k), rec(k+1, j)))
        return A[i][j]
    
    rec(0, n-1)
    return A[0][n-1]

runtests( opt_sum )
