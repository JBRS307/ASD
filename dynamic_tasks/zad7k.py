from zad7ktesty import runtests 

def DFS(T, s, visited):
    root_leng = 0
    m = len(T)
    n = len(T[0])
    
    def DFSvisit(i, j):
        nonlocal root_leng, visited
        if not visited[i][j]:
            visited[i][j] = True
            root_leng += T[i][j]
            if i-1 >= 0 and T[i-1][j]:
                DFSvisit(i-1, j)
            if i+1 < m and T[i+1][j]:
                DFSvisit(i+1, j)
            if j+1 < n and T[i][j+1]:
                DFSvisit(i, j+1)
            if j-1 >= 0 and T[i][j-1]:
                DFSvisit(i, j-1)
    
    DFSvisit(0, s)
    return root_leng

def knapsack(T, Z, l):
    n = len(T)
    dp = [[0]*(l+1) for _ in range(n)]

    for i in range(l+1):
        if T[0] <= i:
            dp[0][i] = Z[0]

    for i in range(1, n):
        for j in range(l+1):
            dp[i][j] = dp[i-1][j]
            if T[i] <= j:
                dp[i][j] = max(dp[i][j], dp[i-1][j-T[i]]+Z[i])
    
    return dp

def ogrodnik (T, D, Z, l):
    m = len(T)
    n = len(T[0])
    visited = [[False]*n for _ in range(m)]
    trees = []
    for location in D:
        trees.append(DFS(T, location, visited))
    
    dp = knapsack(trees, Z, l)
    return dp[-1][-1]
    


runtests( ogrodnik, all_tests=True )
