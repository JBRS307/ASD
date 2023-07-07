from zad1testy import runtests
from math import inf


def dijkstra(G, A, B):
    n = len(G)
    visited = [False]*n
    dist = [(inf, -1)]*n
    dist[A] = (0, -1) # stąd możemy sobie wyjść w każdy możliwy sposób

    while True:
        min_dist = inf
        min_ind = None
        transport = -1
        for i in range(n):
            if dist[i][0] < min_dist and not visited[i]:
                min_dist = dist[i][0]
                min_ind = i
                transport = dist[i][1]

        if min_ind is None or min_ind == B:
            return dist
        
        for i in range(n):
            if not visited[i] and min_ind != i and G[min_ind][i] and G[min_ind][i] != transport and \
               dist[min_ind][0] + G[min_ind][i] < dist[i][0]:
                dist[i] = (dist[min_ind][0] + G[min_ind][i], G[min_ind][i])
        visited[min_ind] = True

def islands(G, A, B):
    dist = dijkstra(G, A, B)
    return dist[B][0] if dist[B][0] != inf else None
        

runtests( islands )

# G = [
#     [0, 1, 8],
#     [0, 0, 1],
#     [8, 0, 0]
# ]
# A = 0
# B = 2

# print(islands(G, A, B))
