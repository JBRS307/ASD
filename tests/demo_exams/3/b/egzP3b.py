from egzP3btesty import runtests 

def list_to_edge(G):
    new_G = []
    mass = 0
    for i in range(len(G)):
        for neigh in G[i]:
            if i < neigh[0]:
                new_G.append((i, neigh[0], neigh[1]))
                mass += neigh[1]
    return new_G, mass

def kruskal(G, n, mass):
    parent = [i for i in range(n)]
    rank = [0]*n
    # MST = []
    
    def find(x):
        nonlocal parent
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
    
    not_taken = None
    for i in range(len(G)):
        x = G[i][0]
        y = G[i][1]

        rep_x = find(x)
        rep_y = find(y)

        if rep_x != rep_y:
            # MST.append(G[i])
            mass -= G[i][2]
            union(x, y)
        elif not_taken is None:
            not_taken = i
    
    if not_taken is not None:
        mass -= G[not_taken][2]
    return mass


def lufthansa ( G ):
    n = len(G)
    G, mass = list_to_edge(G)
    G.sort(key=lambda x: -x[2])

    return kruskal(G, n, mass)

    

runtests( lufthansa, all_tests=True )