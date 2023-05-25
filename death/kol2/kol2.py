# Jakub Rękas

# Na początku za pomocą BFSa sprawdzamy, czy graf jest spójny, jeśli nie, zwracamy None.
# Działanie algorytmu opiera się na algorytmie kruskala, najpierw należy przerobić listę sąsiadów na listę krawędzi (O(V+E)),
# następnie po kolei budować MST, budujemy tyle, ile wynosi krawędzi, w każdej iteracji jednak zaczynamy od krawędzi
# z coraz wyższą wagą. Jeśli w drzewie jest dziura (czyli jakaś krawędź zostaje wzięta do MST, gdy poprzednia nie została wzięta), to
# tego drzewa w ogóle nie bierzemy pod uwagę, przerywamy wtedy pętlę i nie modyfikujemy zmiennej zawierającej minimalną wagę pięknego
# drzewa. Jeśli taka sytuacja nie zachodzi, sprawdzamy, czy to co nam wyszło jest w ogóle spójne, jeśli nie, to również nie bierzemy
# tego pod uwagę. Jeśli visited każdego wierzchołka w grafie jest równe True, znaczy, że mst jest spójne i możemy porównać jego masę
# z masą aktualnie najmniejszą.

#Złożoności O(ElogV + V + E + E(E+V)) = O(E^2 + VE). Jeśli E ~ V, to wtedy O(V^2 + V^2) = O(V^2) = O(E)
# Jeśli E ~ V^2 to O(V^4 + V^3) = O(V^4) = O(E^2)


from kol2testy import runtests
from collections import deque

def BFS(G, v):
    n = len(G)
    visited = [False]*n
    q = deque()
    visited[v] = True
    q.append(v)

    while len(q) != 0:
        s = q.popleft()
        for neigh, _ in G[s]:
            if not visited[neigh]:
                visited[neigh] = True
                q.append(neigh)
    
    return not(False in visited)



def list_to_edges(G):
    n = len(G)

    edges = []
    for i in range(n):
        for elem in G[i]:
            if i < elem[0]:
                edges.append((i, elem[0], elem[1]))
    return edges


def kruskal(G, n):
    G.sort(key=lambda x: x[2])
    # parent = [i for i in range(n)]
    # rank = [0]*n
    MST = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
    
    min_mass = float('inf')
    for start in range(len(G)):
        not_taken = None
        MST = []
        rank = [0]*n
        parent = [i for i in range(n)]
        mass = 0
        visited = [False]*n
        for i in range(start, len(G)):
            edge = G[i]
            x = edge[0]
            y = edge[1]
            visited[x] = visited[y] = True

            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                MST.append(edge)
                union(x, y)
                mass += edge[2]
                if not_taken == i-1:
                    break
            else:
                not_taken = i
        else:
            if mass != 0 and not(False in visited):
                min_mass = mass if mass < min_mass else min_mass
    
    return min_mass


def beautree(G):

    if not BFS(G, 0):
        return None

    E = list_to_edges(G)


    return kruskal(E, len(G))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
