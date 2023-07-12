from egzP1btesty import runtests
from queue import PriorityQueue

def edges_to_list(G):
    n = 0
    for edge in G:
        n = max(n, edge[0], edge[1])
    n += 1

    G_list = [[] for _ in range(n)]
    for edge in G:
        G_list[edge[0]].append((edge[1], edge[2]))
        G_list[edge[1]].append((edge[0], edge[2]))
    
    return G_list

def to_l(V, L):
    for i in range(len(V)):
        if V[i][0] == L:
            return True
    return False

def dijkstra(G, D, L):
    n = len(G)
    q = PriorityQueue()
    visited = [False]*n
    dist = [[float('inf'), float('inf')] for _ in range(n)]
    dist[D] = [0, 0]
    q.put((0, D))

    while not q.empty():
        _, u = q.get()
        for v, weight in G[u]:
                if not visited[v] and dist[u][0] + weight < dist[v][0]:
                    dist[v][0] = weight + dist[u][0]
                    dist[v][1] = dist[u][1]+1
                    q.put((dist[v][0], v))
                elif dist[u][1] + 1 < 4 and dist[v][1] >= 4:
                    dist[v][1] = dist[u][1] + 1
                    dist[v][0] = dist[u][0] + weight
                    q.put((dist[v][0], v))
        visited[u] = True
    
    return dist


def turysta( G, D, L ):
    G = edges_to_list(G)
    n = len(G)

    return dijkstra(G, D, L)[L][0]

runtests ( turysta )