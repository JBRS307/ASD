from zad5ktesty import runtests

def beat_the_motherfucker(A):
    n = len(A)
    memo = [[0]*n for _ in range(n)]

    def game(i, j):
        nonlocal memo, A, n
        if i > j:
            return 0
        if i == j:
            memo[i][i] = A[i]
            return A[i]
        if memo[i][j] != 0:
            return memo[i][j]
        
        memo[i][j] = max(min(game(i+1, j-1), game(i+2, j))+A[i], min(game(i+1, j-1), game(i, j-2))+A[j])
        return memo[i][j]
    
    return game(0, n-1)

def garek ( A ):
    return beat_the_motherfucker(A)

runtests ( garek )