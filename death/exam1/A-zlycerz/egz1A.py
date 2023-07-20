# Jakub Rękas

# Na początku tworzymy tzw. graf pościgowy, który ma każdą krawędź podwojoną, oraz do tego iloczynu dodane jest r.
# Następnie po każdym z tych grafów puszczamy algorytm dijkstry, po grafie zwykłym z wierzchołka s (przed rabunkiem) 
# oraz po grafie pościgowym z wierzchołka t (po rabunku). Zapisujemy sobie obie tablice dystansów. Następnie szukamy takiego wierzchołka, 
# dla którego dystans od s przed rabunkiem oraz dystans do t po rabunku (czyli koszty podróży)
# minus to co ukradliśmy (teraz to całkowity kosz podróży), jest jak najmniejszy. Robimy to liniowo w pętli
# Na koniec zwracamy to minimum

# Złożoność pamięciowa O(V+E)(na nowy graf)
# Złośoność czasowa O(V+E+2ElogV+V) = O(ElogV) ~ O(V^2logV) (krawędzi może być co najwyżej V^2)

from egz1Atesty import runtests
from queue import PriorityQueue
inf = float('inf')

def six_star_chase(G, r):
    n = len(G)
    chase_G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            chase_G[i].append((G[i][j][0], G[i][j][1]*2+r))
    return chase_G

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    dist = [inf]*n
    dist[s] = 0
    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        _, u = q.get()
        for v, weight in G[u]:
            if not visited[v]:
                if dist[u]+weight < dist[v]:
                    dist[v] = dist[u]+weight
                    q.put((dist[v], v))
        visited[u] = True
    
    return dist
    

def gold(G,V,s,t,r):
    n = len(G)
    chase_G = six_star_chase(G, r)
    from_s = dijkstra(G, s)
    from_t = dijkstra(chase_G, t)
    min_cost = inf
    for i in range(n):
        cost = from_s[i]+from_t[i]-V[i]
        min_cost = min(min_cost, cost)
    return min_cost



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True)
