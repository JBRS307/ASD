#Do implementacji find/union wystarczą dwie tablice - jedna zawiera parent każdego wierzchołka, druga zawiera ich rangi.
#Korzeń drzewa ma jako parent siebie

#Tablica rank jest na początku wypełniona zerami

def kruskal(G):
    n = len(G)
    parent = [i for i in range(n)]
    rank = [0]*n

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
    
    