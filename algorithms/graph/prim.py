#tree dijkstra

from queue import PriorityQueue

def tree_dijkstra(G, s):
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    dist = [float('inf')]*n
    dist[s] = 0
    q = PriorityQueue()

    q.put((0, s))
    while not q.empty():
        _, u = q.get()
        for v, value in G[u]:
            if not visited[v] and value < dist[v]:
                dist[v] = value
                parent[v] = u
                q.put((dist[v], v))
        visited[u] = True
    
    return parent

if __name__ == "__main__":
    G = [
    [(1, 3), (2, 4)],
    [(0, 3), (2, 1), (3, 2)],
    [(0, 4), (1, 1), (3, 5)],
    [(1, 2), (2, 5), (4, 6)],
    [(3, 6), (5, 7)],
    [(4, 7), (6, 8)],
    [(5, 8), (7, 9)],
    [(6, 9), (8, 10)],
    [(7, 10), (9, 11)],
    [(8, 11)]
]

print(*tree_dijkstra(G, 0))