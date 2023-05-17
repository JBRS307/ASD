from zad8testy import runtests
import math

def kruskal(G, n):
    parent = [i for i in range(n)]
    rank = [0]*n
    MST = []

    def find(x):
        nonlocal parent, rank
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        nonlocal parent, rank
        x = find(x)
        y = find(y)

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
    
    for edge in G:
        x = edge[0]
        y = edge[1]

        rep_x = find(x)
        rep_y = find(y)

        if rep_x != rep_y:
            MST.append(edge)
            union(x, y)
    
    rep = find(0)
    for i in range(1, n):
        rep_next = find(i)
        if rep_next != rep:
            return None
    
    return MST



def highway( A ):
    n = len(A)
    G = []

    

    for i in range(n):
        for j in range(i+1, n):
            dist = math.sqrt(math.pow(A[i][0]-A[j][0], 2)+math.pow(A[i][1]-A[j][1], 2))
            dist = math.ceil(dist)
            G.append((i, j, dist))
    
    G.sort(key=lambda x: x[2])

    min_days = math.inf

    while True:
        MST = kruskal(G, n)
        if MST is None:
            break

        new_days = MST[-1][2] - MST[0][2]
        min_days = new_days if new_days < min_days else min_days
        G.pop(0)
    
    return min_days
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )

# A = [(100, 100), (100, 200), (210, 100), (210, 200)]
# print(highway(A))