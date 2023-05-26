from kol2testy import runtests
from collections import deque

def BFS(G, v):
    visited = [False]*len(G)
    q = deque()
    visited[v] = True
    q.append(v)

    while q:
        s = q.popleft()
        for neigh in G[s]:
            if not visited[neigh]:
                visited[neigh] = True
                q.append(neigh)
    
    return False not in visited


def list_to_edge(G, n):
    E = []
    for s in range(n):
        for neigh in G[s]:
            if s < neigh[0]:
                E.append((s, neigh[0], neigh[1]))
    return E

def edge_to_list(E, n):
    G = [[] for _ in range(n)]

    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    
    return G


def beautree(G):
    n = len(G)
    E = list_to_edge(G, n)
    m = len(E)

    E.sort(key=lambda x: x[2])

    T = E[:n-1]
    mass = 0
    for edge in T:
        mass += edge[2]

    T = edge_to_list(T, n)

    first = 0
    last = n-1
    if BFS(T, 0):
        min_mass = mass
    else:
        min_mass = float('inf')

    while last < m:
        rem = E[first]
        add = E[last]

        T[rem[0]].remove(rem[1])
        T[rem[1]].remove(rem[0])

        T[add[0]].append(add[1])
        T[add[1]].append(add[0])

        mass -= rem[2]
        mass += add[2]

        if BFS(T, 0):
            min_mass = mass if mass < min_mass else min_mass
        
        first += 1
        last += 1
    
    return min_mass if min_mass != float('inf') else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
