# Jakub Rękas

# Algorytm działa w czasie O(n^2). Wykorzystuje on metodę wstępującą. Dla każdego parkingu
# oblicza minimalną cenę, jaką trzeba zapłacić, żeby do niego dojechać w dwóch wypadkach: najpierw
# jeśli nie możemy wykorzystać podwojonego dystansu, później jeśli możemy.
# Wybiera on minimalną cenę w zasięgu wstecz.

from zad9testy import runtests
from math import inf

def merge_OC(O, C):
    P = []
    for i in range(len(O)):
        P.append((O[i], C[i]))
    return P

def min_cost( O, C, T, L ):
    P = merge_OC(O, C)
    P.append((L, 0))
    P.append((0, 0))
    P.sort()
    n = len(P)

    # w kolumnie 0 bez możliwości podwojenia dystansu
    # w kolumnie 1 z możliwością podwojenia dystansu
    dp = [[inf]*2 for _ in range(n)] 
    
    it = 0
    while P[it][0] <= T:
        dp[it][0] = 0
        it += 1

    for i in range(it, n):
        min_cost = inf
        for j in range(i-1, -1, -1):
            if P[i][0]-P[j][0] > T:
                break
            min_cost = min(min_cost, dp[j][0]+P[j][1])
        dp[i][0] = min_cost
    
    it = 0
    while P[it][0] <= T<<1: # przyspieszam to jak mogę
        dp[it][1] = 0
        it += 1
    
    for i in range(it, n):
        min_cost = inf
        for j in range(i-1, -1, -1):
            if P[i][0]-P[j][0] > T<<1:
                break
            min_cost = min(min_cost, dp[j][0]+P[j][1])
        for j in range(i-1, -1, -1):
            if P[i][0]-P[j][0] > T:
                break
            min_cost = min(min_cost, dp[j][1]+P[j][1])
        dp[i][1] = min_cost
    
    return min(dp[n-1][0], dp[n-1][1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
