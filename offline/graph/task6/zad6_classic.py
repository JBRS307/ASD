from zad6testy import runtests
from collections import deque
import math

def build_bgraph(M, n):
    G = [[0]*(2*n) for _ in range(2*n)]

    for i in range(n):
        for machine in M[i]:
            G[i][n+machine] = 1
    
    for i in range(2*n):
        G[i].extend([0, 0])
    
    G.append([0 for _ in range(2*n+2)])
    G.append([0 for _ in range(2*n+2)])

    for i in range(n): #source
        G[-2][i] = 1
    
    for i in range(n, 2*n): #sink
        G[i][-1] = 1

    return G

def BFS(G, s, t, parent):
    n = len(G)
    q = deque()
    visited = [False]*n
    q.append(s)
    visited[s] = True

    while q:
        u = q.popleft()
        for i in range(n):
            if G[u][i]:
                if not visited[i]:
                    q.append(i)
                    parent[i] = u
                    visited[i] = True
                    if i == t:
                        return True
    return False

def ford(G, s, t):
    n = len(G)
    parent = [None]*n
    max_flow = 0

    while BFS(G, s, t, parent):
        path_flow = math.inf
        v = t
        while v != s:
            path_flow = (G[parent[v]][v] if G[parent[v]][v] < path_flow else path_flow)
            v = parent[v]
        
        max_flow += path_flow

        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = u
        
    return max_flow


def binworker( M ):
    G = build_bgraph(M, len(M))
    n = len(G)
    return ford(G, n-2, n-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )


# M = [ [ 0, 1, 3],
#     [ 2, 4],
#     [ 0, 2],
#     [ 3 ],
#     [ 3, 2] ]

# G = build_bgraph(M, len(M))

# print(*G, sep="\n")

# print(binworker(M))
