from kol3btesty import runtests
from queue import PriorityQueue
import math as m

def add_flying(G, A, n):
    A.append(0)
    
    for i in range(n):
        G[i].append((n, A[i]))
    
    new_vert = []
    for i in range(n):
        new_vert.append((i, A[i]))
    G.append(new_vert)

def dijkstra(G, s, t, n):
    visited = [False]*n
    dist = [m.inf]*n
    q = PriorityQueue()
    dist[s] = 0
    q.put((0, s))

    while not q.empty():
        _, u = q.get()
        for v, value in G[u]:
            if not visited[v]:
                if dist[u]+value < dist[v]:
                    dist[v] = dist[u]+value
                    q.put((dist[v], v))
        visited[u] = True
        if visited[t]:
            return dist[t]


def airports( G, A, s, t ):
    n = len(G)

    # print(G)

    add_flying(G, A, n)
    # print(G)

    return dijkstra(G, s, t, n+1)   


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )