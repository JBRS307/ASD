from egzP8btesty import runtests

def list_to_matrix(G):
    n = len(G)
    M = [[float('inf')]*n for _ in range(n)]

    for i in range(n):
        for edge in G[i]:
            M[i][edge[0]] = edge[1]
    
    for i in range(n):
        M[i][i] = 0
    
    return M

def george_floyd(G):
    n = len(G)
    dist = [[elem for elem in line] for line in G]

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if dist[u][t]+dist[t][v] < dist[u][v]:
                    dist[u][v] = dist[u][t] + dist[t][v]
    
    return dist

def robot( G, P ):
    M = list_to_matrix(G)

    dist = george_floyd(M)

    res = 0
    for i in range(1, len(P)):
        res += dist[P[i-1]][P[i]]
    return res
    
runtests(robot, all_tests = True)
