#Jakub Rękas

#Trzeba puścić algorytm Dijkstry z a i sprawdzić dystans do b
#
#1. Należy dodać planety z S do grafu. Da się to zrobić O(S). Należy, do listy krawędzi E, dla pierwsze planety z S
#dodać jej krawędź do każdej innej z S o wadze 0. W ten sposób w reprezentacji listowej wszystkie planety z S będą połączone z jedną.
#Ponieważ jednak czasy podróży między tymi planetami są równe 0, to nie ma znaczenia czy polecimy bezpośrednio między dwiema czy
#przez jedną planetę pośrednią.
#2. Graf należy przerobić na reprezentację listową robi się to bardzo prosto w czasie O(E+S). Dla każdej krawędzi, w reprezentacji
#listowej dodajemy wierzchołek sąsiedni z odpowiednią wagą, robimy tak dla obu wierzchołków w krotce w liście krawędzi.
#3. Z wykorzystaniem listy sąsiadów odpalamy na grafie algorytm dijkstry z punktu a, algorytm zwraca tablice dystansów każdego
#wierzchołka od punktu a.
#4. Jeśli dystans od a do b wynosi nieskończoność, to znaczy, że ścieżka od a do b nie istnieje, ponieważ każdy wierzchołek
#został zainicjalizowany z tą wartością, co oznacza, że algorytm go nie przetworzył. Należy zwrócić None. W przeciwnym razie
#zwracamy ten dystans.


from zad5testy import runtests
from queue import PriorityQueue

def edge_to_list(E, n):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    
    return G

def dijkstra(G, s, t, n):
    dist = [float('inf')]*n
    visited = [False]*n
    q = PriorityQueue()
    dist[s] = 0

    q.put((0, s))
    while not q.empty():
        d, u = q.get()
        for v, value in G[u]:
            if not visited[v]:
                if d+value < dist[v]:
                    dist[v] = d+value
                    q.put((dist[v], v))
        
        visited[u] = True
        if visited[t]:
            return dist
    
    return None


def spacetravel( n, E, S, a, b ): #n - |V|, E - lista krawędzi, S - planety, gdzie można się teleportować, a - start, b - koniec
    n_anom = len(S)

    for i in range(1, n_anom):
        E.append((S[0], S[i], 0))
    
    G = edge_to_list(E, n)

    dist = dijkstra(G, a, b, n)
    if dist is None:
        return None

    return dist[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )