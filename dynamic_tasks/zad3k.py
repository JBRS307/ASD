from zad3ktesty import runtests
import sys

sys.setrecursionlimit(1<<20)

def ksuma( T, k ):
    n = len(T)
    memo = [float('inf')]*n

    def rec(i):
        nonlocal T, memo, k
        if memo[i] != float('inf'):
            return memo[i]
        if i-k < 0:
            memo[i] = T[i]
            return memo[i]
        
        min_sum = float('inf')
        for j in range(i-1, i-1-k, -1):
            min_sum = min(min_sum, rec(j))
        memo[i] = min_sum+T[i]
        return memo[i]
    
    min_sum = float('inf')
    for i in range(n-k, n):
        min_sum = min(min_sum, rec(i))
    return min_sum

def tab_ksum(T, k):
    n = len(T)
    dp = [float('inf')]*n

    for i in range(k):
        dp[i] = T[i]
    
    for i in range(k, n):
        for j in range(i-1, i-1-k, -1):
            dp[i] = min(dp[i], dp[j]+T[i])
    
    return min(dp[n-k:])

runtests(tab_ksum)
# runtests(ksuma)