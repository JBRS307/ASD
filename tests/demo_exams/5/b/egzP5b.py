from egzP5btesty import runtests

def process(B):
    for i in range(len(B)):
        if B[i][0] > B[i][1]:
            B[i] = (B[i][1], B[i][0])

def find_len(T):
    n = 0
    for ticket in T:
        for elem in ticket:
            n = (elem if elem > n else n)
    
    return n+1

def DFS(G, s, ban):
    n = len(G)
    visited = [False]*n
    visited[ban] = True

    def DFSvisit(s):
        nonlocal G, visited
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                DFSvisit(v)
    
    DFSvisit(s)
    
    return (False in visited)

def edges_to_list(T, n):
    G = [[] for _ in range(n)]

    for edge in T:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    
    return G

def koleje ( B ):
    process(B)
    B.sort(key=lambda x: (x[0], x[1]))
    
    T = []
    prev = None
    for ticket in B:
        if ticket != prev:
            T.append(ticket)
            prev = ticket
    n = find_len(T)
    G = edges_to_list(T, n)

    res = 0
    if DFS(G, 1, 0):
        res += 1
    for i in range(1, n):
        if DFS(G, 0, i):
            res += 1
    
    return res
    

runtests ( koleje, all_tests=True )