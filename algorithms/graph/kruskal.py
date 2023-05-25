#Do implementacji find/union wystarczą dwie tablice - jedna zawiera parent każdego wierzchołka, druga zawiera ich rangi.
#Korzeń drzewa ma jako parent siebie

#Tablica rank jest na początku wypełniona zerami

def kruskal(G, n):
    parent = [i for i in range(n)]
    rank = [0]*n
    MST = []
    # visited = [False]`*n

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
    
    G.sort(key=lambda x: x[2])

    for edge in G:
        x = edge[0]
        y = edge[1]

        rep_x = find(x)
        rep_y = find(y)

        if rep_x != rep_y:
            MST.append(edge)
            union(x, y)
    
    return MST

    


if __name__ == "__main__":
    G = [
        (0, 1, 2),
        (1, 2, 3),
        (2, 3, 1),
        (0, 3, 4),
        (3, 4, 5),
        (4, 5, 6),
        (5, 6, 7),
        (6, 7, 8),
        (7, 8, 9),
        (8, 9, 10),
        (9, 0, 11),
        (0, 2, 12),
        (2, 4, 13),
        (4, 6, 14),
        (6, 8, 15)
    ]
    
    MST = kruskal(G, 15)

    print(*MST, sep="\n")
    