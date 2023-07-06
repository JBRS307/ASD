def player(A, x, y):
    n = len(A)
    m = len(A[0])
    vis = [[False] * m] * n
    cnt = 0
    def DFS(a,b):
        nonlocal cnt
        vis[a][b] = True
        cnt += 1
        if a+1 < n and not vis[a+1][b]:
            DFS(a+1,b)
        if a - 1 > 0 and not vis[a-1][b]:
            DFS(a-1,b)
        if b+1 < m and not vis[a][b+1]:
            DFS(a,b+1)
        if b - 1 > 0 and not vis[a][b-1]:
            DFS(a,b-1)
    DFS(x,y)
    return cnt
